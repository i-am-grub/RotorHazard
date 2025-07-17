from rotorhazard.interface.sensor import Reading, Sensor


class StubSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self, 'TestSensor')
        self.address = 123
        self.value = 0

    @Reading(units='')
    def counter(self):
        return self.value

    def update(self):
        self.value += 1

def discover(*args, **kwargs):
    return [StubSensor()]
