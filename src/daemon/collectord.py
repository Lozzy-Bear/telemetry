"""
Collects data and parses into a JSON to send database for dashboard

The collector is the manager of all other src daemon. It handles scheduling
when other daemon should run and makes pull requests from them for data. Some
daemon may need to run in a continuously monitoring mode, in this case the
collector listens for new data. The collector also packages all the src data
into a JSON format file and pushes that to the dashboard database.
"""
import datetime
from src.common.classes import Script
import asyncio
import tomllib as toml
import os
import json


class Collector:
    def __init__(self):
        self.config_file = "../../config.toml"
        self.file_prefix = ''
        self.config = {}
        self.data = {}
        self.tasks = []
        self.load_config()
        self.load_scripts()
        self.wait = 10
        asyncio.run(self.run())

    def load_config(self):
        with open(self.config_file, 'rb') as fp:
            self.config = toml.load(fp)

        if self.config['general']['nodename'] == '':
            self.config['general']['nodename'] = os.uname()[1]

        if not os.path.isdir(self.config['general']['directory']):
            print('ERROR: directory not found =' +
                  self.config['general']['directory'])
            exit()

        self.file_prefix = self.config['general']['directory'] + 'telemetry_' + \
                           self.config['general']['site'] + '_' + \
                           self.config['general']['nodename']
        self.data = {'general': self.config['general']}

    def load_scripts(self):
        for key, value in self.config['scripts'].items():
            self.tasks.append(Script(self.config['scripts'][key]))

    async def write_json(self):
        time = datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S')
        file = self.file_prefix + '_' + time + '.json'
        with open(file, 'w') as fp:
            json.dump(self.data, fp)
        print(self.data)

    async def run(self):
        for task in self.tasks:
            await task.start()

        while True:
            await asyncio.sleep(self.wait)
            for task in self.tasks:
                self.data.update(task.data)
            await self.write_json()


if __name__ == '__main__':
    Collector()
