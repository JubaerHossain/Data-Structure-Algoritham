#python hash table
hash_table = [0] * 10
def checkPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True
def getPrime(n):
    if n % 2 == 0:
        n += 1
    while not checkPrime(n):
        n += 2
    return n
def hashFunction(key):
    c = getPrime(10)
    return key % c

def insert_hash(key, value):
    index = hashFunction(key)
    hash_table[index] = [key, value]
def remove_hash(key):
    index = hashFunction(key)
    hash_table[index] = 0


insert_hash(1, "one")
insert_hash(2, "two")
insert_hash(3, "three")
insert_hash(4, "four")
insert_hash(5, "five")


print(hash_table)