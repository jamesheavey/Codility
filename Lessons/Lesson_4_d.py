'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''

def solution(A):

    ### Input Check

    if not isinstance(A,list):
        raise TypeError('Input 2 must be an array')

    ### Method 1

    if len(A) != len(set(A)) or len(A) < 1:
        return 0

    A.sort()

    for idx,val in enumerate(A):
        if idx + 1 != val:
            return 0

    return 1

    ### Method 2

    # counter = [0]*len(A)

    # for element in A:

    #     if not 1 <= element <= len(A):
    #         return 0

    #     else:
    #         if counter[element-1] != 0:
    #             return 0

    #         else:
    #             counter[element-1] = 1

    # return 1

print(solution([4,1,3,2]))