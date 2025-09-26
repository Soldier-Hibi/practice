collection = []
count = 0

for i in range(5):
    element = input()
    collection.append(element)

for i in range(len(collection) -1, -1, -1):
    print(collection[i])