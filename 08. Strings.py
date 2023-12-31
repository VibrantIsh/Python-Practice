# 1. Create your multiline string and show how to print it.
lyrics =  '''Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow
Your heart is all I own
And in your eyes, you're holding mine'''
print(lyrics)
lyrics1 = "Cause we were just kids when we fell in love \n Not knowing what it was \nI will not give you up this time \nBut darling, just kiss me slow \nYour heart is all I own \nAnd in your eyes, you're holding mine"
print(lyrics1)

# 2. Create a program that accepts a string and displays each word's length and the length of the string.
stringinput = input("Enter your String here: ")
striglen = len(stringinput)
print("String character's length: ", striglen)
stringwordlist = stringinput.split( ) 
stringwordlist = list(stringwordlist)
stringwordlen = len(stringwordlist )
print("String word length: ", stringwordlen, "\n" )

for i in stringwordlist:
    print(f"{i} length: ", len(i))

# 3. Write a program that will count the number of lowercase and uppercase character in a user- supplied string.
stringinput = input("Enter your String here: ")
counterlower = 0
counterupper = 0
for i in stringinput:
    if i == i.lower():
        counterlower += 1
    elif i == i.upper():
        counterupper += 1
    else:
        print("Invalid Input")
print(f"Total lowercase character are: {counterlower}, Total uppercase characters are: {counterupper}")


# 4. Create a program that will count the length of the given string without relying on an in-built function. Given string:
given_string = "Jack and Jill went up the hill. To fetch a pail of water."
counter = 0
for i in given_string:
    counter += 1
print(f"Total characters length is: {given_string}")

word_counter = 0
wordsplit = given_string.split()
wordlist = list(wordsplit)
for j in wordlist:
    word_counter += 1

print(f"Character count: {counter} \nWord count: {word_counter}")

# 6. Write a program to elicit a string from the user in lower or small case letters and then 
stringinput = input("Enter your string here: ").lower()
stringaa = stringinput.title() # or stringaa = stringinput.capilatize()
print(stringaa)

# 5. Write a program to elicit a string from the user and then determine the total number of characters included in a string.
string_input = input("Enter your string here: ").lower()
counter = 0
for i in string_input:
    counter +=1 
print("Total num of chracters:", counter)


# 7. Write a program that obtains a user-supplied string. Use the isnumeric() to determine whether or not it contains numbers.
string_input = input("Enter your string here: ")
string = string_input.isnumeric()
print(string)

# 8. Write a program that obtains a user-supplied string. Use the isdigits() to determine whether or not it contains digits.
string = '065262'
print(string.isdigit())
 
string = '13Ishmeet'
print(string.isdigit())


# 9. The longest word in the dictionary is "Pneumono ultramicroscopicsilicovolcanoconiosis." Write a program that takes the longest given word in the dictionary as an input and outputs the count of only the distinct characters in it.
string_input = input("Enter your string here: ").lower()
distinct = set(string_input)
counter = 0
for i in distinct:
    counter += 1
print(counter)

# or by len method


# 10. Given: "string1=Pneumonoultramicroscopicsilicovolcanoconiosis." Write a Python program that takes the given string and returns a new string with all the vowels stripped out.
string1= "Pneumonoultramicroscopicsilicovolcanoconiosis."
vowels = "aeiou"
lst = {}
for i in string1:
    for j in vowels:
        if i == j:
            lst[i] = string1[i]
        else:
            continue

print(lst)
string1 = "Pneumonoultramicroscopicsilicovolcanoconiosis."
vowels = "aeiou"
vowel_indices = {}
for i, char in enumerate(string1):
    if char in vowels:
        if char in vowel_indices:
            vowel_indices[char].append(i)
        else:
            vowel_indices[char] = [i]

print(vowel_indices)


# 11. Write a Python for loop program that obtains a user-supplied string and finds out if the first character is lowercase.
string_input = input("Enter your string here: ")

for i in string_input:
    if i[0] == i.lower():
        print("True")
        break
    else:
        print("False")
        break


# 11. Write a Python for loop program that obtains a user-supplied string and finds out if the first character is lowercase.
string_input = input("Enter your string here: ")
formating = string_input.split()
lst = list(formating)
counter = 1
for i in lst:
    counter += 1
    if lst[counter] == i.title():
        print(True)  
    else:
        print("False")
        break

#13. Write a Python program that takes the given string and finds out if all the words are in upper case.
def upper_check(n):
    if n == n.upper():
        return True
    else:
        return False

strl = "STRINGS"
str2= "Strings"
result = upper_check(strl)
result1 = upper_check(str2)

print(result)
print(result1)
    

# 14. Write a Python program that takes the given string and finds out if the string includes alphanumeric characters.
strl = "Genius is 1 percent inspiration and 99 percent perspiration"
contains_alphanumeric = False

for char in strl:
    if char.isalnum():
        contains_alphanumeric = True
        break

if contains_alphanumeric:
    print("True")
else:
    print("False")

#15. Write a program to take a string as input and output a string with all the words in the input string capitalized and lowercase intermittently.
def capitalize_alternate_words(input_string):
    words = input_string.split()
    result = []
    
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.upper())
        else:
            result.append(word.lower())
    
    return ' '.join(result)

string1 = "happiness multiplies as we divide it with others."
output_string = capitalize_alternate_words(string1)
print(output_string)

# 16. Write a program that, when given a string "anopheles", will return a new string containing the same characters but in reverse order
str1 = "anopheles"
str2 = str1[::-1]
print(str2)

# 17. Write a program that, when given a string, gives back the words arranged in reverse order.
string = "A tree starts with a seed."
str2 = string.split()
lst = []
for i in str2:
    lst.append(i[::-1])
print(" ".join(lst))

#or
# str1 = string[::-1]
# print(str1)

# 18 Write a program that, when given two substrings, gives back a combined string. 
substrl = "An ounce of practice subate?" 
substr2 = "is worth a thousand words"
print(substrl+"\n",substr2)
