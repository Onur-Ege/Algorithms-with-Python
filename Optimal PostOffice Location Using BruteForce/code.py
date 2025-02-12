# in this code we calculate total distance for all villages from other villages and calculate the average
# then we find minimum of these distances
# time complexity: O(n^2)
# space complexity: O(n)

villages = []
while True:
    try:
        line = input()
        if line == "":
            break
        villages.append(line)
    except EOFError:
        break
averageDistanceList = []


# function that calculate average distance for all villages and add this result to average distance list
def fun(x):
    for a in x:
        total = 0
        for b in x:
            y = abs(int(a) - int(b))
            print(f"distance between{a}-{b} = {y}")
            total += y
        # printing average distance for all villages
        print(f"average distance for village {a} is {total/(len(x)-1)}")
        averageDistanceList.append(total/(len(x)-1))


# we call function for finding distances
fun(villages)

# below code find index of village that has minimum average distance
j = 0
min_average = averageDistanceList[0]

for i in range(len(averageDistanceList)):
    if averageDistanceList[i] < min_average:
        min_average = averageDistanceList[i]
        j = i

# print result
print()
print(f"we should build post office in {villages[j]} village")