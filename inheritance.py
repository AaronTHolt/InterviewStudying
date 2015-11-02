

class Pet(object):

    def __init__(self, name=None, kind=None):
        self.name = name
        self.kind = kind

    def getName(self):
        return self.name

    def getKind(self):
        return self.kind

    def __str__(self):
        return "{name} is a {kind}".format(name=self.name, kind=self.kind)


class Dog(Pet):

    def __init__(self, name=None, barks=None, stray=None):
        Pet.__init__(self, name, "Dog")
        self.barks = barks
        self.stray = stray

    def getBarks(self):
        return self.barks

    def getStray(self):
        return self.stray

    def __str__(self):
        return """{name} is a {kind} who {barks} 
and {stray} a stray""".format(
                name=self.name, kind=self.kind, 
                barks=self.barks, stray=self.stray)


aa = Dog('Clifford', 'barks', 'is')
print aa
print aa.getName()