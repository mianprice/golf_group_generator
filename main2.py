import random
import copy

def mean(num_set):
    m = 0.0
    for i in num_set:
        m += i
    return m/len(num_set)

def variance(num_set):
    v = 0.0
    m = mean(num_set)
    for i in num_set:
        v += ((i - m)**2)
    return v

def group_handicap(g):
    h = 0
    for i in g:
        h += i[1]
    return h

def team_variance(groups):
    s = []
    for i in groups:
        s.append(group_handicap(i))
    return variance(s)

def swap(x,y):
    global groups
    test = copy.deepcopy(groups)
    test[x[0]][x[1]] = groups[y[0]][y[1]]
    test[y[0]][y[1]] = groups[x[0]][x[1]]
    j = team_variance(test)
    k = team_variance(groups)
    if team_variance(test) < team_variance(groups):
        groups = test
        return True
    else:
        return False

testdata = [
("Mitzel",7),
("Hollenstein",10),
("Seese",13),
("Hajduk",12),
("Gallagher",8),
("Lake",9),
("Klimko",14),
("Singer",12),
("Crane",7),
("Lavinsky",9),
("Holmes",12),
("Stewart",15)
]

random.shuffle(testdata)

groups = [[("",0)]*4 for i in xrange(len(testdata)/4)]
for i in xrange(4):
    for j in xrange(len(testdata)/4):
        groups[j][i] = testdata[i+(j*4)]
'''
print team_variance(groups)
for i in groups:
    print i

print "\n\n\n"
'''
swap_count = 0
try_count = 0
try_records = []
total_tries = 0
tries_per_swap = []
while try_count < 50:
    if team_variance(groups) == 0:
        break
    x1 = random.randint(0,2)
    x2 = random.randint(0,3)
    y1 = random.randint(0,2)
    y2 = random.randint(0,3)
    x = (x1,x2)
    y = (y1,y2)
    coord_check = (x,y)
    if (coord_check not in try_records) and x1 != y1:
        if swap(x,y):
            tries_per_swap.append(len(try_records))
            try_records = []
            total_tries += try_count
            try_count = 0
            swap_count += 1
        else:
            try_records.append(coord_check)
            try_count += 1
total_tries += try_count
tries_per_swap.append(len(try_records))
'''
print swap_count
print try_count
print team_variance(groups)
'''
for i in groups:
    string = "\nTeam Handicap: %0.3f\nTeam members: " % group_handicap(i)
    for j in xrange(len(i)):
        string += i[j][0]
        if j != (len(i) - 1):
            string += ", "
    string += "\n\n"
    print string

string_tries = ""
for i in xrange(len(tries_per_swap)):
    string_tries += "Swap: %d || Tries: %d\n" % (i+1, tries_per_swap[i])

analysisString = "Total Tries: %d\nTotal Swaps: %d\n" % (total_tries, swap_count)
print analysisString + string_tries
