# Pok On Cheng 74157306 and Derek Eang 91465975. ICS 31 Lab sec 5. Lab asst 1e.
print("Today is ", 2013, "/", 9, "/", 27)
print("We are taking ICS 31 Lab sec 5 now!")
print("Today is Friday!! LOL")
print("This assignment is actually done on Thursday.... Orz")

print("\nThe solution below is the answers of part (f).")

print("\nExercise 2.12:")
print("(a) The sum of the first seven positive integers")
print(1 + 2 + 3 + 4 + 5 + 6 + 7)
print(28)

print("\n(c) 2 to the 20th power")
print(2 ** 20)
print(1048576)


print("\n(e) The remainder when 4365 is divided by 61")
print(4365 % 61)
print(34)

print("\nExercise 2.13:")
s1 = '-'
s2 = '+'
print("s1 = '-'")
print("s2 = '+'")
print("\n(b) '-+-'")
print("'" + s1 + s2 + s1 + "'")

print("\n(e) '+--+--+--+--+--+--+--+--+--+--+'")
print("'" + (s2 + 10 * (s1+s1+s2)) + "'")

print("\nExercise 2.14:")
s = 'abcdefghijklmnopqrstuvwxyz'
print("s = 'abcdefghijklmnopqrstuvwxyz'")
print("\n'a'")
print("s[0]")
print("\n'z'")
print("s[25]")
print("\n'q'")
print("s[16]")

print("\nExercise 2.15:")
s = 'goodbye'
print("s = 'goodbye'")
print("\n(a) The first character of string s is 'g'")
print(s[0] == 'g')
print("True")

print("\n(c) The first two characters of s are 'g' and 'a'")
print(s[0] + s[1] == 'g' + 'a')
print("False")

print("\n(e) The middle character of s is 'd'")
print(s[3] == 'd')
print("True")

print("\n(g) The last chatacters of string s match the string 'tion'")
print(s[3] + s[4] + s[5] + s[6] == 't' + 'i' + 'o' + 'n')
print("False")

print("\nExercise 2.16:")
print("(a)Assign 6 to varia ble a and 7 to variable b")
a = 6
b = 7
print("a =", end = ' ')
print(a)
print("a = 6")
print("\nb =", end = ' ')
print(b)
print("b = 7")

print("\n(b) Assign to variable c the average of variable b")
c = (a + b) / 2
print("c =", end = ' ')
print(c)
print("c = 6.5")

print("\n(d) Assign to variables first, middle and last the strings 'John, 'Fitzgerald', and 'Kennedy'")
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
print(first)
print(middle)
print(last)

print("\n(e) Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately")
fullname = first + " " + middle + " " + last
print(fullname)

print("\nExercise 2.17:")
print("(a) The sum of 17 and -9 is less than 10.")
print((17 + (-9)) < 10)
print("True")

print("\n(c) c is no more than 24")
print(c < 24)
print("True")

print("\n(d) 6.75 is between the values of integers a and b")
print(a < 6.75 < b)
print("True")

print("\n(e) The length of string middle id larger than the length of string first and smaller than the length string last")
print(len(first) < len(middle) < len(last))
print("False")

print("\nExericse 2.21:")
print("Before reverse:")
s = ['t', 'o', 'p']
print(s)
print("s = 'top'")
print("\nAfter reverse:")
s.reverse()
print(s)
print("s = 'pot'")
