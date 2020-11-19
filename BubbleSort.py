def bubblesort(array):
    n = len(array)

    for num in range(n - 1):

        for j in range(0, n - num - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


arr = [64, 34, 25, 12, 22, 11, 90]


bubblesort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
    # print("%d" % arr[i]),
