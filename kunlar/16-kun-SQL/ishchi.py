class Ishchi:
    def __init__(self, ism, familiya, sharif, yosh):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.yosh = yosh

    def fish(self):
        print("{} {} {}, {} yoshda".format(self.familiya, self.ism, self.sharif, self.yosh))