class car(object):
    def __init__(self, make, model, year, condition, kms):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showall):
        if showall:
            print('This car is a %s %s from %s,it is %s and has %s kms.'
                  % (self.make, self.model, self.year, self.condition, self.kms))
        else:
            print('This car is %s %s from %s' % (self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2012, 'New', 0)
whip.display(True)

