#Insertion Sort
def insertionSort(data):
    for i in range(1,len(data)):
        j = i
        while j > 0 and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
            j = j-1
    return data

data = [5,2,4,6,1,3]
print(insertionSort(data))
#best case time complexity O(n)
#worst case time complexity: O(n^2) because of nested loops and swaps in the inner loop 
#space complexity: O(1) because no extra space is used 




