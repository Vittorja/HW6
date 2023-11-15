list_1 = [12, 3, 4, 10]
print(list_1)
list_2 = [1]
list_3 = []
list_4 = [12, 3, 4, 10, 8]
list_1.insert(0, list_1.pop())
print(list_1)
list_2.insert(0, list_2.pop())
print(list_2)
list_2.insert(0, list_2.pop())
print(list_2)
print(list_3)
list_3 = []
if list_3:
    list_3.insert(0, list_3.pop())
else:
    print(list_3)
print(list_4)
list_4.insert(0, list_4.pop())
print(list_4)
