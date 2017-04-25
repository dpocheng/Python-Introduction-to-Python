# Pok On Cheng 74157306 and Masanori Uehara 57654039. ICS 31 Lab sec 5. Lab asst 6.

#
#
# Part (c)
#
#

print()
print("Part (c)")
print()

print()
print("Part (c1)")
print()

from random import randrange
for i in range(50):
    print(randrange(11))
for i in range(50):
    print(randrange(1,7))

print()
print("Part (c2)")
print()

def roll2dice() -> int:
    j = randrange(1,7)
    k = randrange(1,7)
    return j + k

for i in range(50):
    print(roll2dice())

print()
print("Part (c3)")
print()

def distribution_of_rolls(num: int):
    print("Distribution of dice rolls")
    new_list = []
    for i in range(num):
        new_list.append(roll2dice())
    for i in range(2,13):
        print("{0:2}: {1:>4} {2:>8.2f}%   ".format(str(i),new_list.count(i), new_list.count(i)/len(new_list)*100), new_list.count(i)*"*")
    print("---------------------------------------------------")
    print("     " + str(num) + " rolls")
distribution_of_rolls(200)

#
#
# Part (d)
#
#

print()
print("Part (d)")
print()

print()
print("Part (d1)")
print()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def Caesar_encrypt(plaintext: str, key: int) -> str:
    key = key % 26
    traslation_table = str.maketrans(ALPHABET, ALPHABET[key:] + ALPHABET[:key])
    return plaintext.lower().translate(traslation_table)

def Caesar_decrypt(ciphertext: str, key: int) -> str:
    key = key % 26
    traslation_table = str.maketrans(ALPHABET, ALPHABET[-key:] + ALPHABET[:-key])
    return ciphertext.lower().translate(traslation_table)
testStr = "this is test Text."
print(Caesar_encrypt(testStr, 3))
print(Caesar_encrypt(Caesar_decrypt(testStr, 3),3))

print()
print("Part (d2)")
print()

masaCipher = "pq, ug vium qa uiai. vqkm bw ummb gwc :)" # key is 8
print(Caesar_decrypt(masaCipher, 8))
messageP = "xubbe, rktto! dysu je cuuj oek yd ksy" # key is 10
print(Caesar_encrypt(messageP, 10))

print()
print("Part (d3)")
print()

print(Caesar_encrypt(testStr, 29))
print(Caesar_encrypt(Caesar_decrypt(testStr, 29),29))

#
#
# Part (e)
#
#

print()
print("Part (e)")
print()

e1text = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

print()
print("Part (e1)")
print()

def print_line_numbers(lst: list):
    for i in range(len(lst)):
        print("{0:3}: {1:}".format(str(i+1), lst[i]))
print_line_numbers(e1text)

print()
print("Part (e2)")
print()

def stats(lst: list):
    empty = 0
    lines = 0
    totalChar = 0
    for line in lst:
        lines += 1
        totalChar += len(line)
        if not line:
            empty += 1
    print("{0:5}    lines in the list".format(lines))
    print("{0:5}    empty lines".format(empty))
    print("{0:7.1f}  average characters per line".format(totalChar/lines))
    print("{0:7.1f}  average characters per non-empty line".format(totalChar/(lines-empty)))
stats(e1text)

print()
print("Part (e3)")
print()

def list_of_word(lst: list) -> list:
    new_list = []
    for line in lst:
        new_string = ""
        for i in range(len(line)):
            if line[i] in "'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                new_string += line[i]
            else:
                new_string += " "
        new_string = new_string.split()
        new_list.extend(new_string)
    return new_list
print(list_of_word(e1text))
