"""q5
The Selection of candidates for ZSCS includes a strength test conducted on the field. A group of 4 trainees is participating in a lifting test for 3 rounds. After each round, you will record the strength level (in kilograms) lifted by each trainee. After all trainees complete all rounds, calculate the average strength level for each trainee across the 3 rounds, and identify the trainee (or trainees) with the highest average strength level as the strongest. If multiple trainees attain the same highest average level, they should all be selected."""

data = list()
for i in range(3): # 3 rounds
    each_round = list()
    for j in range(4): # 4 trainees
        read = int(input())
        if read < 1 or read > 200:
            print("INVALID INPUT")
            exit()
        each_round.append(read)
    data.append(each_round)

r1 , r2, r3 = data

# Calculating the average for each trainee
t1 = (r1[0] + r2[0] + r3[0]) // 3
t2 = (r1[1] + r2[1] + r3[1]) // 3
t3 = (r1[2] + r2[2] + r3[2]) // 3
t4 = (r1[3] + r2[3] + r3[3]) // 3

avgs = [t1, t2, t3, t4]
max_strength = max(avgs)


if max_strength<100:
    print("All trainees are unfit")
    exit()
# Trainees with highester average strength
for i in range(len(avgs)):
    if avgs[i] == max_strength:
        print(f"Trainee Number: {i+1}")

    




