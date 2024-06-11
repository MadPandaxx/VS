def selectionsort (arr):
    for i in range(len(arr) - 1):
        lowestnumberindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowestnumberindex]:
                lowestnumberindex = j
        if lowestnumberindex != i:
            arr[i], arr[lowestnumberindex] = arr[lowestnumberindex], arr[i]
    return arr

arr = [4, 2, 16, 32, 8]
sorted_arr = selectionsort(arr)
print("Hasil Selection Sort", sorted_arr)