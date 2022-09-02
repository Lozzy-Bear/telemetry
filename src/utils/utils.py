import os
import json
import tomllib as toml
import datetime
import subprocess


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


if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 1, 'd': 2}
    m = merge_dicts(d1, d2)
    print(m)
    write_json(m, '/home/arl203/icebear/telemetry/test')
    print(load_config('/home/arl203/icebear/telemetry/config.toml'))

