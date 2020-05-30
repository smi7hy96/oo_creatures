class Cockroach:
    def __init__(self, size, colour, wings, species, status):
        self.size = size
        self.colour = colour
        self.wings = wings
        self.species = species
        self.status = status

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
                self.status = 'Dead'
                return 'WE GOT IT'

    def jump(self, no_times):
        jumping = ''
        for i in range(no_times):
            jumping += '*boing* '

        return jumping.strip()

    def reproduce(self):
        return Cockroach((self.size//2)+1, self.colour, self.wings, self.species, 'Alive')
