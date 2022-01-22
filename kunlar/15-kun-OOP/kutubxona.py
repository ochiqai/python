class Calculator():

    def __init__(self):
        print("Kalkulyator yaratildi")
        self.x = 0
        self.y = 0

    def qushish(self, x, y):
        self.x = x
        self.y = y
        natija = self.x + self.y
        return natija