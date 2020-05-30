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

    def squish(self, chance):
        if self.size > 3:
            return 'how did it not die'
        else:
            if chance == 0:
                return 'quick little bugger'
            else:
                return 'WE GOT IT'

    def jump(self, no_times):
        jumping = ''
        for i in range(no_times):
            jumping += '*boing* '

        return jumping.strip()
