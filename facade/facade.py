class    EventManager():
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
        
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier():
    def __init__(self):
        print("Arranging hotel for marriage...")

    def isAvailable(self):
        print("Is the hotel free for the event on the given day?")
        return True

    def bookHotel(self):
        print("Registered the booking!\n")
    
class Florist():
    def __init__(self):
        print("Flower decorations for the event...")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for decorations!\n")

class Caterer():
    def __init__(self):
        print("Food arrangements for the event...")

    def setCuisine(self):
        print("Chinese and Continental cuisine to be served!\n")

class Musician():
    def __init__(self):
        print("Musical arrangements for the marriage...")

    def setMusicType(self):
        print("Jazz and Classical will be played!\n")

class You():
    def __init__(self):
        print("You:: Whoa! Marriage arrangements?")

    def askEventManager(self):
        print("You:: Lets contact the Event Manager")

        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to the Event Manager, all preparations are done! Phew!")

you = You()
you.askEventManager(    )
    
