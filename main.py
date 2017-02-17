import random

class Golfer(object):
    def __init__(self,name,handicap):
        self.name = name
        self.handicap = handicap

    def print_self(self):
        print "Golfer: %s || Handicap: %s" % (self.name, self.handicap)

    def get_handicap(self):
        return self.handicap

    def get_name(self):
        return self.name

class Group(object):
    def __init__(self,players):
        self.players = players
        self.group_handicap()
        self.set_printer()

    def group_handicap(self):
        self.group_handicap = 0
        for i in self.players:
            self.group_handicap += i.get_handicap()

    def set_printer(self):
        string = "Golfers: "
        for i in xrange(len(self.players)):
            if i < len(self.players) - 1:
                string += self.players[i].get_name() + ", "
            else:
                string += self.players[i].get_name() + " || "
        string += "Group Handicap: " + str(self.group_handicap)
        self.printer = string

    def get_printer(self):
        return self.printer

    def print_self(self):
        print self.printer



class GroupList(object):
    def __init__(self,maximum):
        self.groups = []
        self.maximum = maximum
        self.printer = ""

    def add(self,group):
        self.groups.append(group)
        self.set_printer()

    def set_printer(self):
        string = "GROUPLIST\n=========\n"
        for i in xrange(len(self.groups)):
            string += "Group %d\n=======\n" % (i+1)
            string += self.groups[i].get_printer() + "\n\n"
        self.printer = string

    def print_self(self):
        print self.printer




names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

golfer_list = []

for i in names:
    handicap = random.randint(1,20)
    golfer_list.append(Golfer(i,handicap))

'''
Print Golfer List (Use to check the golfer_list generation)
for i in golfer_list:
    i.print_self()
'''

group_list = GroupList(4)

for i in xrange(len(golfer_list)+1):
    if i == 0:
        next_group = []
    if len(next_group) < 4:
        next_group.append(golfer_list[i])
    else:
        if i < len(golfer_list):
            group_list.add(Group(next_group))
            next_group = []
            next_group.append(golfer_list[i])
        else:
            group_list.add(Group(next_group))

group_list.print_self()
