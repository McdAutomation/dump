class A:
    def __init__(self,data):
        self.data = data
        self.children = []
    def addNode(self,node):
        self.children.append(node)

a = A(5)
b = A(6)
c = A(9)

a.addNode(b)
b.addNode(c)

temp = a
while len(temp.children) > 0:
    print(temp.data)
    temp = temp.children[0]
