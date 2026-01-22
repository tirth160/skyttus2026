1. Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
print(number)


2. Access the third element
numbers = (10, 20, 30, 40, 50)
print(numbers[2])



3. Unpack a tuple into variables
numbers = (10, 20, 30, 40, 50)
a, b, c, d, e = numbers
print(a, b, c, d, e)

4. Access the third element in a tuple. 
t = (10, 20, 30, 40)
print(t[2])

5. Unpack a tuple into separate variables. 
t = (10, 20, 30, 40)
a, b, c, d = t
print(a, b, c, d)


6. Create a set of 5 fruits.
fruits = {"apple", "banana", "mango", "orange", "grape"}
print(fruits)

  
7. Add a new fruit to the set.
fruits = {"apple", "banana", "mango", "orange", "grape"}
fruits.add("pineapple")
print(fruits)

8.  Remove an element from a set.
fruits = {"apple", "banana", "mango", "orange", "grape"}
fruits.remove("banana")
print(fruits)


9. Find union of two sets.
fruits = {"apple", "banana", "mango", "orange", "grape"}
fruits2 = {"apple", "kiwi", "mango"}
print(fruits.union(fruits2))

10.  Find inter vvvvccccccsection of two sets.
fruits = {"apple", "banana", "mango", "orange", "grape"}
fruits2 = {"apple", "kiwi", "mango"}  
print(fruits.intersection(fruits2))

 
11. Check if one set is subset of another.
fruits = {"apple", "banana", "mango", "orange", "grape"}
fruits2 = {"apple", "kiwi", "mango"}
print(fruits.issubset(fruits2))


 12.Convert a list with duplicate values into a set to remove duplicates. 
lst = [1, 2, 2, 3, 4, 4, 5]
print(set(lst))


13. Create a dictionary storing student names and marks.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)


14. Add a new key-value pair to an existing dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["David"] = 88
print(students) 


15. Delete a key-value pair from a dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
del students["Charlie"]
print(students)


16. Merge two dictionaries into one.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
extra = {"Eva": 92, "Frank": 80}
merged = {**students, **extra}
print(merged)



17. Check if a key exists in a dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Alice" in students)



18.  Count word frequency in a given string using a dictionary.
text = "apple banana apple mango banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)



19.  Find the key with the maximum value in a dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
max_key=max(students, key=students.get)
print(max_key)



 20. Reverse keys and values in a dictionary. 
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
reversed_dict = {v: k for k, v in students.items()}
print(reversed_dict)



21.  Update the value for a specific key.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Alice"] = 95
print(students)


 22.  Convert a list of tuples into a dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
tuple_list = [("Math", 90), ("Science", 85), ("English", 88)]
print(dict(tuple_list))	