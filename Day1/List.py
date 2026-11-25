# A list stores multiple values in one variable.
# Lists are:
# Ordered.
# Changeable (mutable).
# Able to contain duplicate values.

List = [20,30,40]
print(List)
print(type(List))
print(List[0])
print(List[1])
print(List[2])
# changing the value of Index 0
List[0] =  "Maaz"
print(List)
# adding Item
List.append(50)
print(List)
# changing the value of Index 0
List[0] = 20
# Sorting the List
List.sort()
print(List)
# removing an item
List.remove(50)
print(List)



