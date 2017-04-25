# Pok On Cheng 74157306 and Kyle Vonderwerth 50183290. ICS 31 Lab sec 5. Lab asst 3.

#
#
# Part (c)
#
#

print('\n')
print('Part (c)')
print()
print('\n')
print('Ex 3.36')
print()

def abbreviation(day):
    assert isinstance(day, str), 'day is not a string'  ##  Check if day is a string
    assert len(day) >= 2 ## Check if str len >= 2 and if str is type string
    return day[0:2] ##  return first two character in string
print(abbreviation('Tuesday'))

print('\n')
print('Ex 3.43')
print()

def distance(second):
    assert isinstance(second, int), 'Second is not an integer'  ##  Check if second is integer
    return (340.29 / 1000) * second ##  return the value of distance in second
print(distance(3))
print(distance(6))

print('\n')
print('Ex 3.35')
print()

import math
def points(x1, y1, x2, y2):
    assert isinstance(x1, int), 'x1 is not an integer number'
    assert isinstance(x2, int), 'x2 is not an integer number'
    assert isinstance(y1, int), 'y1 is not an integer number'
    assert isinstance(y2, int), 'y2 is not an integer number'
    z = pow((x2 - x1), 2) + pow((y2 - y1), 2) 
    return math.sqrt(z) ## return the square root => distance
print(points(0, 0, 1, 1))
print(points(0, 0, 0, 1))

print('\n')
print('Ex 3.44')
print()

import turtle
def polygon(sides):
    assert isinstance(sides, int), 'sides is not an integer'
    angles = int(((sides - 2) * 180) / sides)   ## calculate the angle should turn
    angles = 180 - angles
    s = turtle.Screen()
    t = turtle.Turtle() ## turtle screen pop up
    while sides > 0:    ## turtle graphics starts drawing
        t.forward(100)
        t.left(angles)
        sides = sides - 1
    s.exitonclick() ## end of the function
##polygon(4)
##polygon(12)

#
#
# Part (d)
#
#

print('\n')
print('Part (d)')
print()
print('\n')
print('Ex 3.32')
print()

def pay(wage, hour):
    if hour > 40:
        return ((hour - 40) * (wage * 1.5)) + (40 * wage)  ## calculate the total wage that people who work more than 40 hours
    else:
        return wage * hour ## calculate the total wage for those worked under 40 hours
print(pay(10, 10))
print(pay(10, 35))
print(pay(10, 45))

print('\n')
print('Part (d)')
print()

#
#
# Part (e)
#
#

print('\n')
print('Part (e)')
print()
print('\n')
print('Part (e1)')
print()

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RL = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
def restaurant_price(restaurant):
    assert isinstance(restaurant, (list, tuple))
    return restaurant.price
print(restaurant_price(RL[0]))

print('\n')
print('Part (e2)')
print()

RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
RC.sort(key = restaurant_price)
print(RC)

print('\n')
print('Part (e3)')
print()

def costliest(restaurant):
   restaurant.sort(key = restaurant_price, reverse = True)
   return restaurant[0].name
print(costliest(RC))

print('\n')
print('Part (e4)')
print()

def costliest2(restaurant):
   restaurant = sorted(restaurant, key = restaurant_price, reverse = True)
   return restaurant[0].name
print(RL)
print()
print(costliest2(RL))
print()
print(RL)

#
#
# Part (f)
#
#

print('\n')
print('Part (f)')
print()
print('\n')
print('Part (f1)')
print()

Book = namedtuple('Book', 'author title genre year price instock')
BSI = [
    Book("Leif H. Smith", "Sports Psychology For Dummies", "Sports", 1970, 10.00, 27),
    Book("Charles Austin Beard", "History of the United States", "History", 2013, 70.00, 75),
    Book("Deb Perelman", "The Smitten Kitchen Cookbook", "Cookbook", 1989, 30.00, 100),
    Book("Elke Linda Buchholz", "Art: A World History", "Art History", 1999, 20.00, 180),
    Book("Patricia H. Rushford", "Deadly Aim", "Mystery", 2004, 120.00, 17),
    Book("Ljubomir Perkovic", "Introduction to Computing Using Python: An Application Development Focus", "Technology",  2011, 80.00, 300) ]
def print_title(j):
    return BSI[j].title
j = 0
for i in BSI:
    print(print_title(j))
    j = j + 1
    
print('\n')
print('Part (f2)')
print()

def book_title(book):
    return book.title
def sort_title(BSI, m):
    BSI = sorted(BSI, key = book_title, reverse = False)
    return BSI[m].title
m = 0
for l in BSI:
    print(sort_title(BSI, m))
    m = m + 1

print('\n')
print('Part (f3)')
print()

i = 0
for j in BSI:
    temp_list = list(BSI[i])
    temp_list[-2] = BSI[i][-2]*1.1
    BSI[i] = tuple(temp_list)
    print(BSI[i][-2])
    i += 1

print('\n')
print('Part (f4)')
print()

k = 0
for i in BSI:
    if BSI[k][2] == "Technology":
        print(BSI[k][1])
    k = k + 1

print('\n')
print('Part (f5)')
print()

m = 0
list_before = []
list_after = []
list_before_string = ''
list_before_string += "More titles before 2000:\n"
list_after_string = ''
list_after_string += "More titles 2000 or later:\n"
for n in BSI:
    if BSI[m][3] < 2000:
        list_before.append(BSI[m][1])
        list_before_string += BSI[m][1]
        list_before_string += "\n"
    elif BSI[m][3] >= 2000:
        list_after.append(BSI[m][1])
        list_after_string += BSI[m][1]
        list_after_string += "\n"
    m += 1
##list_before.sort()
##list_after.sort()
print(list_before)
print(list_after)
print()
print(list_before_string)
print(list_after_string)

print('\n')
print('Part (f6)')
print()

def inventory_value(book):
    return book[4]*book[5]
def book_value(book):
    return book[-1]
j = 0
for i in BSI:
    temp = list(BSI[j])
    value = inventory_value(temp)
    temp.append(value)
    BSI[j] = tuple(temp)
    j += 1
def top_value(book):
    book = sorted(book, key = book_value, reverse = True)
    return book[0]
temp = []
temp = list(top_value(BSI))
print("The higest-value book is", temp[1], "by", temp[0], "at a value of $", temp[-1])

#
#
#Part (g)
#
#

print('\n')
print('Part (g)')
print()
import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(8.0)
def DrawEye (x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.left(120)
    t.circle(60,125) 
    t.left(56)
    t.circle(60,125) #Draw eye perimeter
    t.penup()
    t.seth(0)  
    t.goto(x-53,y-30)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(28,360)  #Draw iris
    t.end_fill()
    t.pendown()
    t.left(90)
    t.right(40)
    t.penup()
    t.forward(20)
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(16,360)
    t.end_fill()                    #Draw pupil
    t.seth(0)         #Reset tuttle orientation to 0

def DrawNose():
    t.penup()
    t.goto(-40,15)
    t.pendown()
    t.right(120)
    t.forward(100)
    t.circle(30,140)
    t.seth(0)

def DrawMouth():
    t.penup()
    t.color('red')
    t.begin_fill()
    t.goto(27,-170)
    t.left(145)
    t.pendown()
    t.circle(80,70)
    t.seth(0)
    t.left(145)
    t.circle(80,70)   #Draw upper mouth
    t.left(90)
    t.circle(110,112) #Draw lower mouth
    t.end_fill()
    


def DrawFace():
    DrawEye(-100,100,'brown')
    DrawEye(100,100,'brown')
    DrawNose()
    DrawMouth()

DrawFace()

s.exitonclick()


