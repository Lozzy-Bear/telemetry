import os
import json
import tomllib as toml
import subprocess
import asyncio
from contextlib import suppress
import importlib

def merge_dicts(*dictionary_args):
    merged = {}
    for dictionary in dictionary_args:
        merged.update(dictionary)
    return merged


def write_json(data: dict, filepath: str):
    if not filepath.endswith('.json'):
        filepath += '.json'
    with open(filepath, 'w') as fp:
        json.dump(data, fp)
    return


def load_config(filepath):
    with open(filepath, 'rb') as fp:
        config = toml.load(fp)

    if config['general']['nodename'] == '':
        config['general']['nodename'] = os.uname()[1]

    return config


def execute_cmd(cmd):
    # try/except block lets install script continue even if something fails
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        output = {'cmd_error': err.output}
    return output.decode('utf-8')


class Script:
    # todo: include script restarting or failure is okay and doesn't halt everything else
    def __init__(self, config, func, wait):
        # Let us expect config to be a dict with everything we need
        self.func = getattr(importlib.import_module(name='src.daemons.testd.testd'), 'test_script')
        # self.func = getattr(importlib.import_module('src.daemons.testd.testd'), 'test_script')
        self.func()
        self.config = config
        self.wait = wait
        self._running = False
        self._task = None

    def _setup(self):
        # Read the config data and setup the script.
        return

    async def start(self):
        if not self._running:
            self._running = True
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        if self._running:
            self._running = False
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        while True:
            await asyncio.sleep(self.wait)
            self.func(self.config)
