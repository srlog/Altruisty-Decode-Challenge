"""Q3
You are given an array, and you need to choose a contiguous subarray of length ‘k’. For each subarray, find the maximum element and return the minimum of those maximums."""

k = int(input())
n = int(input())
array = list()
for i in range(n):
    array.append(int(input())) # Reading array

subarray = list()
for i in range(n):
    if i + k <= n:
        subarray.append(array[i : i+k]) # Creating all subarrays with length k

print()
print(min(map(max, subarray)))  # Finding the maximum of each subarray and the overall minimum



"""Explanation: 
The subarrays of size ( k = 2 ) are:
[3, 1] with maximum 3
[1, 4] with maximum 4
[4, 1] with maximum 4
[1, 5] with maximum 5
[5, 9] with maximum 9

The minimum of these maximums is 4. Therefore, the answer is 4.
"""
# The minimum among 3,4,5,9 gives 3 .. 3 is the answer