from abc import abstractmethod, ABCMeta

class State(metaclass = ABCMeta):
    @abstractmethod
    def doThis(self):
        pass

class StartState(State):
    def doThis(self):
        print("TV switching on")

class StopState(State):
    def doThis(self):
        print("TV switching off")

class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()

context = TVContext()
start = StartState()
stop = StopState()

context.setState(start)
context.doThis()