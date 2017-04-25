# Pok On Cheng 7415 7306 and Thien-An Nguyen 30015827, ICS Lab 5. Lab Assignment 7.

#
#
# Part (c)
#
#

print()
print("Part (c)")
print()

print()
print("Part (c1) + (c3)")
print()

from random import choice
def random_names(num: int) -> list:
    ''' Reads the file and randomly chooses the name in format '''
    surnameWholeList = []
    surnameList = []
    firstnameWholeList = []
    firstnameList = []
    fullnameList = []
    infile1 = open('surnames.txt', 'r')
    for k in infile1:
        new_list = []
        new_list = k.split("\t")
        surnameWholeList.append(new_list)
    for i in surnameWholeList:
        surnameList.append(i[0]) # This one is for storing surnames only
    infile2 = open('malenames.txt', 'r')
    infile3 = open('femalenames.txt', 'r')
    for k in infile2:
        new_list = []
        new_list = k.split("\t")
        firstnameWholeList.append(new_list)
    for k in infile3:
        new_list = []
        new_list = k.split("\t")
        firstnameWholeList.append(new_list)
    for i in firstnameWholeList:
        firstnameList.append(i[0]) # This one is for storing firstnames only
    for i in range(num):
        surname = ""
        firstname = ""
        fullname = ""
        surname = choice(surnameList)
        firstname = choice(firstnameList)
        fullname = fullname + surname + ", " + firstname
        fullnameList.append(fullname)
    return fullnameList
for i in random_names(3):
    print(i)

print()
print("Part (c2)")
print()

allnames1 = random_names(1000)
allnames2 = []
for a in allnames1:
    new_list = a.split(", ")
    surname = ""
    firstname = ""
    fullname = ""
    for i in range(len(new_list)):
        if i == 0:
            surname = new_list[i].lower().capitalize()
        elif i == 1:
            firstname = new_list[i].lower().capitalize()
    fullname = surname + ", " + firstname
    allnames2.append(fullname)
#for i in allnames2:
    #print(i)

print()
print("Part D")
print()

print()
print("Part (d1)")
print()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_rotate(key: int) -> str:
    '''Return ALPHABET rotated forward or backwards according to key
    '''
    s = ''
    for i in ALPHABET:
        replace = ALPHABET.find(i)+key
        s+=ALPHABET[replace%26]
    return s
assert(alphabet_rotate(2)=='cdefghijklmnopqrstuvwxyzab')
assert(alphabet_rotate(27)=='bcdefghijklmnopqrstuvwxyza')
assert(alphabet_rotate(3)=='defghijklmnopqrstuvwxyzabc')

def Caesar_encrypt(message: str, key: int) -> str:
    '''Return message, encrypted using Caesar cipher; key indicates how far down the alphabet to
    substitute
    '''
    return message.lower().translate(str.maketrans(ALPHABET, alphabet_rotate(key)))
assert(Caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 1)=='bcdefghijklmnopqrstuvwxyza')
assert(Caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 27)=='bcdefghijklmnopqrstuvwxyza')
assert(Caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 50)=='yzabcdefghijklmnopqrstuvwx')

def Caesar_decrypt(message: str, key: int) -> str:
    '''Return message, decrypted using Caesar cipher; key indicates how far down the alphabet to
    substitute
    '''
    return message.lower().translate(str.maketrans(alphabet_rotate(key), ALPHABET))
assert(Caesar_decrypt('bcdefghijklmnopqrstuvwxyza', 1)==ALPHABET)
assert(Caesar_decrypt('bcdefghijklmnopqrstuvwxyza', 27)==ALPHABET)
assert(Caesar_decrypt('yzabcdefghijklmnopqrstuvwx', 50)==ALPHABET)


test = ""
text1 = ""
text2 = ""
text1 = Caesar_encrypt("dangerous", 3)
text2 = Caesar_encrypt("lifestyle", 5)
test = text1 + " " + text2
print(test)



def Caesar_break(text: str) -> str:
    ''' decrypts the message without key'''
    word = ""
    infile = open('wordlist.txt', 'r')
    infile_list = []
    for line in infile:
        infile_list.append(line.strip())
    for m in range(26):
        new_word = ""
        new_list = []
        new_word += Caesar_decrypt(text, m)
        new_list = new_word.split()
        for i in new_list:
            for l in range(len(infile_list)):
                if i == infile_list[l]:
                    word = word + i + " "
    return word
print(Caesar_break(test))
        
    
        
    
print()
print("Part E")
print()

def print_line_numbers (S: str, num: int, part: str) -> str:
    '''Print L, with a new line for each string and a line number with each string
    '''
    if part == "e2":
        line = "{:5d}: {}".format(num, S)
    elif part == "e3":
        line = "{}".format(S)
    return line

def stats(S: str):
    '''Print number of lines, empty lines, average characters per line, and average
    characters per non empty line for L
    '''
    empty = 0
    tot_char = 0
    for x in S:
        if x == "\n":
            empty+=1
        tot_char+=len(x)
    avg_char = tot_char/len(S)
    avg_charne = tot_char/(len(S)-empty)
    length = len(str(max([empty, tot_char, avg_char, avg_charne])))
    print('{:{width}} lines in the list'.format(len(S), width = length+1))
    print('{:{width}} empty lines'.format(empty, width = length+1))
    print('{:{width}.1f} average characters per line'.format(avg_char, width = length))
    print('{:{width}.1f} average characters per non-empty line'.format(avg_charne, width = length))

def copy_file(string: str):
    ''' copies the file with different strings '''
    if string == "line numbers":
        part = "e2"
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        count = 0
        for line in infile:
            lines = ""
            count += 1
            lines = print_line_numbers(line, count, part)
            outfile.write(lines)
        infile.close()
        outfile.close()
    elif string == 'Gutenberg trim':
        part = "e3"
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        count1 = 0
        for line in infile:
            lines = ""
            count1 += 1
            if count1 >= 19 and count1 <= 12694:
                lines = print_line_numbers(line, count1, part1)
            outfile.write(lines)
        infile.close()
        outfile.close()
    elif string == 'statistics':
        new_list = []
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        for line in infile:
            new_list.append(line)
            outfile.write(line)
        stats(new_list)
        infile.close()
        outfile.close()
    else:
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
    

copy_file("line numbers")
copy_file("Gutenberg trim")
copy_file("statistics")






