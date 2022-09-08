import json
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


def execute_cmd(cmd):
    # try/except block lets install script continue even if something fails
    try:
        output = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        output = {'cmd_error': err.output}
    return output.decode('utf-8')
