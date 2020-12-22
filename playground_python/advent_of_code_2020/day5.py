#!/usr/bin/python3 

# part 1: 
# What is the highest seat ID on a boarding pass? 
# solution: 818 

def get_seat_ID(num): 
    return ((num & 0x3F8) >> 3) * 8 + (num & 0x007)


def yield_boarding_passes(file):
    with open(file, 'r') as f: 
        for line in f:
            retval = line.split('\n')
            yield retval[0]

def decode_char(c):
    switcher = {'F': 0, 
                'B': 1, 
                'L': 0, 
                'R': 1
                }
    return switcher.get(c, 'invalid')


def main():

    highest_seat_ID = 0
    IDs = []

    for boarding_pass in yield_boarding_passes('day5_input.txt'):
        # replace letters with 0s and 1s 
        bin_pass = 0x000
        for x in range(len(boarding_pass)):
            tmp = list(boarding_pass)
            bin_pass |= (decode_char(tmp[x]) << (len(boarding_pass) - x - 1))

        tmp = get_seat_ID(bin_pass)
        #print(bin_pass)
        IDs.append(tmp) # for part 2
        if tmp > highest_seat_ID:
            highest_seat_ID = tmp

    print('highest ID: %d' %highest_seat_ID)

    # part 2 
    IDs.sort()

    for i, ID in enumerate(IDs):
        # TODO: catch error at end of list (index out of range)
        if ID+2 == IDs[i+1]:
            print(ID)


if __name__ == '__main__':
    main()

# EOF 

