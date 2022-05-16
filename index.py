#python tuple

tupleList = (1,2,3,4,5,6,7,8,9,10)

tupleToList = list(tupleList) #  tuples to convert to list because tuple is immutable
tupleToList.append(11)
tupleToList.append(12)
tupleToList.append(13)

tupleToList.remove(11) # remove element from list and convert back to tuple
tupleList = tuple(tupleToList) 

newItem = ('newItem',)

tupleList += newItem

(newItem, *printData) = tupleList # unpacking tuple

for x in tupleList: # loop through tuple
    print(x)
for x in range(len(tupleList)): # loop through tuple
    print(tupleList[x])

joinList = tupleList * 2 # join tuple
print(joinList)

# tuple methods 
print(tupleList.count(1)) # count number of times 1 appears in tuple
print(tupleList.index(1)) # index of 1 in tuple