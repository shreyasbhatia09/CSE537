# do not modify the function names
# You are given L and M as input
# Each of your functions should return the minimum possible L value alongside the marker positions
# Or return -1,[] if no solution exists for the given L

# Your backtracking function implementation

from collections import defaultdict
import copy
infinity = 99999999999999


def check_constraints(list):
    diff = defaultdict(int)
    diff_list = [abs(i - j) for i in list for j in list if i != j]
    for i in diff_list:
        diff[i] += 1
        if diff[i] == 3:
            return False
    return True


def list_init(a, M):
    if len(a) == 0:
        return [infinity] * M
    else:
        return a


def backtracking_helper(list, index, L, M):

    # Check base case
    if index > L + 1:
        return []

    # check constraints as you go
    if not check_constraints(list):
        return []

    # if we found a list with size M check its validity and return accordingly
    if len(list) == M:
        if check_constraints(list):
            return list
        else:
            return []

    # This will store the list with the smallest L
    max_res = []

    # Recur for all values
    for i in range(index, L+1):
        list.append(i)
        res = copy.deepcopy(backtracking_helper(list, i + 1, L, M))
        # the most important backtracking step.
        list.remove(i)
        res = copy.deepcopy(list_init(res, M))
        max_res = copy.deepcopy(list_init(max_res, M))
        if res[M-1] < max_res[M-1]:
            max_res = copy.deepcopy(res)
    return max_res


def BT(L, M):
    "*** YOUR CODE HERE ***"
    res = []
    res = backtracking_helper([], 0, L, M)
    if res[0] == 99999999999999:
        return -1, []
    else:
        return res[M-1], res

def forward_check( val, list):
    forward_list = copy.deepcopy(list)
    forward_list.append(val)
    return check_constraints(forward_list)

def forward_checking_helper(list, index, L, M):

    # Check base case
    if index > L + 1:
        return []

    # check constraints as you go
    if not check_constraints(list):
        return []

    # if we found a list with size M check its validity and return accordingly
    if len(list) == M:
        if check_constraints(list):
            return list
        else:
            return []

    # This will store the list with the smallest L
    max_res = []

    # Recur for all values
    for i in range(index, L+1):

        # Forward Checking
        if not forward_check(i,list):
            continue

        list.append(i)

        res = copy.deepcopy(backtracking_helper(list, i + 1, L, M))
        # the most important backtracking step.
        list.remove(i)
        res = copy.deepcopy(list_init(res, M))
        max_res = copy.deepcopy(list_init(max_res, M))
        if res[M-1] < max_res[M-1]:
            max_res = copy.deepcopy(res)

    return max_res

# Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    res = []
    res = forward_checking_helper([], 0, L, M)
    # solution not found
    if res[0] == 99999999999999:
        return -1, []
    else:
        return res[M-1], res


# Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1, []


flist = backtracking_helper([], 0, 25, 7)
print flist
flist2 = forward_checking_helper([], 0, 25, 7)
print flist2
