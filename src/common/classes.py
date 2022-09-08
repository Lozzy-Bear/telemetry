import asyncio
from contextlib import suppress
import importlib


class Script:
    # todo: include script restarting or failure is okay and doesn't halt everything else
    def __init__(self, config):
        module, func = config['entry'].rsplit('.', 1)
        self.func = getattr(importlib.import_module(module), func)
        self.config = config
        self.wait = config['schedule']
        self._running = False
        self._task = None
        self.data = {}

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

    def schedule(self):
        # updates wait time for next sampling given config
        self.wait = 10

    async def _run(self):
        while True:
            await asyncio.sleep(self.wait)
            self.data = self.func(self.config)
