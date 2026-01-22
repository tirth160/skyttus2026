
#1. Take a string input and print its length
text = input("Enter a string: ")
print(len(text))


#2. Convert a sentence to lowercase
sentence = "Hello World"
print(sentence.lower())


#3. Replace spaces with underscores
text = "hello world python"
print(text.replace(" ", "_"))


#4. Extract the first and last character of a string
word = "Python"
print(word[0], word[-1])


#5. Reverse a string using slicing
word = "Python"
print(word[::-1])


#6. Count how many times a letter appears in a string
text = "banana"
print(text.count("a"))


#7. Check if a word is present in a sentence
sentence = "I love Python programming"
print("Python" in sentence)


#8. Take name & age and print using f-string
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old")


#9. Remove extra spaces from start and end
text = "   hello world   "
print(text.strip())


#10. Join a list of words with '-' between them
words = ["python", "is", "fun"]
print("-".join(words))


#11. Create a list of 5 favorite movies
movies = ["Inception", "Avatar", "Titanic", "Joker", "Gladiator"]
print(movies)


#12. Add a new movie to the list
movies.append("Interstellar")
print(movies)


#13. Remove the first movie from the list
movies.pop(0)
print(movies)


#14. Sort a list of numbers in ascending order
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers)


#15. Reverse a list
numbers.reverse()
print(numbers)


#16. Find the largest number in a list
print(max("numbers"))


#17. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)


#18. Access the last element of a list without using index number
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list[-1])


#19. Create a nested list and access an inner element
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][0])   # Output: 3


#20. Count how many times an element appears in a list
nums = [1, 2, 2, 3, 2, 4]
print(nums.count (2))


