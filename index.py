#Merge Sort
def MergeSort(data):
    print(data)
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1



data = [54,26,93,17,77,31,44,55,20]
MergeSort(data)
print(data)


#best case: O(n)
#worst case: O(n^2)
#average case: O(n log n)
#space complexity: O(n)

