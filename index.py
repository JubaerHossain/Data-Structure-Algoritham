class DijSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def Union (self, x, y):

        x_set = self.find(x)
        y_set = self.find(y)

        if x_set == y_set:
            return

        if self.rank[x_set] <  self.rank[y_set]:
            self.parent[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set
        else:
            self.parent[y_set] = x_set
            self.rank[x_set] += 1


obj = DijSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)

if obj.find(0) == obj.find(4):
    print("Yes")
else:
    print("No")

if obj.find(1) == obj.find(0):
    print("Yes")
else:
    print("No")