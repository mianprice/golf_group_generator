import random

def factorial(n):
    f = 1
    for i in xrange(1,n+1):
        f *= i
    return f

def variance(num_set):
    v = 0
    m = mean(num_set)
    for i in num_set:
        v += ((i - m)**2)
    return v

def median(num_set):
    i = len(num_set)
    if i % 2 == 0:
        m = (num_set[(i/2)-1] + num_set[i/2])/2
    else:
        i = len(num_set) - 1
        m = num_set[i]
    return m

class Golfer(object):
    def __init__(self,(name,handicap)):
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
'''
print "Do you have a maximum number of groups?\nEnter the maximum, or 0 for no maximum."
max_groups = int(raw_input("#: "))
'''
max_groups = 0

names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]

golfer_list_base = []
handicap_list = []

for i in names:
    handicap = random.randint(1,20)
    handicap_list.append(handicap)
    golfer_list_base.append(Golfer((i,handicap)))

handicap_list = sorted(handicap_list)
median_handicap = median(handicap_list)
print median_handicap

handicap_minus = {}
handicap_plus = {}

for i in golfer_list_base:
    if i.get_handicap() < median_handicap:
        handicap_minus[i.get_name()] = i.get_handicap()
    else:
        handicap_plus[i.get_name()] = i.get_handicap()

sorted_minus = sorted(handicap_minus.items(), key = lambda (k,v): v)
print sorted_minus

sorted_plus = sorted(handicap_plus.items(), key = lambda (k,v): v)
print sorted_plus
exit(0)

'''
Print Golfer List
for i in golfer_list_base:
    i.print_self()
'''
if max_groups < 1:
    max_groups = 1000000

num_golfers = 0
if len(golfer_list_base) % 4 == 0:
    if len(golfer_list_base) / 4 > max_groups:
        print "Unfortunately, there are too many golfers to play in foursomes with your maximum number of groups."
    else:
        num_golfers = 4
        group_list = GroupList(len(golfer_list_base)/4)
elif len(golfer_list_base) % 3 == 0:
    if len(golfer_list_base) / 3 > max_groups:
        print "Unfortunately, there are too many golfers to play in threesomes with your maximum number of groups."
    else:
        num_golfers = 3
        group_list = GroupList(len(golfer_list_base)/3)

if num_golfers == 0:
    print "Sorry, you'll need to change the number of golfers enteres and restart the program."
else:
    ideal_golfer_list = golfer_list_base
    ideal_list_variance = variance(golfer_list_base)



    for i in xrange(len(ideal_golfer_list)+1):
        if i == 0:
            next_group = []
        if len(next_group) < num_golfers:
            next_group.append(ideal_golfer_list[i])
        else:
            if i < len(ideal_golfer_list):
                group_list.add(Group(next_group))
                next_group = []
                next_group.append(ideal_golfer_list[i])
            else:
                group_list.add(Group(next_group))

    '''
    Print Group List
    group_list.print_self()
    '''
