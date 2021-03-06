# Pok On Cheng 74157306 and Erik Henriquez 57374677. ICS 31 Lab sec 5. Lab asst 4.

#
#
# Part (c)
#
#

print("\n")
print("Part (c)")
print(" ")

print("\n")
print("Exercise 3.17")
print(" ")

a, b, c = 3, 4, 5

print("\n")
print("3.17(a)")
print(" ")

if a < b:
    print("OK")

print("\n")
print("3.17(b)")
print(" ")

if c < b:
    print("OK")

print("\n")
print("3.17(c)")
print(" ")

if (a + b) == c:
    print("OK")

print("\n")
print("3.17(d)")
print(" ")

if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
    print("OK")

print("\n")
print("Exercise 3.18")
print(" ")

print("\n")
print("3.18(a)")
print(" ")

if a < b:
    print("OK")
else:
    print("NOT OK")

print("\n")
print("3.18(b)")
print(" ")

if c < b:
    print("OK")
else:
    print("NOT OK")

print("\n")
print("3.18(c)")
print(" ")

if (a + b) == c:
    print("OK")
else:
    print("NOT OK")

print("\n")
print("3.18(d)")
print(" ")

if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
    print("OK")
else:
    print("NOT OK")

print("\n")
print("Exercise 3.19")
print(" ")

lst = ["January", "February", "March"]
for i in lst:
    print(i[0:3])

print("\n")
print("Exercise 3.20")
print(" ")

lst = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if ((i ** 2) % 8) == 0:
        print(i)

#
#
# Part (d)
#
#

print("\n")
print("Part (d)")
print(" ")

print("\n")
print("Part (d1)")
print(" ")

def is_vowel (letter: str) -> bool:
    return letter in 'aeoiuAEIOU'
assert is_vowel('a') == True
assert is_vowel('Z') == False
print(is_vowel('X'))

print("\n")
print("Part (d2)")
print(" ")

def print_nonvowels (word: str) -> str: #Takes a string and prints a new string
#which only has the nonvowels
    for i in word:
        if i not in 'aeoiuAEIOU':
            print(i)
#assert print_nonvowels('C') == 'C'
print_nonvowels('Computer') #Testing this since we can't really assert the function properly.
print (' ')
print_nonvowels('Happy')

print("\n")
print("Part (d3)")
print(" ")

def nonvowels (word: str) -> str:
    new_string = '' #Named new_string instead of results
    for i in word:
        if i not in 'aeoiuAEIOU':
            new_string = new_string + i + " " #Included a space to show each character better.
    return new_string
assert nonvowels('Computer') == 'C m p t r '
print(nonvowels('2,34'))
print(nonvowels('Happy'))
print(nonvowels('Rata#3for_us'))

print("\n")
print("Part (d4)")
print(" ")

def consonants (sentence: str) -> str:
    results = nonvowels(sentence)
    new_sentence = ''
    for i in results:
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            new_sentence = new_sentence + i + " "
    return new_sentence
print(consonants('Rata#3for_us'))

print("\n")
print("Part (d5)")
print(" ")

def vowels (word: str) -> str: #Makes string of vowels
    vowels_string = ''
    for i in word:
        if i in 'aeoiuAEIOU':
            vowels_string = vowels_string + i + " "
    return vowels_string
def select_letters (word_type: str, word: str) -> str:
    if word_type == 'v':
        return vowels(word)
    elif word_type == 'c':
        return consonants(word)
    else:
        empty_string = ''
        return empty_string
print (select_letters ('v', 'facetiously'))
print (select_letters ('c', 'facetiously'))

print("\n")
print("Part (d6)")
print(" ")

def hide_vowels (word:str) -> str:
    new_string1 = ''
    for i in word:
        if i in 'aeiouAEIOU':
            new_string1 = new_string1 + "-"
        else:
            new_string1 = new_string1 + i
    return new_string1
print(hide_vowels("Happy Midterm"))

#
#
# Part (e)
#
#

print("\n")
print("Part (e)")
print(" ")

print("\n")
print("Exercise 3.22")
print(" ")

list22 = eval(input("Enter list of words: "))
for i in list22:
    if i != 'secret':
        print(i)

print("\n")
print("Exercise 3.23")
print(" ")

list23 = eval(input("Enter list: "))
for i in list23:
    if i[0] in 'ABCDEFGHIJKLM':
        print(i)

print("\n")
print("Exercise 3.24")
print(" ")

list24 = eval(input("Enter a list: "))
print("The first list element is", list24[0])
print("The last list element is", list24[-1])

#
#
# Part (f)
#
#

print("\n")
print("Part (f)")
print(" ")

from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

print("\n")
print("Part (f1)")
print(" ")

def restaurant_name(rl: Restaurant) -> Restaurant:
    return rl.name
def alphabetical(rl: Restaurant) -> Restaurant:
    rl = sorted(rl, key = restaurant_name, reverse = False)
    return rl
print(alphabetical(RL))

print("\n")
print("Part (f2)")
print(" ")

def alphabetical_names(rl: Restaurant) -> Restaurant:
    rl = sorted(rl, key = restaurant_name, reverse = False)
    rl_new = []
    for i in rl:
        rl_new.append(i.name)
    return rl_new
print(alphabetical_names(RL))

print("\n")
print("Part (f3)")
print(" ")

def all_Thai(rl: Restaurant) -> Restaurant:
    rl_new = []
    for i in rl:
        if i[1] == "Thai":
            rl_new.append(i.name)
    return rl_new
print(all_Thai(RL))

print("\n")
print("Part (f4)")
print(" ")

def select_cuisine(rl: Restaurant, num: int):
    if num == 0:
        rl_new = []
        string = input("Please select the cuisine of restaurants: ")
        for i in rl:
            if i.cuisine == string:
                rl_new.append(i.name)
        print(rl_new)
        return  rl_new
    elif num == 1:
        string = input("Please select the cuisine of restaurants: ")
        rl_new = []
        for i in rl:
            if i.cuisine == string:
                rl_new.append(i)
        average = average_price(rl_new)
        return average
    elif num == 2:
        string = input("Please select the cuisine of first restaurants: ")
        rl_new = []
        for i in rl:
            if i.cuisine == string:
                rl_new.append(i)
        string = input("Please select the cuisine of second restaurants: ")
        for i in rl:
            if i.cuisine == string:
                rl_new.append(i)
        average = average_price(rl_new)
        return average
    elif num == 3:
        return select_cheaper(rl, 1)
print(select_cuisine(RL, 0))

print("\n")
print("Part (f5)")
print(" ")

def select_cheaper(rl: Restaurant, num: int) -> Restaurant:
    rl_new = []
    if num == 0:
        number = float(input("Please enter a price: "))
        for i in rl:
            if i.price < number:
                rl_new.append(i.name)
    elif num == 1:
        for i in rl:
            if i.price < 15.00:
                rl_new.append(i.name)
    return rl_new
print(select_cheaper(RL, 0))

print("\n")
print("Part (f6)")
print(" ")

def average_price(rl: Restaurant) -> float:
    total = 0.0
    count = 0
    for i in rl:
        total = total + i[4]
        count = count + 1
    average = total / count
    return average
print(average_price(RL))

print("\n")
print("Part (f7)")
print(" ")

print(select_cuisine(RL, 1))

print("\n")
print("Part (f8)")
print(" ")

print(select_cuisine(RL, 2))

print("\n")
print("Part (f9)")
print(" ")

print(select_cuisine(RL, 3))

#
#
# Part (g)
#
#

print("\n")
print("Part (g)")
print(" ")

print("\n")
print("Exercise 3.25")
print(" ")

def four_multiples():
    num = int(input("Enter n: "))
    j = 0
    for i in range(4):
        mult = j * num
        print(mult)
        j = j + 1
four_multiples()

print("\n")
print("Exercise 3.26")
print(" ")

def num_squares():
    num = int(input("Enter n: "))
    j = 0
    for i in range(num):
        print(j ** 2)
        j = j + 1
num_squares()
