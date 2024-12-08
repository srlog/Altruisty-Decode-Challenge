"""Bees and flowers are placed on a line segment represented by a string. The character `*` represents a bee, and `|` represents a flower. The string consists of only these two characters. You are given two arrays, `startIndex` and `endIndex`, which represent ranges on the line segment. For each range, calculate the number of bees between two flowers, including the flowers at the endpoints.
Note: `startIndex` and `endIndex` are 1-indexed.
"""


string = input("ENTER your string: ")

# Reading starting indexes
start_index = list() 
start_n = int(input())
for i in range(start_n):
    start_index.append(int(input()))

# Reading ending indexes
end_n = int(input())
end_index = list()  
for i in range(end_n):  
    end_index.append(int(input()))


ans = []
# Using zip to access them as pairs
for s, e in zip(start_index, end_index):
    this = string[s:e] # Substring with the given range
    count = this.count("|*|") # Finding the number of bees between flowers
    ans.append(count)

print(ans)

