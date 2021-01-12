'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):

    ### Input Check

    if not isinstance(A,list):
        raise TypeError('Input 2 must be an array')

    ### Method

    A = list(set(A))
    A.sort()
    
    count = 1

    for num in A:
        if num > 0:
            if num != count:
                break
            count += 1

    if count == A[-1]: 
        count += 1

    return count

print(solution([1,3,6,4,1,2]))