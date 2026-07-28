# # eligible to vote
# age=int(input('Enter the age:'))
# if age<0:
#     print('Not born yet')
# elif age<18:
#     print('NOT eligible')
# elif age>=18 and age<=50:
#     print(' eligible to vote')
# elif age>=50 and age<=80:
#     print('okay you are eligible to vote')
# elif age>80:
#     print('Take a rest')
# else:
#     print('invalid age') 


# # 1 wap to check the given character is uppercase/ lowercase/ digit/ special (without using inbuilt function)
# a=input('Enter the value:')
# if a>='A' and a<='Z':
#     print('uppercase')
# elif a>='a' and a<='z':
#     print('lowercase')
# elif a>'-9' and a<'9':
#     print('digit')
# else:
#     print('special')
    
    
# # 2 for a character if uppercase return lowercase if lowercase return uppercase  --> ORD , CHR
# a=input('Enter the value:')
# b=ord(a)
# if 65<=b<=90:
#     print('lowercase:',chr(b+32))
# elif 97<=b<=122:
#     print('uppercase',chr(b-32))
# else:
#     print('odd charter')


# # 3 wap to check a data is a collection/individual data type
# a=eval(input('Enter the value:'))
# # if a is (str,dict,tuple,list,bool,int,float):
# #     print('datatype')
# # if a is (type(str)):
# #     print('string')
# if type(a)==list:
#     print('list')
# elif type(a)==dict:
#     print('dictionary')
# elif type(a)==tuple:
#     print('Tuple')
# elif type(a)==set:
#     print('set')
# elif type(a)==str:
#     print('string')
# elif type(a)==int:
#     print('integer')
# elif type(a)==bool:
#     print('bool')
# else:
#     print('not data type')


# # 4 wap if input is string return its length, else if input is list pop element, else if input is tuple reverse else invalid input
# a=eval(input('Enter the value:'))
# if type(a)==str:
#     print('string',len(a))
# elif type(a)==list:
#     if a:
#         b=a.pop()
#         print('poped elemen:',b)
#         print('Ramaining list:',a)
#     else:
#         print('list is empty,nothing is pop')
# elif type(a)==tuple:
#     print('reverse',a[::-1])
# else:
#     print('invalid input')
        

# # 5 wap to check that the given number is a single digit, double digit or a triple digit
# a=int(input('Enter the value:'))
# if 0<=a<=9:
#     print('single digit')
# elif 10<=a<=99:
#     print('duble digit')
# elif 100<=a<=999:
#     print('triple digit')
# else:
#     print('different digit')


# # 6 wap to check that the given data is of which individual datatype
# a=eval(input('Enter the value:'))
# if type(a)==int:
#     print('integer')
# elif type(a)==str:
#     print('string')
# elif type(a)==complex:
#     print('complex')
# elif type(a)==float:
#     print('float')
# elif type(a)==bool:
#     print('boline')
# else:
#     print('collection data type')


# # 7 Wap to check a age belongs to which category 0 to 17 child and 18 to 30 adult, 31 to 60 men , 61 to 100 senior citizen, else invalid
# a=eval(input('Enter the value:'))
# if 0<=a<=17:
#     print('child')
# elif 18<=a<=30:
#     print('adult')
# elif 31<=a<=60:
#     print('men')
# elif 61<=a<=100:
#     print('senior citize')
# else:
#     print('invalid')


# # 8 wap to check which is smallest value among 3 numbers
# a=65
# b=34
# c=76
# if a<b and a<c:
#     print(a)
# elif b<c:
#     print(b)
# else:
#     print(c)


# # 9 wap to take marks of 5 sub, calculate the average if the average if the average is b/w90-100 print distinction if 75-85 print first class and if it's 60-74 print third class, below 50 fail . 
# a=50
# b=56
# c=70
# d=80
# e=90
# avg=a+b+c+d+e
# print(avg)
# avg=avg/5
# print(avg)
# if 90<=avg<=100:
#     print('Distinction')
# elif 75<=avg<=89:
#     print('First class')
# elif 60<=avg<=74:
#     print('Second class')
# elif 50<=avg<=59:
#     print('Third class')
# else:
#     print('Fail')



# # 10 wap to check the is uppercase or lowercase or digit or special character (using inbuilt function)
# a=input('Enter the value:')
# if a.isupper():
#     print(f'{a} is a uppercase')
# elif a.islower():
#     print(f'{a} is a lowercase')
# elif a.isdigit():
#     print(f'{a} is a digit')
# else:
#     print(f'{a} is a specieal character')
    

# # 11 wap to check that tha last character of the given string is special character or not [no inbuilt fuction ]
# a=(input('Enter the value:'))
# b=a[-1]
# c=ord(b)
# if 65<=c<=90 or 97<=c<=122 or 48<=c<=57:
#     print('not special character')
# else:
#     print('special character')


# # 12 egt the last digit of a number and check its even or odd without typecasting and indexing | slicing
# a=eval(input('Enter the value:'))
# # a=[2,4,6,7,9,1,5] 
# b=a[-1]
# if b%2==0:
#     print(f'{b} is even')
# else:
#     print(f'{b} is odd')
    

# # 13. Wap to check whether the data is mutable or not. 
# data=eval(input('Enter The value:'))
# if type(data) in (list,dict,set):
#     print('mutable')
# else:
#     print('not mutable')        


# # 14. Wap to check whether the given character is digit or not.
# cha=(input('Enter The value:'))
# if '0'<=cha<='9':
#     print('digit')
# else:
#     print('charther')


# # 15. Wap to check whether the given character is special or not. 
# cha=(input('Enter The value:'))
# if 'a'<cha<'z' or 'A'<cha<'Z' or '0'<cha<'9':
#     print('not special character')
# else:
#     print('special character')


# # 16. Wap to check whether a list consists of middle value or not.
# # num=int(input('Enter The value:'))
# num=[1,2,3,8,4,5]
# if len(num)%2!=0:
#     print('middel value')
# else:
#     print('not middel value')


# # 17. Wap to check whether the number is even or odd. 
# num=int(input('Enter The value:'))
# if num%2==0:
#     print('even')
# else:
#     print('odd')


# # 18. Wap to check whether the given data is mutable or immutable. 
# data=eval(input('Enter The value:'))
# if type(data) in (list,dict,set):
#     print('mutable')
# else:
#     print('immutable') 


# # 19. Wap to check whether 2 values are pointing to the same memory or not.
# a=int(input('Enter The value:'))
# b=int(input('Enter The value:'))
# if a is b:
#     print('same memory')
# else:
#     print('not same memory')


# # 20. Consider a tuple of length 2 and check whether the tuple is homogenous or not.
# a=('a','b')
# if type(a[0])==type(a[1]):
#     print('homogenous') 
# else:
#     print('not homogenous')


# # 21. Wap to check whether the string is palindrome or not. 
# cha=(input('Enter The value:'))
# if cha[0]==cha[-1]:
#     print('palandrom')
# else:
#     print('not palandrom')


# # 22. Wap to check whether the number is positive or negative.
# num=(input('Enter The value:'))
# if '0'<=num<='9':
#     print('positive no')
# else:
#     print('negative no')


# # 23. Wap to check whether the char is uppercase, lowercase, digit or special char. 
# num=(input('Enter The value:'))
# if  'A'<=num<='Z':
#     print('uppercase')
# elif 'a'<=num<='z':
#     print('lowercase')
# elif '0'<=num<='9':
#     print('digit')
# else:
#     print('specieal character')


# # 24. Wap to check whether the given integer is single digit or two digits or three digits or more than three digits. 
# num=int(input('Enter The value:'))
# if 0<=num<=9:
#     print('singel digit')
# elif 10<=num<=99:
#     print('2 digit')
# elif 100<=num<=999:
#     print('3 digit')
# else:
#     print('more than 3 digit')


# # 25.Wap to check the given points are lying in which quadrant. 
# x = int(input("Enter x coordinate: "))
# y = int(input("Enter y coordinate: "))
# if x > 0 and y > 0:
#     print("1st Quadrant")
# elif x < 0 and y > 0:
#     print("2nd Quadrant")
# elif x < 0 and y < 0:
#     print("3rd Quadrant")
# elif x > 0 and y < 0:
#     print("4th Quadrant")
# else:
#     print("Point lies on X-axis, Y-axis, or Origin")


# # 26. Wap to find the greatest of 3 numbers. 
# a=int(input('Enter The value:'))
# b=int(input('Enter The value:'))
# c=int(input('Enter The value:'))
# if a>c and a>b:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)


# # 27. Wap to find the smallest of 3 numbers. 
# a=int(input('Enter The value:'))
# b=int(input('Enter The value:'))
# c=int(input('Enter The value:'))
# if a<c and a<b:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else:
#     print(c)


# # 28. Wap to check the relation between two integer numbers. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("First number is greater")
# elif a < b:
#     print("First number is smaller")
# else:
#     print("Both numbers are equal")


# # 29. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, if it is digit print the reminder when  it is divided by 3 else if it is special character print it’s ASCII value. 
# a=(input("Enter first number: "))
# if 'a'<=a<='z':
#     print(chr(ord(a)-32))
# elif 'A'<=a<='Z':
#     print(chr(ord(a)+32))
# elif '0'<=a<='9':
#     print(int(a)%3)
# else:
#     print(ord(a))


# # 30. Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5. 
# num=int(input('Enter the value: '))
# if num%3==0 and num%5==0:
#     print('buzzfizz')
# elif num%5==0:
#     print('buzzz')
# elif num%3==0:
#     print('fizzz')
# else:
#     print("Neither Fizzz nor Buzzz")
