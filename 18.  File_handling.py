# Use the following text files for the programming exercise.

# specimenl.txt
# Fintech, a combination of the terms "financial" and technology," refers to businesses that use technology to enhance or automate financial services and processes.

# specimen2.txt
# Python is one of the famous programming language.
# Python is used in the Financial Analyses and other processing.

# specimen3.txt
# Python is useful in storing and retrieving data into a file including database.
# The data analysis is made easier in Python which make add fuels to its popularity.
# Python adopts to any upcoming trend in IT industry.




# Create a text file and then display it using a Python script
content = """Python is useful in storing and retrieving data into a file including database.
The data analysis is made easier in Python which make add fuels to its popularity.
Python adopts to any upcoming trend in IT industry."""

with open("sample.txt", "w") as file:
    file.write(content)
with open("sample.txt", "r") as file:
    print(file.read())



# 2. Create a Python program that generates a file containing a list of all English alphabet letters arranged in a specific order.
order = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

with open('alphabet.txt', 'w') as file:
    file.write(order)

# 3. Create a Python program that reads the named specimen2.txt file line-by-line and count the number of lines.
file_name = "specimen2.txt"

with open(file_name, "r") as file:
    count = sum(1 for line in file)

print(f"The total lines in the file '{file_name}' are: {count}")
