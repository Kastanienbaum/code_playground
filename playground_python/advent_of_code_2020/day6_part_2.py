#!/usr/bin/python3 

# part 2: Count the number of questions to which everyone answered "common_yes". 
# What is the sum of those counts?

with open('day6_input.txt', 'r') as f: 
    common_yes = []
    total = 0
    answers = []
    sum_of_common_yes = 0
    
    # read line, add list to list 
    for line in f:
        if line == '\n':
            print(answers)
            # analyse lists for common element
            persons_in_group = len(answers)
            for _list in answers:
                common_yes = set(_list).intersection(iter(answers).next())
            print(common_yes)
            print(len(common_yes))
            sum_of_common_yes += len(common_yes)

            # reset list
            answers = []
            common_yes = []
        else: 
            # add string to list
            tmp = list(line.split('\n')[0])
            answers.append(tmp)

    # take last entry into account
    #sum_of_common_yes += len(common_yes)

    # 3275 is WRONG (too high)
    print(sum_of_common_yes)


# EOF 

