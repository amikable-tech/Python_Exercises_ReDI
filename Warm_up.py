#1. print hello world
c = 'Hello World'
print(c)

#2 Ask the user for their name and output “Hello“ and the name that has been input
name = input('What is your name?\n')
print('Hi' , name)

#3 Get two numbers from the user and add them together
num1 = input('give a number')
num2 = input('give another number')
num1 = int(num1)
num2 = int(num2)
result = num1 + num2
print(result)

#4 Write a program that outputs all numbers from 1 to 10
i = 1
while i <= 10:
    print("i is:", i)
    i += 1 


#5 write a program that outputs all numbers from 1 to a number that the user has set
i = 1
num = int(input('limit'))
while i <= num:
    print("i is:", i)
    i += 1 

#6 Write a program that outputs all numbers from 1 to 10 in steps of two
i = 1
while i <= 10:
    print("i is:", i)
    i += 2

# 7. Write a program that outputs all fruits inside the list of fruits = [“apple”, “banana”, “pear”]
fruits = ['apple', 'banana', 'pear']
for fruit in fruits:
    print('this is a fruit:',fruit)
    
# 8. Get a string from the user and then reverse the string and output it
txt = input('what would you like to reverse? ' )[::-1]
print(txt)

#9. Get two numbers a and b from the user. Tell the user which number is bigger, or if they are the same
num1 = int(input('give a number'))
num2 = int(input('give another number'))
if num1 > num2:
    print("{0} is greater than {1}".format(num1, num2))
elif num1 == num2:
    print("{0} is equal to {1}".format(num1, num2))
else:
    print("{0} is less than {1}".format(num1, num2))

#10. Get a word as input from the user. Find out how many characters there are in the word and tell the user that number
text = str(input('Please input a word ' ))
len(text)
print(len(text))