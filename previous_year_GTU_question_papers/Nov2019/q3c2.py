# Explain Lists, Tuples and Dictionaries with example and give comment on mutability for each of them.

########## LISTS ##########
"""
Lists are one of the most powerful tools in python. 
They are just like arrays declared in other languages. 
But the most powerful thing is that list need not be always homogeneous. 
A single list can contain strings, integers, as well as objects. 
Lists can also be used for implementing stacks and queues. 

Lists are mutable, i.e., they can be altered once declared.
"""
print("\n\n########## LISTS ##########\n")
l = [1, "a", "string", 1+2]
print(f"List l = {l}")
l.append(6)
print(f"Appended list l = {l}")
l.pop()
print(f"Popping element from list l = {l}")
print(f"Printing element at index 1 in list = {l[1]}")


########## TUPLES ##########
"""
A tuple is a sequence of immutable Python objects. 
Tuples are just like lists with the exception that tuples cannot be changed once declared.
Tuples are usually faster than lists.
"""
print("\n\n########## TUPLES ##########\n")
tup = (1, "a", "string", 1+2)
print(tup)
print(f"Element at index 1 in tuple = {tup[1]}")


########## DICTIONARIES ##########
"""
Dictionary in Python is an unordered collection of data values, 
used to store data values like a map, 
which unline other Data Types that holds key:value pair. 
Key value is provided in the dictionary to make it more optimized.
Note - Keys in a dictionary doesn't allows polymorphism.

In Python, a Dictionary can be created by placing sequence of elements within curly {} braces, separated by 'comma'.
Dictionary holds a pair of values, one being the key and the other corresponding pair element being its Key:value.
Values in a dictionary can be of any datatype and can be duplicated, whereas keys can't be repeated and must be immutable.
Note - Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.
"""
print("\n\n########## DICTIONARIES ##########\n")
# Creating a Dictionary with Integer Keys
dictionary = {1: "A", 2: "B", 3: "C"}
print("\nDictionary with the use of Integer Keys: ")
print(dictionary)

# Creating a Dictionary with Mixed Keys
dictionary_mixed = {"Name": "Jon", 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(dictionary_mixed)
