import datetime


def test_script(config):
    print(f"This job is running: {datetime.datetime.utcnow()}")
    data = {'a': 1, 'b': 'test data dict', 'time': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}
    return {'test_script': data}

