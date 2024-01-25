from Heap import MinHeap as mh

a = mh([4,10,3,5,1])
print(a)
b = []
for i in range(len(a)):
    b.append(a.pop())
print(b)