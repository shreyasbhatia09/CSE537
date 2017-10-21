# do not modify the function names
# You are given L and M as input
# Each of your functions should return the minimum possible L value alongside the marker positions
# Or return -1,[] if no solution exists for the given L

# Your backtracking function implementation

from collections import defaultdict
import timeit
import copy
import time

infinity = 99999999999999

def check_constraints(list):
    """
        check wether the list satisfies the
        Golumb Ruler constraints
    """
    if len(list) != len(set(list)):
        return []
    # Create a dictionary of difference between every i and j
    diff = defaultdict(int)
    diff_list = [abs(i - j) for i in list for j in list if i != j]
    for i in diff_list:
        diff[i] += 1
        if diff[i] > 2:
            return False
    # if constraints are passed return true
    return True


def list_init(a, M):
    """
       Return a list with
       M infinity values
       if the length of the list is 0
    """
    if len(a) == 0:
        return [infinity] * M
    else:
        return a


def backtracking_helper(list, index, L, M, checks):

    """
        Helper module for backtracking.
        This utility function performs the
        necesssary recursion
    """

    # Check base case
    if index > L + 1:
        return [], checks

    # check constraints as you go
    if not check_constraints(list):
        return [], checks

    # if we found a list with size M check its validity and return accordingly
    if len(list) == M:
        if check_constraints(list):
            return list, checks

        else:
            return [], checks

    # This will store the list with the smallest L
    optimal_soln = list_init([], M)
    # Recur for all values
    # Recur for all values in the domain
    checks += 1
    checks_temp=0
    for i in range(0, L+1):
        if (i==index):
            continue
        list.append(i)
        resList, checks_temp = backtracking_helper(list, i + 1, L, M,0)
        checks = checks + checks_temp
        res = copy.deepcopy(resList)
        # Backtrack
        list.remove(i)
        # Compare result to find optimal solution
        res = list_init(res, M)
        res.sort()
        if res[M - 1] < optimal_soln[M - 1]:
            optimal_soln = res

    return optimal_soln, checks


def BT(L, M):
    "*** YOUR CODE HERE ***"
    res = []
    res, checks = backtracking_helper([0], 1, L, M, 0)
    if res[0] == 99999999999999:
        return -1, []
    else:
        print checks
        return res[M-1], res


def forward_check(index, L, list):
    """
        Returns a list of allowed values
        with respect to the golumb ruler constraints
    """

    def list_diff(A, B):
        return [val for val in A if val not in set(B)]

    diff = defaultdict(int)
    diff_list = [abs(i - j) for i in list for j in list if i != j]
    for i in diff_list:
        diff[i] += 1

    not_allowed_values = [i for i in diff if diff[i] > 2]
    allowed_values = range(index, L+1)

    return list_diff(allowed_values, not_allowed_values)


def forward_checking_helper(list, index, L, M, checks):
    """
        Helper module for backtracking with Forward checking.
        This utility function performs the
        necesssary recursion
    """

    # Check base case
    if index > L + 1:
        return [],checks

    # check constraints as you go
    if not check_constraints(list):
        return [],checks

    # if we found a list with size M check its validity and return accordingly
    if len(list) == M:
        if check_constraints(list):
            return list, checks
        else:
            return [],checks

    # Create a new domain by removing values
    # which do not satisfy the constraint
    forward_check_values = forward_check(index, L, list)

    # Recur for all values which satisfy the constraint
    optimal_soln = list_init([], M)
    checks += 1
    checks_temp = 0
    for i in forward_check_values:
        # Append to the list and recur
        list.append(i)
        resList ,checks_temp = forward_checking_helper(list, i + 1, L, M, 0)
        checks = checks + checks_temp
        res1 = copy.deepcopy(resList)
        # Remove from the list for backtracking
        list.remove(i)
        # Compare result for optimal solution
        res1 = list_init(res1,M)
        res1.sort()
        if res1[M-1] < optimal_soln[M-1]:
            optimal_soln = res1
    return optimal_soln, checks


# Your backtracking+Forward checking function implementation
def FC(L, M):
    res = []
    res, checks = forward_checking_helper([0], 1, L, M, 0)
    # solution not found
    if res[0] == 99999999999999:
        return -1, []
    else:
        print checks
        return res[M-1], res



# Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1, []


# M = 8
# L = 35
# start_time = time.time()
# flist = BT(L, M)
# end_time = time.time()
# print flist, (end_time-start_time)
#
# start_time = time.time()
# flist2 = FC(L, M)
# end_time = time.time()
# print flist2, (end_time-start_time)