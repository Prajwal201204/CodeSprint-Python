
# if qution practis

# # a=10
# # print(a)

# a=eval(input('input value'))
# b=eval(input('input value'))
# c=eval(input('input value'))
# d=(a+b+c)/300*100
# print(d)

# ----------------------------------------------------------------------------------------------

# # if
# # 1)
# a=int(input('enter tha value'))
# if a%2==0:
#     print('even')
    
# # 2)     
# a=int(input('enter tha value'))
# if a==0:
#     print('zero')
    

# # 3) 
# a=int(input('enter tha value'))
# if a%3==0 and a%7==0:
#     print('divide by 3 and 7')


# # 4) 
# a=int(input('enter tha value'))
# if a>=10 and a<=20:
#     print ('between 10 and 20')

# # 5) 
# a=int(input('enter tha value'))
# if a%2==0 and a%3==1:
#     print('divide by 2 and not by 3')


# # 6) 
# a=int(input('enter tha value'))
# b=int(input('enter tha value'))
# c=int(input('enter tha value'))
# if a>b and a>c:
#     print(a)
# if b>a and b>c:
#     print(b)
# if c>a and c>b:
#     print(c)


# # 7)
# a=(input("enter tha value :"))
# if a in ('a','e', 'i', 'o', 'u'):
#     print('vowel')

# # 8)
# a=(input("enter tha value :"))
# if a not in  ('a','e', 'i', 'o', 'u'):
#     print('consonat')

# # 9
# a=int(input("enter tha value :"))
# b=int(input("enter tha value :"))
# if (a+b)>100:
#     print('greater than 100')


# # 10
# a=(input("enter tha value :"))
# if a[0]==a[-1]:
#     print('same number')


# # 11
# a=int(input("enter tha value :"))
# if 999>a>100 :
#     print('3 digit no')


# # 12 
# a=int(input("enter tha value :"))
# if a%5==0:
#     print(a)


# # 13) palindrome
# a=input('enter the value: ')
# rev=(a)[::-1]
# if a==rev:
#     print('palindrome')


# # 14) 31
# a=int(input('enter the value: '))
# b=int(input('enter the value: ')) 
# if (a+b)>100:
#     print('greater than 100')


# # 15) 33
# a=int(input('enter the value: '))
# b=int(input('enter the value: '))
# c=a-b
# if c < 0:
#     print('number is negative')

# # 16) 34
# a=int(input('enter the value: '))
# b=a**2
# if b>100:
#     print('grather than 100')

# # 17) 35
# a=int(input('enter the value: '))
# b=a**3
# if b%5==0:
#     print('divide by 5')

# # 18) 
# a=int(input('enter the value: '))
# b=int(input('enter the value: '))
# c=a+b
# if c%2==0:
#     print('even')

# # 19) 41
# a=int(input('enter the value: '))
# if 999>a>100:
#     print('3 digit no')

# # 20) 42
# a=(input('enter the value: '))
# if a[0]==a[-1]:
#     print('palandrom')
 

# .....................................................................................................


# else practise quation 

# # 1) 
# a=eval(input('enter the value: '))
# if type(a) in (list,set,dict):
#     print('mutable')
# else:
#     print('immutable')


# # 2) 
# a=eval(input('enter the value: '))
# if 0<a<9:
#     print('digit')
# else:
#     print('character')
    
    
# # 3)    
# a=(input('enter the value: '))
# if 'a'<=a<='z' or 'A'<=a<='Z' or '9'<=a<='0':
#     print('not a special char')
# else:
#     print('special char')

# # 4) 
# a=[10,20,30,40,50]
# if len(a)%2!=0:
#     print('middle value ')
# else:
#     print('not middle value')

# # 5) 
# a=(input('enter the value: '))
# if a[0]==a[-1]:
#     print('palandrom')
# else:
#     print('not palandrom')

# .............................................................................................

# elif qution 

# 1)
# a=(input('enter the value: '))
# if 'A'<=a<='Z':
#     print('uppercase')
# elif 'a'<=a<='z':
#     print('Lowercase')
# else:
#     print('special char')

# # 2) 
# a=int(input('enter the value: '))
# if 0<=a<=9:
#     print('single digit')
# elif 10<=a<=99:
#     print('2 digit')
# elif 100<=a<=999:
#     print('3 digit')
# else:
#     print('more digit')


# # 3
# a=int(input('enter the value: '))
# if a%3==0:
#     print('multiply by 3')
# elif a%5==0:
#     print('multiply by 5')
# elif a%3==0 and a%5==0:
#     print('multiply by 3 and 5')
# else:
#     print('not multiply 3 and 5')

# # 4)
# a=int(input('enter tha value'))
# b=int(input('enter tha value'))
# c=int(input('enter tha value'))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# # 5)
# a=int(input('enter tha value'))


# ..........................................................................................................

# nested if

# # 1)
# a=[10,20,30]
# if len(a)%2!=0:
#     mid=len(a)//2
#     if type(a[mid])==str:
#         print('middel value is string')
#     else:
#         print('middle value is not a string')
# else:
#     print('no middel value')


# # 2) 
# n=(input('enter tha value:'))
# if 'a'<=n<='z' or 'A'<=n<='Z':
#     if n in ('aeiouAEIOU'):
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('not character')


# # 3) 
# username=(input('enter tha value:'))
# if username=='admin':
#     password=(input('enter tha value:'))
#     if password=='admin123':
#         print('password is correct')
#         print('login sucess')
#     else:
#         print('incorrect password')
# else:
#     print('user not exist')



# ..........................................................................................

# while loop

# # 1)
# i=0
# while i<5:
#     print('prajwal')
#     i=i+1


# # 2)

# a=(input('enter tha value:'))
# i=0
# while i<=10:
#     print(i)
#     i+=1
    
    
# # 2)
# a=int(input('enter tha value:'))
# while 0<a:
#     print(a)
#     a-=1


# # 3
# n=int(input('enter tha value:'))
# i=1
# while i<=10:
#     print(f"{n} x {i} = {i*n}")
#     i+=1


# 4
# n=int(input('enter tha value:'))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i+=1
# print(sum)


# 5
# n=int(input('enter tha value:'))
# sum=1
# i=1
# while i<=n:
#     sum=sum*i
#     i+=1
# print(sum)


# # 6
# cha='ABCDEF'
# i=0
# while i<len(cha):
#     print(cha[i])
#     i+=1
    
    
# # 7)
# cha='ABCDEF'
# i=0
# while i<len(cha):
#     print(cha[i])
#     i+=2
# 
# 
# 
# cha='ABCDEF'
# i=0
# while i<len(cha):
#     if i%2==0:
#         print(cha[i])
#     i+=1 


# # 8)
# a='ASHDJWDjdsgdwi'
# i=0
# while i<len(a):
#     if 'a'<=a[i]<='z':
#         print(a[i])
#     i+=1



# # 9)factor
# n=int(input('enter tha value:'))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1
 
 

# # 10 Wap to convert binary to decinaml.
# binary = int(input("Enter binary number: "))
# decimal = 0
# base = 1
# while binary > 0:
#     digit = binary % 10
#     decimal = decimal + digit * base
#     base = base * 2
#     binary = binary // 10
# print(decimal) 
 
 
 
# # 11 Wap to get the following output.
# A = '10011100'
# B = '00110101'
# i = 0
# count = 0
# while i < len(A):
#     if A[i] == B[i]:
#         count += 1
#     i += 1
# print(count) 


# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# # For loop
# a={5,6,7}
# out=set()
# for i in a:
#     out.add(i+2)
# print(out)  

# # 1 Wap to print all the integers present in a list. 
# a=[10,20,30,'1','apple']
# for i in a:
#     if type(i)==int:
#         print(i)
    

# # 2 Wap to find the length of homogenous tuple without len(). 
# a=(10,20,30,10,20,30,'1','apple')
# count=0
# for i in a:
#     count+=1
# print(count)
        

# # 3 Wap to remove duplicates from list      
# a = [10, 20, 10, 30, 20, 40]
# new = []
# for i in a:
#     if i not in new:
#         new.append(i)
# print(new)


# # 4 Wap to extract all the even numbers present in a list. 
# a = [10, 25, 10, 31, 20, 40]
# for i in a:
#     if i%2==0:
#         print(i)


# # 5 Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers. 
# d = {'a': 10, 'b': 'hello',1: 20, 'c': 30}
# for i in d:
#     if type(i) == str and type(d[i]) == int:
#         print(i, d[i])



# # Wap to check whether the list is homogenous or not. 
# a = [10, 20, 30, 40]
# t = type(a[0])
# flag = True
# for i in a:
#     if type(i) != t:
#         flag = False
# if flag:
#     print("Homogeneous")
# else:
#     print("Not Homogeneous")
    

# # .Wap to replace the space by * present in a string 
# s = input("Enter string: ")
# result = ""
# for i in s:
#     if i == " ":
#         result = result + "*"
#     else:
#         result = result + i
# print(result)


# # . Wap to get the following output. 
# # S='always keep smiling' 
# # Out='syawla peek gnilims'
# s = "always keep smiling"
# words = s.split()
# result = ""
# for i in words:
#     result = result + i[::-1] + " "
# print(result) 


#  
# S=['jiocinema.com','file.py','web.html','amazom.com','www.org' ,'python.py']



############################################################################################
# ### function

# 1
# def add():
#     a=int(input('enter the value:'))
#     b=int(input('enter the value:'))
#     print(a+b)
# add()


# # 2
# def add(a,b):
#     print(a+b)
# m=int(input('enter the value:'))    
# n=int(input('enter the value:'))
# add(m,n)



############################################################################################
#  #################33function

# def add():
#     a=int(input('enter the value:'))
#     b=int(input('enter the value:'))
#     print(a+b)
# add()


# 
# def add(a,b):
#     print(a+b)
#     m=int(input('enter the value:'))    
#     n=int(input('enter the value:'))
#     return m+n,m*n,m-n
# print(add(20,30))
# # a,b,c=add()
# # print(a,b,c)


# # 1) Wap to check whether the number is strong or not. 
# def factorial(n):
#     fact=1
#     for i in range (1,n+1):
#         fact=fact*i
#     return fact
# def is_strong(n):
#     temp=n
#     sum=0
#     while n!=0:
#         ld=n%10
#         sum=sum + factorial(ld)
#         n=n//10
#     if sum==temp:
#         print('strong number')
#     else:
#         print ('not strong number')
# is_strong(145)



# # #
# def greet (func):
#     def inner (*args ,**kwargs):
#         print('welcome to my process')
#         func(*args,*kwargs)
#         print("thanks for using my program")
#     return inner

# @greet
# def add (a,b):
#     print(a+b)
# add(10,20)


##############################################################################################3
# # ###########  lambda
# # 1.
# strr=lambda x:'palindrome' if x==x[::-1] else 'not palindrome'
# print(strr('101'))

# # 2.
# num=lambda x: x*2 if x%2==0 else x**3
# print(num(5))



##############################################################################################
#######  Map
# # # 1. Use map() to square all numbers in the list: 
# sqr=lambda n : n**2
# lst=[1,2,3,4]
# res=map(sqr,lst)
# print(list(res)) 

# # 2. Use map() to convert a list of strings to uppercase: 
# words = ['apple', 'banana', 'cherry']
# result = list(map(str.upper, words))
# print(result)

# # 10. Combine first and last names using map(): 
# first_names = ['John', 'Jane', 'Alice']
# last_names = ['Doe', 'Smith', 'Johnson']
# result = list(map(lambda f, l: f + " " + l, first_names, last_names))
# print(result)

