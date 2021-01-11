'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

def solution(A):
    
    ### Input Check

    if not isinstance(A,list):
        raise TypeError("Input must be an array")

    if len(A) != len(set(A)):
        raise ValueError("All array elements must be distinct")

    ### Method 1

    if len(A) == 0:
        return 1

    n = len(A)+1
    consecutive_sum = n * (n + 1)//2

    return consecutive_sum - sum(A)

    ### Method 2

    # missing_element = len(A)+1
     
    # for idx,value in enumerate(A):
    #     missing_element = missing_element ^ value ^ (idx+1)
         
    # return missing_element

print(solution([1,2,3,4,5,6,7,8,9,10,11,13]))