#Lists: ordered, mutable, allows duplicate elements

print("\nOriginal list.")
myList = ["banana", "cherry", "apple"]
print(myList)

print("\nInitializing an empty list.")
myList2 = list()
print(myList2)

print("\nShowing a list can hold different types of values at the same time.")
myList3 = [5, True, "apple", "apple"]
print(myList3)

print("\nAccessing an item in the list.")
item = myList[0]
print(item)

print("\nAccessing an item in reverse in the list.")
item = myList[-1]
print(item)

print("\nPrinting out the entire list.")
for index in myList:
    print(index)

print("\nChecking if a certain item is in the list.")
if "banana" in myList:
    print("yes")
else:
    print("no")

print("\nChecking if a certain item is in the list.")
if "lemon" in myList:
    print("yes")
else:
    print("no")

print("\nFinding the length of an array using len().")
print(len(myList))

print("\nAdding an item to the end of a list using .append().")
myList.append("lemon")
print(myList)

print("\nInserting an item into a specific index using .insert().")
myList.insert(1, "blueberry")
print(myList)

print("\nRemoving the last item in a list using .pop().")
item = myList.pop()
print(item)
print("Updated list after using .pop().")
print(myList)

print("\nRemoving a certain item from the list.")
myList.remove("cherry")
print(myList)

print("\nReversing the order of the list using .reverse().")
myList.reverse()
print(myList)

print("\nSorting a list using sorted().")
new_list = sorted(myList)
print("Original list.")
print(myList)
print("Sorted list.")
print(new_list)

print("\nSorting also works with numbers.")
myList4 = [4, 3, 1, -1, -5, 10]
print("Original list.")
print(myList4)
myList4.sort()
print("Sorted list.")
print(myList4)

print("\nClearing a list using .clear().")
myList.clear()
print(myList)

print("\nInitializing a list using a value then using * with a certain number.")
myList = [0] * 5
print(myList)

myList2 = [1, 2, 3, 4, 5]

print("\nCreating a new list by adding two lists together.")
new_list = myList + myList2
print(new_list)

myList.clear()
new_list.clear()

print("\nUsing various ways of Slicing with a Python List.")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Using 1:5.")
new_list = myList[1:5]
print(new_list)

print("Using :5.")
new_list = myList[:5]
print(new_list)

print("Using 1:.")
new_list = myList[1:]
print(new_list)

print("Using ::2 to make a copy with every 2nd index.")
new_list = myList[::2]
print(new_list)

print("\nReversing the list using slicing, ::-1.")
new_list = myList[::-1]
print(new_list)

print("\nTrying to copy a list, but failing since modifying the copy modifies the original too.")
list_original = ["banana", "cherry", "apple"]

list_copy = list_original

list_copy.append("lemon")

print(list_copy)
print(list_original)

print("\nCorrect way to copy a list using .copy().")
list_original = ["banana", "cherry", "apple"]

list_copy = list_original.copy()

list_copy.append("lemon")

print(list_copy)
print(list_original)

print("\nAnother correct way to copy a list using list().")
list_original = ["banana", "cherry", "apple"]

list_copy = list(list_original)

list_copy.append("lemon")

print(list_copy)
print(list_original)

print("\nAnother correct way to copy a list using slicing, :.")
list_original = ["banana", "cherry", "apple"]

list_copy = list_original[:]

list_copy.append("lemon")

print(list_copy)
print(list_original)

print("\nModifying a list.")
myList = [1, 2, 3, 4, 5, 6]
modified_List = [index * index for index in myList]

print(myList)
print(modified_List)