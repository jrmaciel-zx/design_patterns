class Model(object):
    def logic(self):
        data = "Got it!"
        print("Model: Crunching data as per business logic")
        return(data)

class View(object):
    def update(self, data):
        print("View: Updating the view with results: ", data)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: Relayed the Client asks")
        data = self.model.logic()
        self.view.update(data)

class Client(object):
    print("Client: Asks for certain information")
    controller = Controller()
    controller.interface()

if (__name__ == "__main__"):
    t = Client()