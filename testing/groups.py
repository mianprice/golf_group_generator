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

def swap(x,y,g):
    test = copy.deepcopy(g)
    test[x[0]][x[1]] = g[y[0]][y[1]]
    test[y[0]][y[1]] = g[x[0]][x[1]]
    j = team_variance(test)
    k = team_variance(g)
    if team_variance(test) < team_variance(g):
        g = test
        return (True,g)
    else:
        return (False,g)

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
# g_input = '123456,3:987654,17:3456,8:9876,7:4567,7:987643,14:23457857,2:0327403270,10:81739179,15:2163812763,3:8312963,6:028193710,8:382179,14:381721987,14:32890179,16:3278917,9'
parsed_input = input_parse(g_input)


parsed_input = sorted(parsed_input, key=lambda x:x[1])
l_parsed = len(parsed_input)
g_parsed = l_parsed/4
test_groups = []
groups = [[("",0)]*4 for i in xrange(l_parsed/4)]
for i in xrange(l_parsed):
    group_counter = i % (g_parsed)
    index_counter = i / (g_parsed)
    if index_counter % 2 == 1:
        rev = True
    else:
        rev = False
    if rev:
        groups[g_parsed - 1 - group_counter][index_counter] = parsed_input[i]
    else:
        groups[group_counter][index_counter] = parsed_input[i]
test_groups.append(groups)

random.shuffle(parsed_input)
groups = [[("",0)]*4 for i in xrange(l_parsed/4)]
for i in xrange(l_parsed):
    group_counter = i % (g_parsed)
    index_counter = i / (g_parsed)
    if index_counter % 2 == 1:
        rev = True
    else:
        rev = False
    if rev:
        groups[g_parsed - 1 - group_counter][index_counter] = parsed_input[i]
    else:
        groups[group_counter][index_counter] = parsed_input[i]
test_groups.append(groups)


exit_string = ""
for group in test_groups:
    swap_count = 0
    loop_count = 0
    try_count = 0
    try_records = []
    total_tries = 0
    tries_per_swap = []
    loops_per_swap = []
    num_groups = len(group)
    num_members = len(group[0])
    max_loops = num_groups * num_members * ()
    total_loops = 0
    while try_count < 100 and loop_count < 1000:
        if team_variance(group) == 0:
            break
        x1 = random.randint(0,num_groups - 1)
        x2 = random.randint(0,num_members - 1)
        y1 = random.randint(0,num_groups - 1)
        y2 = random.randint(0,num_members - 1)
        x = (x1,x2)
        y = (y1,y2)
        coord_check1 = (x,y)
        if (coord_check1 not in try_records) and x1 != y1 and group[x[0]][x[1]] != group[y[0]][y[1]]:
            s,new_group = swap(x,y,group)
            if s:
                group = new_group
                tries_per_swap.append(try_count)
                loops_per_swap.append(loop_count)
                try_records = []
                total_tries += try_count
                try_count = 0
                swap_count += 1
                total_loops += loop_count
                loop_count = 0
            else:
                try_records.append(coord_check1)
                try_count += 1
                loop_count += 1
        else:
            try_records.append(coord_check1)
            loop_count += 1

    total_loops += loop_count
    total_tries += try_count
    tries_per_swap.append(try_count)
    loops_per_swap.append(loop_count)

    # PRINT STRING OUTPUT  (FOR PRINTING TO STANDARD OUTPUT)
    group_strings = ""
    for i in group:
        string = "\nTeam Handicap: %.0f\nTeam members: " % group_handicap(i)
        for j in xrange(len(i)):
            string += i[j][0]
            if j != (len(i) - 1):
                string += ", "
        string += "\n\n"
        group_strings += string
    print group_strings

    string_tries = ""
    for i in xrange(len(tries_per_swap)):
        string_tries += "Swap: %d || Tries: %d || Loops: %d\n" % (i+1, tries_per_swap[i], loops_per_swap[i])

    analysisString = "Total Loops: %d\nTotal Tries: %d\nTotal Swaps: %d\n" % (total_loops,total_tries, swap_count)
    print analysisString + string_tries

    exit_string += group_strings + analysisString + string_tries + "\n"

sys.exit(exit_string)

# Print output for PHP to handle
#
# output_string = ""
# for i in xrange(len(groups)):
#     if i != 0:
#         output_string += ":"
#     for j in xrange(len(groups[i])):
#         output_string += groups[i][j][0]
#         if j != len(groups[i]) - 1:
#             output_string += ","
#
# sys.exit(output_string)
