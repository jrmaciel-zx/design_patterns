class MetaSingleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if not self in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]

class Logger(metaclass = MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()

print(logger1, logger2)