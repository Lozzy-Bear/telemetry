import datetime


def test_script(config):
    print(f"This job is running: {datetime.datetime.utcnow()}")
    data = {'a': 1, 'b': 'test data dict'}
    return data

