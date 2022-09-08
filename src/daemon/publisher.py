class Publisher:
    # Pushing the data to home should be a different daemon than collector
    # this way we can keep local data in local storage and publish whenever
    # we want. They can be asynchronous processes.
    def __init__(self):
        print("gotta do this soon")