from abc import ABCMeta, abstractmethod

class Section(metaclass = ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal section")

class AlbumSection(Section):
    def describe(self):
        print("Album section")

class PatentSection(Section):
    def describe(self):
        print("Patent section")

class PublicationSection(Section):
    def describe(self):
        print("Publication section")

class Profile(metaclass = ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())

if __name__ == '__main__':
    profile_type = input("Which profile would you like to create? [Linkedin or Facebook] ")
    profile = eval(profile_type.lower())()
    print("Creating the ", type(profile).__name__, " profile")
    print("Profile has sections --", profile.getSections())