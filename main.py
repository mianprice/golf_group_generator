import random

class Golfer(object):
    def __init__(self,name,handicap):
        self.name = name
        self.handicap = handicap

    def print_self(self):
        print "Golfer: %s || Handicap: %s" % (self.name, self.handicap)

names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

golfer_list = []

for i in names:
    handicap = random.randint(1,20)
    golfer_list.append(Golfer(i,handicap))

for i in golfer_list:
    i.print_self()
