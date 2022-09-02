"""
Collects data and parses into a JSON to send database for dashboard

The collector is the manager of all other src daemons. It hadnles scheduling
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


def listen():
    return


def request():
    return


def package_telemetry():
    return


class Telemetry:

    def __init__(self):
        self.filepath = "../../../config.toml"
        self.config = utils.load_config(self.filepath)
        self.scheduler()

    def scheduler(self):
        for key, value in self.config.items():
            print(key, value)
        return


    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    # return


if __name__ == '__main__':
    Telemetry()