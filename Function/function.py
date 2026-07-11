# # 
# def greet (name,gender):
#     if gender=='Female':
#         print(f'Hello misss.{name}')
#     else:
#         print(f'Hello mr.{name}')
# greet('ram','male')



# # 
# def salaryIncr(salary):
#     salary+=5000
#     print('hiked salary:',salary)
#     return salary 
# hikedSal=salaryIncr(20000)
# print(hikedSal - 3000)


# # # 
# def square (x):
#     return x**2
# x=eval(input('enter the value'))
# a=square(x)
# print(f'the square of {x} is {a}')


        


###############################################################################################################################################

# #   Function example

#  # 1 waf to perform addition if a>b else perform subtraction
# def num(a,b):
#     if a>b :
#         print(a+b)
#     else:
#         print(a-b)
# num(100,20)


# # 
# def num(a,b):
#     if a>b :
#         return(a+b)
#     else:
#         return(a-b)
# # v=num(a,b)
# v=num(100,20)
# print(v)
                                                                 
                                                                 
# # 2 waf to check that the string is pallindrome or not take user input without using slicing
# def ispal(strr):
#     start=0
#     end=len(strr)-1  
#     while start < end:
#         if strr[start]!=strr[end]:
#             return 'Not pallindrome'
#         start+=1
#         end-=1 
#     return'Pallindrome'
# print(ispal('momo'))        


# # 3  waf to return the square, cube, square root, cube root of a value taken from user
# def value(x):
#     return x**2 , x**3, x*(0.5), x**(1/3)
# v=(value(eval(input('enter the value:'))))
# print(v)


# # # 4 "WAF to search for a particular character in a given string both of them should be taken from user as an argument and print the index of character."
# def check (strr,chrr):
#     for i in range (len (strr)):
#         if strr[i]==chrr:
#             return i
#     return -1
# res=check('malayalam','a')
# if res != -1:
#     print(res)
# else:
#     print('Not found in the given string')
    
    
# # 5 waf to take the square of all the elements present inside the list
# def num(x):
#     return [i**2 for i in x]
# x=eval(input('enter the value:'))
# v=num(x)
# print(v)


# # 6 waf to fetch the last digit of a number after performingthe addition of two number
# def last_digit_after_addition(a, b):
#     total = a + b
#     last_digit = total % 10
#     return last_digit
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result = last_digit_after_addition(a, b)
# print(f"The last digit of the sum of {a} and {b} is: {result}")


# # 7 waf to take 3 numbers from user and find the sum of first two and substract the third number from the result of addition
# def num(a,b,c):
#     return (a+b)-c
# a=eval(input('enter the value:'))
# b=eval(input('enter the value:'))
# c=eval(input('enter the value:'))
# v=num(a,b,c)
# print(v)


# # 8 waf to check that the given character is a special character alphabet or a digit without inbuilt function
# def char(x):
#     code = ord(x)
#     if 48 <= code <= 57:   
#         return 'digit'
#     elif (65 <= code <= 90) or (97 <= code <= 122):  # A-Z or a-z
#         return 'alphabet'
#     else:
#         return 'special character'
# ch = input("Enter a single character: ")
# result = char(ch)
# print(f"The character '{ch}' is a {result}.")
 

#######################################################################################################################

# # 1.Function to print Hello
# def name(a):
#     return a
# b=name('hello')
# print(b)


#2. Function to add two numbers
# def num(a,b):
#     return a+b
# b=num(5,6)
# print(b)


# # 3. Function to subtract two numbers
# def num(a,b):
#     return (a-b)
# c=num(100,20)
# print(c)
    

# # 4.Write a function to find the square of a number
# def squre(a):
#     return (a*a)
# c=squre(5)
# print(c)


# # 5.Write a function to find the cube of a number.
# def cube(a):
#     return(a**a)
# c=cube(3)
# print(c)


# # 6.Write a function to check whether a number is even or odd.
# def num(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'
# c=num(50)
# print(c)


# Write a function to check whether a number is positive or negative.
def num(a):
    if 0<=a<=9:
        return 'positive'
    else:
        return 'negative'
c=num(5)
print(c)