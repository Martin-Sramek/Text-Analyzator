# Create databases of texts, users and their password:
texts = ['''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, which traverse the valley.''',

'''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils represent several varieties of perch, as well as 
other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
separator = "-" * 40

# Welcome user:
print(separator)
print("Welcome to the app. Please log in.")

# Check user's name and password:
name = input("Enter your user name: ")

if name not in users:
    print('The user "{}" is not in our database! Closing the program...'.format(name))
    exit()

password = input("Enter your password: ")

if password != users[name]:
    print('"{}" is the invalid password for the user "{}"! Closing the program...'.format(password, name))
    exit()

print(separator)

# User has to pick up one text for analysis:
print("We have 3 texts to be analyzed:")
print("""   
    1: {}

    2: {}

    3: {}
""".format(texts[0], texts[1], texts[2]))
choice = int(input("Choose one of the text above for analysis. Enter the number of the text you want to analyze: "))

analyzed_string = texts[choice - 1]

# Analysis of the selected text:
analyzed_string = analyzed_string.replace(",", "")
analyzed_string = analyzed_string.replace(".", "")

list_of_words = analyzed_string.split()

longest_word = 0
for word in list_of_words:  # search for the longest string in the analyzed text
    if len(word) > longest_word:
        longest_word = len(word)

word_length = [0] * longest_word  # creating of list where lenght of words will be stored
words = len(list_of_words)
lower = 0
title = 0
upper = 0
digits = 0
sum_of_numbers = 0

for word in list_of_words:
    word_length[len(word) - 1] += 1  # adding length of the word to the list
    if not word.isdigit():
        if word.islower():
            lower += 1
        elif word.istitle():
            title += 1
        elif word.isupper():
            upper += 1
    else:
        digits += 1
        sum_of_numbers += int(word)

chart = ""

for i, length in enumerate(word_length):
    if length != 0:
        chart += "{} {} {}\n".format(i + 1, "*" * length, length)

# Printing results:
print(separator)
print("There are {} words in the selected text.".format(words))
print("There are {} titlecase words.".format(title))
print("There are {} uppercase words.".format(upper))
print("There are {} lowercase words.".format(lower))
print("There are {} numeric strings.".format(digits))
print(separator)
print("Distribution of words in the text according to their length:")
print(chart.strip())
print(separator)
print("If we summed all the numbers in this text we would get: {}".format(sum_of_numbers))
print(separator, end="")
print("Poslední řádek")