# Leetcode: https://leetcode.com/articles/find-the-duplicate-number/

# Problem Statement:
# Given an array containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.

# thought to better understand the problem:
# 1. Since the integer can range from 1 to n(inclusive) but there are n+1 integers in total, its guaranteed that
# there is at-least 1 duplicate.

# example: if n = 4, we will have 5 integers in total and integer can range from 1 to 4
# Input: [1,3,4,2,2] , n = 4
# Output: 2
# Input: [3,1,3,4,2] , n = 4
# Output: 3

# --------------------------------------------------------------------------------------------------------------------
# imports
import sys




def create_list_with_duplicate(n):
    list_with_duplicate = []
    for i in range(1,n+1):             # loop will run from 1 to n
        list_with_duplicate.append(i)
    list_with_duplicate.append(n)      # append one more element to make n+1
    return list_with_duplicate


# 1. Naive approach
# take one element and compare it with the rest of the elements
#
def find_duplicate_naive(list_with_duplicate):
    for i in range((len(list_with_duplicate))-1):    # loop will run upto second last index
        for j in range(i+1, len(list_with_duplicate)):  # loop will run upto last index
            if list_with_duplicate[i] == list_with_duplicate[j]:
                return list_with_duplicate[i]
    return -1


# 2. Sort then scan
# by sorting, repeating element will by side by side ~ only neighboring elements need to be compared
# Info: sort() internally uses Quick Sort
#
def find_duplicate_sort_n_scan(list_with_duplicate):
    # https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
    lst = list_with_duplicate.copy()
    lst.sort()
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            return lst[i]
    return -1


# 3. Indexed list
# create a separate list where each index represent each element of the original list,
# initialize with value 0, when an element is seen --> sets its index value to 1.
# If already 1, it means it was visited earlier --> its duplicate. YEY !!

def find_duplicate_indexed_list(list_with_duplicate):
    length = len(list_with_duplicate)
    # https://stackoverflow.com/questions/8528178/list-of-zeros-in-python
    indexed_list = [0]* length
    for i in range(len(list_with_duplicate)):
        if indexed_list[list_with_duplicate[i]] == 1:
            return list_with_duplicate[i]
        indexed_list[list_with_duplicate[i]] = 1
    return -1



# 4. Negation Trick
# Take index, then value at that index, then go to "index at that value" and set it to -ve.
# if we see -ve index at that value", index is repeated.

def find_duplicate_negation_trick(list_with_duplicate):
    for i in range(len(list_with_duplicate)):
        element = abs(list_with_duplicate[i])
        if list_with_duplicate[element] < 0:
            return element
        list_with_duplicate[element] *= -1
    return -1


# start from here
if __name__ == "__main__":
    list_with_duplicate = create_list_with_duplicate(int(sys.argv[1]))  # argv are of string type, typecast to int
    print("n : {}  length of the list : {}".format(sys.argv[1],len(list_with_duplicate)))
    print("list: {}".format(list_with_duplicate))

    duplicate1 = find_duplicate_naive(list_with_duplicate)
    print("Naive : {}".format(duplicate1))

    duplicate2 = find_duplicate_sort_n_scan(list_with_duplicate)
    print("Sort n Scan : {}".format(duplicate2))

    duplicate3 = find_duplicate_indexed_list(list_with_duplicate)
    print("Indexed List : {}".format(duplicate3))

    duplicate4 = find_duplicate_indexed_list(list_with_duplicate)
    print("Negation Trick : {}".format(duplicate4))
