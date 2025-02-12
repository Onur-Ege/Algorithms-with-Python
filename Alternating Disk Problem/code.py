# This code always swap the dark disk to right
# time complexity : O(n^2)
# space complexity : O(1)

DARK = 'D'
LIGHT = 'L'
diskList = []
a = input()
diskList.append(a)


# function for swapping dark element to the right
def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


# definition of function that perform sorting
def fun(x):
    for i in range((len(x))):
        for j in range(len(x)):
            # if our element is dark swap to the right
            if x[j] is DARK:
                try:
                    print("disk positions: ",end="")
                    print(diskList)
                    # swapping
                    swap(x, j, j+1)
                except IndexError:
                    pass
    return x


# use our function to sort disk list
diskList = fun(diskList)

print("final disk positions: ",end="")
# print sorted list of disks
print(diskList)
