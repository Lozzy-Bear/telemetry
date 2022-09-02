import datetime
import json
import src.utils.utils as utils


class Inxi:
    def __init__(self, filename):
        self.site = config['site']
        self.name = config['name']
        self.device = config['device']
        self.run_command()
        print(self.msg)

    def run_command(self):
        # the --tty command is required since we are running inxi from within python
        cmd = f"inxi --tty --no-sudo -v 8 -w --weather-unit m --output json --output-file print"
        msg = utils.execute_cmd(cmd)
        msg = json.loads(msg)
        msg['time'] = datetime.datetime.utcnow().strftime('YY-mm-DD HH:MM:SS')
        msg


        # with open(self.file, 'w') as fp:
        #     json.dump(msg, fp)


if __name__ == '__main__':
    DeviceInfo(config)
