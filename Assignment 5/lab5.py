# Pok On Cheng 74157306 and Christina Pearl Wang 66561706. ICS 31 Lab sec 5. Lab asst 5.

#
#
# Part (c)
#
#

print("\n")
print("Part (c)")
print(" ")

print("\n")
print("Part (c1)")
print(" ")

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
d1 = Dish("Kung Pao Chicken", 9.50, 550)
d2 = Dish("Paht Woon Sen", 9.50, 330)
d3 = Dish("Big Mac", 5.75, 550)

print("\n")
print("Part (c2)")
print(" ")

def Dish_str(ds: Dish) -> Dish:     return ds.name + " ($" + str(ds.price) + "): " + str(ds.calories) + " cal"
print(Dish_str(d2))

print("\n")
print("Part (c3)")
print(" ")

def Dish_same(ds1: Dish, ds2: Dish, string: str) -> bool:
    if string == "name":    # Test if two dishes' name are equal
        return ds1.name == ds2.name
    elif string == "price": # Test if two dishes' price are equal
        return ds1.price == ds2.price
    elif string == "calories":  # Test if two dishes' calories are equal
        return ds1.calories == ds2.calories
assert Dish_same(d1, d3, "name") == False
assert Dish_same(d2, d1, "price") == True
assert Dish_same(d3, d2, "calories") == False
print(Dish_same(d1, d2, "name"))
print(Dish_same(d2, d3, "price"))
print(Dish_same(d3, d1, "calories"))

print("\n")
print("Part (c4)")
print(" ")

def Dish_change_price(dcp: Dish, percent: int) -> Dish:
    
    number = dcp.price
    new_price = number * (1 + (percent / 100))
    dcp = dcp._replace(price = new_price)
    return dcp
print(Dish_change_price(d2, 100))

print("\n")
print("Part (c5)")
print(" ")

def Dish_is_cheap(dic: Dish, number: float) -> bool:
    return dic.price < number
assert Dish_is_cheap(d1, 1.00) == False
assert Dish_is_cheap(d3, 10.00) == True
print(Dish_is_cheap(d1, 10))
print(Dish_is_cheap(d3, 1))

print("\n")
print("Part (c6)")
print(" ")

d4 = Dish("Vietnamese Pho Rice Noodles Soup", 8.75, 650)
d5 = Dish("Stir Fried Rice", 5.75, 625)
DL = [d1, d2, d3, d4, d5]
d6 = Dish("Chicken Nugget", 4.75, 575)
d7 = Dish("Mashed Potato", 3.99, 450)
d8 = Dish("Tofu Soup", 5.99, 500)
d9 = Dish("Sushi", 5.85, 330)
DL2 = [d6, d7, d8, d9]
big_list1 = []
for i in DL:
    big_list1.append(i)
for i in DL2:
    big_list1.append(i)
print(big_list1)
big_list2 = []
for i in DL:
    big_list2.extend(i)
for i in DL2:
    big_list2.extend(i)
print(big_list2)
print()
def Dishlist_display(dl: Dish) -> str:
    string = ""
    for i in dl:
        string = string + i[0] + " " + str(i[1]) + " " + str(i[-1]) + "\n"
    return string
print(Dishlist_display(big_list1))

print("\n")
print("Part (c7)")
print(" ")

def Dishlist_all_cheap(dl: Dish, number: float) -> bool:
    j = 0
    k = 0
    for i in dl:
        if i[1] < number:
            j = j + 1
        k = k + 1
    return j == k
print(Dishlist_all_cheap(big_list1, 10.00))
print(Dishlist_all_cheap(big_list1, 5.00))

print("\n")
print("Part (c8)")
print(" ")

def Dishlist_all_change(dl: Dish, percent: int) -> Dish:
    dl2 = []
    j = 1
    for i in dl:
        new_price = i.price
        new_price = new_price * (1 + (percent / 100))
        i = i._replace(price = new_price)
        dl2.append(i)
    return dl2
print(Dishlist_all_change(big_list1, 100))


print("\n")
print("Part (c9)")
print(" ")

def Dishlist_price(dl: Dish) -> list:
    dl_price = []
    for i in dl:
        price = i.price
        dl_price.append(price)
    return dl_price
print(Dishlist_price(big_list1))

print("\n")
print("Part (c10)")
print(" ")

def Dishlist_average(dl: Dish) -> float:
    dl_price2 = Dishlist_price(dl)
    total = 0
    j = 0
    for i in dl_price2:
        total = total + i
        j = j + 1
    average = total / j
    return average
print(Dishlist_average(big_list1))

print("\n")
print("Part (c11)")
print (" ")

def Dishlist_keep_cheap(dl: Dish, number: float) -> list:
    d1 = []
    for i in dl:
        if i.price < number:
            d1.append(i)
    return d1
print(Dishlist_keep_cheap(big_list1, 5.00))

print("\n")
print("Part (c12)")
print(" ")

d10 = Dish("Salad", 4.85, 100)
d11 = Dish("Beef Stew", 3.55, 230)
d12 = Dish("Steak", 15.85, 500)
d13 = Dish("Pasta", 7.85, 420)
d14 = Dish("Lobster", 21.85, 330)
d15 = Dish("Potato Salad", 2.85, 130)
d16 = Dish("Spam Masubi", 1.00, 110)
d17 = Dish("Nachos", 6.85, 330)
d18 = Dish("Tacos", 2.85, 410)
d19 = Dish("Cheeseburger", 4.85, 330)
d20 = Dish("Sandwhich", 5.00, 270)
d21 = Dish("Pipeline Bowl", 4.99, 280)
d22 = Dish("Udon", 5.85, 330)
d23 = Dish("Pad Thai", 7.95, 530)
d24 = Dish("Casserole", 5.85, 330)
d25 = Dish("Burrito", 8.80, 675)
DL3 = [d1,d2,d3,d4,d5,
       d6,d7,d8,d9,d10,
       d11,d12,d13,d14,d15,
       d16,d17,d18,d19,d20,
       d21,d22,d23,d24,d25]

def before_and_after():
    number = int(input("Enter the percentage that you want to change: "))
    print("Before changing")
    print(Dishlist_display(DL3))
    j = 0
    for i in DL3:
        new_price = i.price
        new_price = new_price * (1 + (number / 100))
        DL3[j] = DL3[j]._replace(price = new_price)
        `
    print("After changing")
    print(Dishlist_display(DL3))
    return
before_and_after()

#
#
# Part (e)
#
#

print("\n")
print("Part (e)")
print(" ")

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

print("\n")
print("Part (e1)")
print(" ")

r3 = Restaurant('Pascal', ' French', '940-752-0107', [Dish('escargots', 12.95, 250),
                                                      Dish('Poached Salmon', 18.50, 550),
                                                      Dish('Rack of Lamb', 24.00, 850),
                                                      Dish('Marjolaine cake', 8.50, 950)])

print("\n")
print("Part (e2)")
print(" ")

RL = [r1, r2, r3]
def Restaurant_first_dish_name(r: Restaurant) -> str:
    return r.menu[0].name
for i in RL:
    print(Restaurant_first_dish_name(i))

print("\n")
print("Part (e3)")
print(" ")

def Restaurant_is_cheap (r: Restaurant, number: float) -> bool:
    return Dishlist_all_cheap(r.menu, number)
print(Restaurant_is_cheap(r3, 25.00))


print("\n")
print("Part (e4)")
print(" ")

C = [r1, r2, r3]
def Collection_raise_prices(C: list) -> list:
    for i in range(len(C)):
        for l in range(len(C[i].menu)):
            new_price = C[i].menu[l].price
            new_price += 2.50
            C[i].menu[l] = C[i].menu[l]._replace(price = new_price)
    return C
print(Collection_raise_prices(C))
print()
def Collection_change_price(C: list, number: int) -> list:
    for i in range(len(C)):
        for l in range(len(C[i].menu)):
            new_price = C[i].menu[l].price
            new_price = new_price * (1 + (number / 100))
            C[i].menu[l] = C[i].menu[l]._replace(price = new_price)
    return C
print(Collection_change_price(C, 10))

print("\n")
print("Part (e5)")
print(" ")

def Collection_select_cheap(C: list, number: float) -> list:
    new_list = []
    for i in range(len(C)):
        total = 0
        count = 0
        for l in range(len(C[i].menu)):
            total = total + C[i].menu[l].price
            count += 1
        average = total / count
        if average <= number:
            new_list.append(C[i])
    return new_list
print(Collection_select_cheap(C, 18.00))

#
#
# Part (g)
#
#

print("\n")
print("Part (g)")
print(" ")

print("\n")
print("Exercise 4.13")
print(" ")

s = 'abcdefghijklmnopqrstuvwxyz'

print("\n")
print("Exercise 4.13(a)")
print(" ")

print(s[1] == 'b' and s[2] == 'c')

print("\n")
print("Exercise 4.13(b)")
print(" ")

print(s[0:14] == 'abcdefghijklmn')

print("\n")
print("Exercise 4.13(c)")
print(" ")

print(s[14:28] == 'opqrstuvwxyz')

print("\n")
print("Exercise 4.13(d)")
print(" ")

print(s[1:27] == 'bcdefghijklmnopqrstuvwxyz')

print("\n")
print("Exercise 4.14")
print(" ")

print("\n")
print("Exercise 4.14(a)")
print(" ")

log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/text.txt HTTP/1.0"'
print(log)

print("\n")
print("Exercise 4.14(b)")
print(" ")

address = log.split(' ')
print(address[0])

print("\n")
print("Exercise 4.14(c)")
print(" ")

address3 = address[3].replace('[','(')
address4 = address[4].replace(']',')')
date = address3 + ' ' + address4
print(date)

print("\n")
print("Exercise 4.19")
print(" ")

first = 'Marlena'
last = 'Sigel'
middle = 'Mae'

print("\n")
print("Exercise 4.19(a)")
print(" ")

a = last + ', ' + first + ' ' + middle
print(a)

print("\n")
print("Exercise 4.19(b)")
print(" ")

b = last + ', ' + first + ' ' + middle[0] + '.'
print(b)

print("\n")
print("Exercise 4.19(c)")
print(" ")

c = first + ' ' + middle[0] + '. ' + last
print(c)

print("\n")
print("Exercise 4.19(d)")
print(" ")

d = first[0] + '. ' + middle[0] + '. ' + last
print(d)

print("\n")
print("Exercise 4.23")
print(" ")

def average():
    s = input("Enter a sentence: ")
    print(s.strip(' '))
    total = 0
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFFGHIJKLMNOPQRSTUVWXYZ':
            total = total + 1
    n = s.split(' ')
    num = len(n)
    average = total / num
    return average
print(average())

#
#
# Part (h)
#
#

print("\n")
print("Part (h)")
print(" ")

Count = namedtuple('Count', 'letter number')
C = []
def letter_count(string1: str, string2: str) -> list:
    ''' If two characters are equal, number add one, then create a Count. Then, return the list of Count
    '''
    j = 0
    for i in range(len(string2)):
        number = 0
        for l in range(len(string1)):
            if string1[l] == string2[i]:
                number += 1
        C.append(Count(string2[i], number))
        j = j + 1
    return C
assert letter_count('The cabbage has baggage', 'abcd') == [Count(letter='a', number=5), Count(letter='b', number=3), Count(letter='c', number=1), Count(letter='d', number=0)]
print(letter_count('The cabbage has baggage', 'abcd'))
