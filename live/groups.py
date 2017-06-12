import random
import copy
import sys

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

def input_parse(s):
    s_list = list(s)
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    numbers = "0123456789"
    pointer = ""
    next_id = ""
    next_hcp = ""
    parsed = []
    id_found = False
    while len(s_list) > 0:
        next_char = s_list.pop(0)
        if next_char == ",":
            id_found = True
        elif next_char == ":":
            next_tuple = (next_id,int(next_hcp))
            parsed.append(next_tuple)
            next_hcp = ""
            next_id = ""
            id_found = False
        elif next_char in letters:
            next_id += next_char
        elif next_char in numbers:
            if id_found:
                next_hcp += next_char
            else:
                next_id += next_char
    next_tuple = (next_id,int(next_hcp))
    parsed.append(next_tuple)
    return parsed

g_input = sys.argv[1]
parsed_input = input_parse(g_input)

groups = [[("",0)]*4 for i in xrange(len(parsed_input)/4)]
for i in xrange(4):
    for j in xrange(len(parsed_input)/4):
        groups[j][i] = parsed_input[i+(j*4)]

input_groups = groups

loop_count = 0
swap_count = 0
try_count = 0
try_records = []
total_tries = 0
tries_per_swap = []
num_groups = len(groups)
num_members = len(groups[0])
while try_count < 50 and loop_count<32000:
    if team_variance(groups) == 0:
        break
    loop_count += 1
    x1 = random.randint(0,num_groups - 1)
    x2 = random.randint(0,num_members - 1)
    y1 = random.randint(0,num_groups - 1)
    y2 = random.randint(0,num_members - 1)
    x = (x1,x2)
    y = (y1,y2)
    coord_check = (x,y)
    if (coord_check not in try_records) and x1 != y1 and groups[x[0]][x[1]] != groups[y[0]][y[1]] and not (groups[x[0]][x[1]] > groups[y[0]][y[1]]  and group_handicap(groups[x[0]]) < group_handicap(groups[y[0]])):
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

output_string = ""
for i in xrange(len(groups)):
    if i != 0:
        output_string += ":"
    for j in xrange(len(groups[i])):
        output_string += groups[i][j][0]
        if j != len(groups[i]) - 1:
            output_string += ","

sys.exit(output_string)
