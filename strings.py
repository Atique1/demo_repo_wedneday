# strings = ordered, immutable, text representation

# a string is with single or double quotation mark
my_string = 'hello world'

# escaping baxkslash \ will ignore single quote within string
my_string2 = 'I\'m a programmer.'

# triple quotation mark is use for multi line string or documentation.
my_string3 = '''This is a 
triple quotation mark and can be 
use for multiline purposes or documentation'''
print (my_string3)

my_string4 = '''123456789 is a \
triple quotation mark and can be \
use for multiline purposes or documentation''' # \ is use for not creating new line
print (my_string4)

# access character from a strings
a_char = my_string4[43]
print (a_char)
b_char = my_string4[-2]
print (b_char)
# my_string4[0] = 't' => it is not possible because string is immutable

# access substring from a strings
substring_my_string4 = my_string4[3:20] # 3 is strat index and 20 is stop index
print (substring_my_string4)

substring_my_string5 = my_string4[:] # this is one way of copy original string
print (substring_my_string5)

substring_my_string6 = my_string4[::3] # this is step index, by default it takes every char. 2 is for every other char
print (substring_my_string6)

substring_my_string7 = my_string4[::-1] # it will reverse the whole string with ::-1 this slicing operator
print (substring_my_string7)

# concatinate (join) 2 strings
greetings = 'Hello'
name = 'Atique'
sentence = greetings + ' ' + name
print (sentence)

# iterate string with for loop
for i in my_string4:
    print (i)

# find a char or words from a string
if 'cx' in my_string4:
    print ('yes')
else:
    print ('no')

# remove the whitespace or ohter unwanted char from a string
a_string_with_whitespace = '   I a\'m a programmer    '
print (a_string_with_whitespace)

a_string_without_whitespace = a_string_with_whitespace.strip()
print (a_string_without_whitespace)

# since string is immutable, we can assign string with base string
a_string = '   This is a string with white space     '
a_string = a_string.strip()
print (a_string)

# uppercase, lowercase, starts with, ends with
print (a_string.upper())
print (a_string.lower())
print (a_string.startswith('This'))
print (a_string.endswith('e'))

# find index of a character or substring in string, count number of specific char,  
print (a_string.index('string'))
print (a_string.index('p'))
print (a_string.find('w'))
print (a_string.count('t'))

# replace char or word from a string. REMEMBER it will not change the original string because it is immutable
print (a_string.replace('space','*****'))
print (a_string)

# converts string into lists
my_string5 = 'how are you doing?'
my_list = my_string5.split() # by default delemeter is space
print (my_list)

my_list2 = my_string5.split('o') # here delemere is o
print(my_list2)

my_string5 = 'how,are,you,doing?'
my_list = my_string5.split(',') # here delemeter is , 
print (my_list)

# converts lists into strings (Very very important)
my_string5 = 'how,are,you,doing?'
my_list = my_string5.split(',') # here delemeter is , 
print (my_list)
new_my_string5 =' '.join(my_list) # concatinates lists element to strings. within these 2 single quotes we can set the contraints. for example, ' ', '.', '#' etc
print(new_my_string5)

# converting lists into strings with more options - BAD WAYS and GOOD WAYS
aa_lists = ['a']*6
print (aa_lists)
    ##### BAD Approach ####
aa_string = ''
for i in aa_lists:
    aa_string +=i
print (aa_string)
    ##### GOOD Approach ####
aa_string = ''.join(aa_lists)
print (aa_string)

# To check the perfomance of previous 2 ways -
from timeit import default_timer as timer
aa_lists = ['a']*1000000
# print (aa_lists)
    ##### BAD Approach ####
start = timer()
aa_string = ''
for i in aa_lists:
    aa_string +=i
stop = timer()
print (stop - start)
    ##### GOOD Approach ####
start = timer()
aa_string = ''.join(aa_lists)
stop = timer()
print (stop-start)

# Format string - there are 2 ways to fromat string - either using % or using .format() or f-Strings
var = 'Tom'
my_string6 = 'the variable is %s' % var # by that means that we have a place holder with a sting (%s) here and after that we filled the placeholere with our variable (var) 
print (my_string6)

var = 3
my_string6 = 'the variable is %d' % var # for integer we use d instead of s
print (my_string6)

var = 3.1416
my_string6 = 'the variable is %f' % var 
print (my_string6)

# modern formatting method
var = 'Tom'
my_string6 = 'the variable is {}'.format(var)  # {}'.format
print (my_string6)

var = 5.2738
var2 = 6
my_string6 = 'the variable is {:f} and {}'.format(var,var2)  # {}'.format() with float and integer
print (my_string6)

# newest way to do the above tasks
var = 'Tom'
my_string6 = f'the variable is {var}'  # f
print (my_string6)

var = 5.2738
var2 = 6
my_string6 = f'the variable is {var*2} and {var2}'  # with f-Strings we can also use mathametical operations also
print (my_string6)




# print (len(a_string))
# for i in range(len(a_string)):
#     print (i, ' => ', a_string[i])
