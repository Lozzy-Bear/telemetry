"""
Collects data and parses into a JSON to send database for dashboard

The collector is the manager of all other src daemons. It handles scheduling
when other daemons should run and makes pull requests from them for data. Some
daemons may need to run in a continuously monitoring mode, in this case the
collector listens for new data. The collector also packages all the src data
into a JSON format file and pushes that to the dashboard database.

Dataclasses are preferred but JSON to DICT is so straight forward.

How should config be done? config.toml? config.py?
"""
import schedule
import time
import datetime
import src.utils.utils as utils
import asyncio


class Telemetry:

    def __init__(self):
        self.filepath = "../../../config.toml"
        self.config = utils.load_config(self.filepath)

    def scheduler(self):
        """
        From the config file determines the schedules when scripts should run, in push or pull, and
        which scripts should be loaded.
        """

        # Daemons that are not commented out should be started up


        # Check if the Daemon is in push or pull. In pull set up schedule in push set up a socket.
        # Maybe always using a socket is just better? Let all the daemons run concurrently at
        # their own schedules and have collectord just make sure they are running?


        # Find all the daemons

        jobs = []
        for key, value in self.config['scripts'].items():
            print(self.config['scripts'][key])
            jobs.append(utils.Script(self.config['scripts'][key],
                                     self.config['scripts'][key]['entry'],
                                     self.config['scripts'][key]['schedule']))
            # print(key, value)
        for job in jobs:
            job.start()

        return


if __name__ == '__main__':
    Telemetry()
