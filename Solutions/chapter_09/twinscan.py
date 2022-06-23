
class Twinscan:

    NUMBER_OF_CHUCKS = 2

    def __init__(self, id, configuration):
        self.id = id
        self.configuration = configuration
        self.power = False
        self.chucks = ['A', 'B']

    def on(self):
        self.power = True

    def off(self):
        self.power = False

    def expose(self):
        print(f'{self.chucks[0]} is being exposed')

    def measure(self):
        print(f'{self.chucks[1]} is being measured')

    def swap(self):
        self.chucks.reverse()

    def info(self):
        print(f'Chuck {self.chucks[0]} is on expose side and chuck {self.chucks[1]} is on measure side')


twinscan = Twinscan('TS124', '1970')

if __name__ == '__main__':

    machine = Twinscan('TS123', '1970')
    machine.info()

    machine.swap()
    machine.info()

    machine.expose()
    machine.measure()
