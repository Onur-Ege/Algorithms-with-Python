# this code always swap the biggest element to the left until all element is sorted
# time complexity: O(n'2)
# space complexity: O(1)

ourList = []
while True:
    try:
        line = input()
        if line == '':
            break
        ourList.append(line)
    except EOFError:
        break
n = len(ourList)


# function that swap bigger element to left
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


# function that perform sorting
def fun(x):
    for i in range(n-1):
        for j in range(i+1, n):
            # if next element is bigger swap
            if int(x[j]) < int(x[i]):
                swap(x, i, j)
                print("swap " + str(x[i]) + " and " + str(x[j]))
                print("new list: ", end="")
                print(x)
    return x


print("first list", end="")
print(ourList)
print("")
# sorting unsorted list
ourList = fun(ourList)
print("sorted sequence: ",end="")
# printing sorted list
print(ourList)