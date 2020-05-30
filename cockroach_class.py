class Cockroach:
    def __init__(self, size, colour, wings, species, status):
        self.size = size
        self.colour = colour
        self.wings = wings
        self.species = species

    def fly(self):
        if self.size > 3:
            return 'RUN AWAY FROM IT!'
        else:
            return 'SOMEONE SWAT IT!'
