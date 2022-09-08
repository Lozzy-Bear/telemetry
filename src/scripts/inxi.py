import datetime
import json
import src.common.utils as utils


def inxi_cli(config):
    print('executing inxi')
    cmd = f"inxi --tty --no-sudo -v 8 -w --weather-unit m --output json --output-file print"
    msg = utils.execute_cmd(cmd)
    msg = json.loads(msg)
    msg['time'] = datetime.datetime.utcnow().strftime('YY-mm-DD HH:MM:SS')
    return {'inxi_cli': msg}
