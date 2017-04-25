#Christina Wang 66561706, Thien-An Nguyen 30015827, ICS 31 Lab sec 5.  Lab asst 6.

print("-----------Part c-----------")


print('----Part (C.1)----')
print()

from random import randrange
for i in range(50):
    print (randrange(1,11))

print()

for i in range(50):
    print (randrange (1,7))

print('----Part (C.2)----')
print()

def roll2dice():
   ''' Returns a number reflecting the random roll of two dice.
   '''
   return randrange(1,7) + randrange(1,7)
for i in range(50):
    print(roll2dice())
    
print()

print("-----------Part c.3-----------")
def distribution_of_rolls(n: int):
    ''' Takes the number of times to roll two dice and prints the distribution of
        values of those rolls
    '''
    print('Distribution of dice rolls\n')
    s = ''
    for y in range(n):
        s+= (str(roll2dice()) + ' ')
    for x in range(2,13):
        count= 0
        for i in s.split(' '):
            if i == str(x):
                count+=1
        print('{:2}:{:6} ({:4.1f}%)  '.format(x, count, (count/n)*100)+str(count*'*'))
    print('-----------------------------\n'+'{:11} rolls'.format(n))
distribution_of_rolls(200)
print()

print("-----------Part D-----------\n")


print("-----------Part d.1-----------")
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

assert(Caesar_decrypt((Caesar_encrypt('abcdefghijklmnopqrstuvwxyz', 1000)), 1000)=='abcdefghijklmnopqrstuvwxyz')

print(Caesar_encrypt('the cat crawled up the ladder', 7))
print(Caesar_decrypt('aol jha jyhdslk bw aol shkkly', 7))

print()
print("-----------Part d.2---------")
Anthony = 'I was running a bit late to class today.'
Christina = 'Today is Wednesday.'

print(Anthony)
print(Caesar_encrypt(Anthony, 2))
print(Caesar_decrypt('k ycu twppkpi c dkv ncvg vq encuu vqfca.', 2))

print()

print(Christina)
print(Caesar_encrypt(Christina, 5))
print(Caesar_decrypt('ytifd nx bjisjxifd.', 5))
print()

print("-----------Part e-----------\n")

print("-----------Part e.1-----------")
lst = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "engaged in a great civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure."]
testlst = ['The day was very windy when I decided to leave class.',
           'It was neither fall nor winter but the air was chilly.',
           'I had to put on my light coat before I began to feel the air inside.']

def print_line_numbers (L: list):
    '''Print L, with a new line for each string and a line number with each string
    '''
    count = 0
    length = len(str(len(L)))
    for i in L:
        count+=1
        print('{:{width}}:  {}'.format(count, i, width = length))
print_line_numbers(lst)
print('\n')
print_line_numbers(testlst)
print('\n\n')


print("-----------Part e.2-----------")
def stats(L: list):
    '''Print number of lines, empty lines, average characters per line, and average
    characters per non empty line for L
    '''
    empty = 0
    tot_char = 0
    for x in L:
        if x == '':
            empty+=1
        tot_char+=len(x)
    avg_char = tot_char/len(L)
    avg_charne = tot_char/(len(L)-empty)
    length = len(str(max([empty, tot_char, avg_char, avg_charne])))
    print('{:{width}} lines in the list'.format(len(L), width = length+1))
    print('{:{width}} empty lines'.format(empty, width = length+1))
    print('{:{width}.1f} average characters per line'.format(avg_char, width = length))
    print('{:{width}.1f} average characters per non-empty line'.format(avg_charne, width = length))
stats(lst)
stats(testlst)
print()

print("-----------Part e.3-----------")
def list_of_words(L: list) -> list:
    '''Print L as list of words without punctuation
    '''
    result = [ ]
    words = ''
    check = ',.:;?!()[]{}\/-'
    for i in L:
        words+=i+' '
    temp = words.split()
    for i in temp:
        temp_word = ''
        for j in i:
            count = 0
            for k in check:
                if k != j:
                   count+=1
            if count == len(check):
                  
               temp_word+=j
        result.append(temp_word)
    return result

quote = ['The man went to the grocery store to buy food because he was hungry.',
         'He did not know what to eat so he bought some pizza.']
quote2 = ['John did not expect the class to be so hard.',
          'He had no idea how much time he would have to study.']

assert(list_of_words(lst)==['Four', 'score', 'and', 'seven', 'years', 'ago', 'our',
                            'fathers', 'brought', 'forth', 'on', 'this', 'continent',
                            'a', 'new', 'nation', 'conceived', 'in', 'liberty', 'and',
                            'dedicated', 'to', 'the', 'proposition', 'that', 'all', 'men',
                            'are', 'created', 'equal', 'Now', 'we', 'are', 'engaged', 'in',
                            'a', 'great', 'civil', 'war', 'testing', 'whether', 'that','nation',
                            'or', 'any','nation', 'so', 'conceived', 'and', 'so', 'dedicated',
                            'can', 'long', 'endure'])
assert(list_of_words(quote) == ['The', 'man', 'went', 'to', 'the', 'grocery', 'store',
                                'to', 'buy', 'food', 'because', 'he', 'was', 'hungry',
                                'He', 'did', 'not', 'know', 'what', 'to', 'eat', 'so',
                                'he', 'bought', 'some', 'pizza'])

print(list_of_words(quote2))
