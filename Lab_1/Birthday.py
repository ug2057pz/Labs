''' January,10,2023 Capstone Class
Part 1: Hello, birthday month

Write a program that asks for your name and the month you were born in.

Then, your program should print
A greeting to you, using your name
A message with the number of letters in your name
A 'Happy birthday month!' message if you were born in the current month
Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.'''

name = input('Please enter your name:') #ask user to enter their name
birth_month = input('Please enter the name of the month you were born in :') #ask user for their birth month
print(f'Hello + {name}')
print('You have {0} letters in your name'.format(len(name))) #print the nuumber of letters
if birth_month == 'January':
    print('Happy birthday month!')
else:
        print('End of the program!')
'''Part 2: List of classes

Write a program that asks for the names of all of the classes you are taking this semester
Save these class names in a list.
Print all the items in the list, one per line.'''