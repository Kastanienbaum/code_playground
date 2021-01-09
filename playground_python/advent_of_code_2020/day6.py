#!/usr/bin/python3 

# part 1: 
# What is the sum of those counts? 
# answer: 6633 

with open('day6_input.txt', 'r') as f: 
    yes = []
    total = 0
    persons = 0
    
    # read line, add new chars to list (no duplicates) 
    for line in f:
        if line == '\n':
            total += len(yes)
            yes = []
            persons = 0
        else: 
            tmp = list(line.split('\n')[0])
            persons = len(tmp)
            for x in tmp:
                if x not in yes:
                    yes.append(x)

    # take last entry into account
    total += len(yes)
    print(total)

    # part 2: Count the number of questions to which everyone answered "yes". 
    # What is the sum of those counts?


# EOF 

