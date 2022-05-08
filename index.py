dicSet = {
    'name': 'python',
    'age': 18,
}

# print(dicSet)

# # dicSet add item
# dicSet['name'] = 'python2'
# dicSet['age'] = 19
#update item
# dicSet.update({'name': 'python3', 'age': 20})
# #dicSet remove item

#get item from dic
# itm = dicSet.get('name')
# print(itm)
# remove item from dict
# dicSet.pop('name')
# print(dicSet)

#loop dict
# for i in dicSet:
#     print(i)
# print(dicSet['name'])
# print(dicSet['age'])


#copy dict
# dicSet2 = dicSet.copy()
# print(dicSet2)

#nested dict
dicSet3 = {
    'python': {
        'year': 1992
    },
    'java': {
        'year': 1995
    },
    'c++': {
        'year': 1994
    },
    'c': {
        'year': 1993
    }
}

# print(dicSet3)
for i in dicSet3:
    for j in dicSet3[i]:
        print(i, dicSet3[i][j])

#methods

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()