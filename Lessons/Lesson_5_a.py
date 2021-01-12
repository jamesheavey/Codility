'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''

def solution(A, B, K):

    ### Input Check

    if not isinstance(A,int) or not isinstance(B,int) or not isinstance(K,int):
        raise TypeError('One or more Inputs not integers')

    if B < A:
        raise ValueError('Input 1 must be greater than or equal to Input 2')

    ### Method

    while B % K != 0: B -= 1

    while A % K != 0: A += 1

    return (B//K) - (A//K) +1


print(solution(1,10,5))