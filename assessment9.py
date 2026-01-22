# #1 Write a program to read a file and display its contents. 
# file = open("sample.txt", "w")
# file.write("Hello Python\n")
# file.write("This is a sample file\n")
# file.write("File handling in Python is easy\n")
# file.close()


# file = open("sample.txt", "r")
# print(file.read())
# file.close()

# #2 Write a program to count the number of lines in a file.
# file = open("sample.txt", "r")
# lines = file.readlines()
# print("Number of lines:", len(lines))
# file.close()

# #3 Write a program to count how many times each word appears in a file.
# file = open("sample.txt", "r")
# text = file.read().split()
# file.close()

# word_count = {}
# for word in text:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)

# #4 Write a program to write 5 user-entered sentences to a file.
# file = open("sentences.txt", "w")

# for i in range(5):
#     sentence = input("Enter a sentence: ")
#     file.write(sentence + "\n")

# file.close()

# #5 Write a program to append a list of strings to an existing file.
# lines = ["Apple\n", "Banana\n", "Cherry\n"]

# file = open("fruits.txt", "a")
# file.writelines(lines)
# file.close()
  
# #6 Write a program to read a file and print only lines containing a specific word.
# word = input("Enter word to search: ")

# file = open("sample.txt", "r")
# for line in file:
#     if word in line:
#         print(line)
# file.close()

# #7 Write a program to replace a specific word in a file and save changes.


# file = open("input.txt", "w")
# file.write("I like apple. Apple is a fruit.")
# file.close()


# file = open("input.txt", "r")
# data = file.read()
# file.close()


# old_word = "apple"
# new_word = "orange"
# data = data.replace(old_word, new_word)


# file = open("input.txt", "w")
# file.write(data)
# file.close()

# print("Word replaced successfully.")


# #8 Write a program to merge the contents of two text files into a third file.

# file1 = open("file1.txt", "w")
# file1.write("This is file one.\nHello from file1.")
# file1.close()

# file2 = open("file2.txt", "w")
# file2.write("This is file two.\nHello from file2.")
# file2.close()

# file1 = open("file1.txt", "r")
# file2 = open("file2.txt", "r")

# data1 = file1.read()
# data2 = file2.read()

# file1.close()
# file2.close()

# file3 = open("merged.txt", "w")
# file3.write(data1 + "\n" + data2)
# file3.close()

# print("Files merged successfully.")

# #9 Write a program to read a CSV file and display its content in a formatted way.

# with open("data.csv", "w") as file:
#     file.write("Name,Age,City\n")
#     file.write("Alice,25,New York\n")
#     file.write("Bob,30,Los Angeles\n")
#     file.write("Charlie,22,Chicago\n")


# with open("data.csv", "r") as file:
#     for line in file:
#         row = line.strip().split(",")  # Split by comma
#         print("{:<10} {:<5} {:<15}".format(row[0], row[1], row[2]))


#10 Write a program to back up a file by copying its contents into another file.

with open("original.txt", "w") as file:
    file.write("This is the original file.\nIt has some text inside.")


with open("original.txt", "r") as source:
    data = source.read()

with open("backup.txt", "w") as backup:
    backup.write(data)

print("Backup created successfully.")
	