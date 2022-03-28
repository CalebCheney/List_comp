''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
import abc
from operator import truediv
from sre_parse import SPECIAL_CHARS


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_evennum = list(filter(lambda num: num % 2 == 0, numbers)) #dont know
filtered_oddnum = list(filter(lambda num: num % 2 == 1, numbers))
print(filtered_evennum) 
print(filtered_oddnum)




''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

six_char_days = list(filter(lambda day: len(day) == 6, weekdays))
print(six_char_days)







''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']

filtered_colors = list(filter(lambda color: color is not 'black' and color is not 'orange', colors))

print(filtered_colors)









''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list = list(filter(lambda num: num not in list2, list1))
print(new_list)



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
more_colors = ['red', 'black', 'white', 'green', 'orange']

ack_list = list(filter(lambda word: 'ack' in word, more_colors))
print(ack_list)
abc_list = list(filter(lambda word: 'abc' in word, more_colors))
print(abc_list)





''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
#string = 'Helloword1' #10 characters



password = input('Enter Password:')
    

upper = lambda word: word.isupper()
lower = lambda word: word.islower()
num = lambda word: word.isdigit()
lenght = lambda word: word >= 8




print(any(filter(upper, x)==))


'''
password_var = list(filter(lambda password: len(password) >= 8 in string, string))

if password_var == True:
    valid_list.append(True)
else:
    valid_list.append(False)
print(password_var)
print(valid_list)
'''





''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
