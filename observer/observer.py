from abc import ABCMeta, abstractmethod

class Subject():
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def deregister(self, observer):
        self.__observers.remove(observer)

    def notifyAll(self, *args):
        for observer in self.__observers:
            observer.notify(self, *args)

class Observer(metaclass = ABCMeta):
    @abstractmethod
    def notify(self, subject, *args):
        pass

    @abstractmethod
    def deregister(self):
        pass
   
class Observer1(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, subject, *args):
        print(type(self), "Got ", args, "from ", subject)

    def deregister(self):
        self.subject.deregister(self)

class Observer2(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    def notify(self, subject, *args):
        print(type(self), "Got ", args, "from ", subject)        

    def deregister(self):
        self.subject.deregister(self)        

t = Subject()
x = Observer1(t)
j = Observer2(t)
t.notifyAll("Notification 1")

x.deregister()
t.notifyAll("NOtification 2")