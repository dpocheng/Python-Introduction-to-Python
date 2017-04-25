# Pok On Cheng 74157306 and Christina Pearl Wang 66561706. ICS 31 Lab sec 5. Lab asst 5.

#
#
# Part (f)
#
#

print("\n")
print("Part (f)")
print(" ")

__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 sp: Search the collection for selected restaurants by price
 p:  Print all the restaurants
 m:  Enter the Menu_enter program
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='sp':
            n = float(input("Please enter the price of dish to search for: "))
            for r in Collection_search_by_price(C, n):
                print(Restaurant_str(r))
        elif response=='m':
            Menu_enter()
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_search_by_price(C: list, price: Restaurant) -> list:
    """ Return list of Restaurants with  prices at or below a specified value
    """
    result = [ ]
    for r in C:
        if r.price <= price:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

### Dish
Dish = namedtuple('Dish', 'name price calories')

def Dish_str(ds: Dish) -> Dish:
    return ds.name + " ($" + str(ds.price) + "): " + str(ds.calories) + " cal"

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the name of dish: "),
        float(input("Please enter the price of dish: ")),
        int(input("Please enter the calories of dish: ")))

## Menus

def Menu_enter():
    print("Welcome to the Menu_enter program!")
    handle_commands1()
    #print("\nThank you.  Good-bye.")

MENU1 = """
Do you want to add a Dish?
 yes:  Add a new dish
 no:   Return the completed list of Dishes
 c:    Change prices for the dishes served
"""

def handle_commands1():
    """ Display menu, accept and process commands.
    """
    string = ""
    C = Collection_new()
    while True:
        response = input(MENU1)
        if response=="yes":
            d = Dish_get_info()
            C.append(d)
            string = string + Dish_str(d) + "\n"
        elif response=='no':
            print(string)
            return string
        elif response=='c':
            number = int(input("Please enter the percentage you want to change: "))
            string = ""
            for i in range(len(C)):
                new_price = C[i].price
                new_price = new_price * (1 + (number / 100))
                C[i] = C[i]._replace(price = new_price)
                string = string + Dish_str(C[i]) + "\n"
        else:
            invalid_command(response)

restaurants()
#Menu_enter()
