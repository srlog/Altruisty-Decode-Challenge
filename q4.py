"""Q4. 
At a festival, a street vendor is selling candy in different flavours. He has N different  flavours of candy (C[]). The task is to find the first  flavours of candy that appears an odd number of times in the batch of candies."""

n = int(input())

flavours = list()

for i in range(n):
    flavours.append(input()) # Reading n flavours


diff_flavours = []
for each in flavours:
    if each not in diff_flavours and flavours.count(each) % 2 != 0: # checking for unique flavours that are have odd occurences
        diff_flavours.append(each) 
if len(diff_flavours) != 0:
    print(diff_flavours[0]) # Printing the first odd flavour
else:
    print("All are Even")
