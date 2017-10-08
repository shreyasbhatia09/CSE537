# do not modify the function names
# You are given L and M as input
# Each of your functions should return the minimum possible L value alongside the marker positions
# Or return -1,[] if no solution exists for the given L

# Your backtracking function implementation

import copy
from collections import defaultdict

infinity = 99999999999999


def check_constraints(list):
    diff = defaultdict(int)
    diff_list = [abs(i - j) for i in list for j in list if i != j]
    for i in diff_list:
        diff[i] += 1
        if diff[i] == 3:
            return False
    return True


def listinit(a, M):
    if len(a) == 0:
        return [infinity] * M
    else:
        return a


def backtracking_helper(list, index, L, M):
    # Check base case
    if index > L + 1:
        return []

    if len(list) == M:
        if check_constraints(list):
            return list
        else:
            return []

    # Add current number
    list.append(index)
    res1 = copy.deepcopy(backtracking_helper(list, index + 1, L, M))

    # Backtrack and find another solution
    list.remove(index)

    # increase current index
    res2 = copy.deepcopy(backtracking_helper(list, index + 1, L, M))

    # Initialize if null
    res1 = listinit(res1, M)
    res2 = listinit(res2, M)

    if res1[M - 1] > res2[M - 1]:
        return res2
    else:
        return res1


def BT(L, M):
    "*** YOUR CODE HERE ***"
    res = []
    res_list = backtracking_helper([], 0, L, M)
    if len(res_list) == 0:
        res = -1
    else: return 1
    return res, res_list

# Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    return -1, []


# Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1, []


flist = backtracking_helper([], 0, 7, 4)
print flist
