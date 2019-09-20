
# Problem Statement:
# Given an array of integers which consists of 0's followed by non-zeroes entries,
# find number of zeroes in that array.

# example:
# Input: [0,0,0,0,9,10,6,4,2]
# Output: 4
# Input: [0,0,23,13,11,4,7]
# Output: 2

# --------------------------------------------------------------------------------------------------------------------

# imports
import sys
from random import randrange


def create_list(n):
    in_list = [0] * n
    for i in range(int(n/3),n):
        # https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
        in_list[i] = randrange(1,100)
    return in_list


# 1. Naive approach
# compare element with 0, if True increment count otherwise we have encountered non-zero value, stop and return count
def count_zeroes_naive(in_list):
    count = 0
    for i in range(len(in_list)):
        if in_list[i] == 0:
            # https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
            count +=1
        else:
            break  # encountered non-zero value, stop here
    return count


# 2. Divide and Prune
# rather than comparing each element with 0 till non-zero value comes, do this
# Step1. Divide - divide the list in half
# Step2. Prune  - if list[mid] = 0
#                    prune right half of the list
#                 else
#                    prune left half of the list

# remove from here and add to Quick Sort later
# https://stackoverflow.com/questions/20917617/whats-the-difference-of-dual-pivot-quick-sort-and-quick-sort
def count_zeroes_divide_n_prune(in_list):
    low  = mid = 0
    hi   = len(in_list)
    while(hi - low > 1):
        # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html # prevent overflow
        # https://www.python.org/dev/peps/pep-0238/
        mid = low + (hi - low)//2
        if in_list[mid] == 0:
            low = mid      # prune right, move low to mid
        else:
            hi = mid - 1   # prune left, move hi to (mid-1)
    if in_list[hi] == 0:
        return hi + 1
    else:
        return low + 1


# start from here
if __name__ == "__main__":
    in_list = create_list(int(sys.argv[1]))  # argv are of string type, typecast to int
    print ("List : {}".format(in_list))

    zero_count1 = count_zeroes_naive(in_list)
    print("Naive : {}".format(zero_count1))

    zero_count2 = count_zeroes_divide_n_prune(in_list)
    print("Divide N Prune : {}".format(zero_count2))