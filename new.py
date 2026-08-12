# # 1 
# # without enumerate
# ls=['google','mapple','apple','python']
# newls={i:ls[i] for i in  range(len(ls))}
# print(newls)

# # with enumerate
# ls=['google','mapple','apple','python']
# newls={i:word for i, word in enumerate(ls)}
# print(newls)



# # 2 wap to create a dictionary having first character of eath word and word pair if word having even length fo
# ls=['google','mapple','apple','python']
# newls={i ls[0]:ls[i] for i in range(len(ls))}
# print(newls)

# # 1 
# # without enumerate
# ls=['google','mapple','apple','python']
# newls={i:ls[i] for i in  range(len(ls))}
# print(newls)


####################################################################################################



# list comprihrnshien

# #1
# ls=[10,20.90,(10,20,30),'hello']
# newls=[i[::-1] if type(i) in [list,tuple,set,str] else i**2 for i in ls]
# print(newls)




# 2 WAP to check that the length of the names stored inside the list is even or odd. If even reverse it and append. else append its length only.
# names = ["Alice", "Bobo", "Charlie", "David",'omie']
# ls=[]
# for i in names:
#     if len(i)%2==0:
#         ls.append (i[::-1])
#     else:
#         ls.append(i)
# print(ls)

# 
# ls=[i[::-1] if len(i)%2==0 else len(i) for i in names]
# print(ls)


# #  3  WAP to find the square of all the numbers between 1 to 50 if that number is divisible by 5.
# ls=[ i**2  for i in range(1,50) if i%5==0  ]
# print(ls)


# # # 4 WAP to get the following output:
      # # s = 'python is very easy'
      # # out = [(python, 6), (is, 2), ...] 
# s = 'python is very easy'
# lo=[]
# word=s.split()
# for i in word:
#     lo.append((i,len(i)))
# print(lo)

# s = 'python is very easy'
# lo=[(i,len(i)) for i in s.split()]
# print(lo)


# # # 5 WAP to extract all the even numbers from a given collection.
# s=[1,2,3,4,5,6,7,8,9,22,3,44,53,234,24,3634,635,23,5,34,5,3,452]
# ls=[i for i in s if i%2==0]
# print(ls)


# # 6 WAP to create a list which contains 10 multiples of 2.
# ls=[i*2 for i in range(1,11) ]
# print(ls)


# 7 WAP to create a list that contains the sum of same‑indexed values of two lists taken from user as input with and without zip() function.  
# a=[10,20,30,40]
# b=[1,2,3,4]
# c=[]
# for i in range (len(a)):
#       c.append((a[i]+b[i]))  
# print(c)

# #
# a=[10,20,30,40]
# b=[1,2,3,4]
# c=[a[i]+b[i] for i in range(len(a)) ]
# print(c)

###############################################################

# set
# # WAP to remove repeated values from a list and return in a set.
# s=[1,2,3,4,2,1]
# d={s[i] for i in range (len(s))}  
# print(d)  

# 2. WAP to get only the palindrome strings from a list and there should be no duplicates in the final output.
# s = ["madam", "racecar", "apple", "hello", "madam", "noon", "level", "world", "noon"]
# a={i for i in s if i==i[::-1]}
# print(a)




##################################################################################################

# dict

# 1 WAP to create a dictionary of values and index pairs with and without enumerate() function.

# without enumerate()
# a=['google',' mapple', 'apple', 'python', 'orange']
# b={i:a[i] for i in range(len(a))}
# print(b)

# with enumerate()
# a=['google',' mapple', 'apple', 'python', 'orange']
# b={i:j for i,j in zip(range(len(a)), a)}
# print(b)

















# #########################################################3

# map

# # 1 use map() to convert a list of strings to uppercase:
# # out=words=['apple','banana','cherry']
# word=['apple','banana','cherry']
# uppers=map(lambda x:x.upper(),word)
# print(list(uppers))


# 2

# # 3 add two lists element-wise using map():
# a=[1,2,3]
# b=[4,5,6]
# c=map(lambda x,y:x+y,a,b)
# print(list(c))


# # 5 use map() to multiply each element by its index:
# nums=[10,20,30,40]
# def mul(n):
#       return n*nums.index(n)
# var=map(mul,nums)
# print(list(var))

# # 6 convert a list of temperatures in celsius to fahrenheit using map();
# a=[0,20,37,100] 
# print(list(map(lambda x:x*(9/5)+32, a)))

# # 8 Given a list of strings containing numbers, convert them to integers using map();
# a=['10','20','30','40']
# b=list(map(lambda x:int(x),a))
# print(b)

# # 10 Combine first and last names using map():
# fist_names=['John','Jane','Alice']
# last_names=['Doe','Smith','Johnson']
# print(list(map(lambda x,y:x+''+y, fist_names,last_names)))

# # 11 convert a list of binary strings to decimal using map():
# binaries=['1010','1111','0001','1001']
# def bintoint(s):
#       res=0
#       j=0
#       for i in s[::-1]:
#             res=res+(int(i)*2**j)
#             j+=1
#       return res
# print(list(map(bintoint,binaries)))


###################################################################################3

# filter


###############################################################333      
      
#  what is genreter   
# it is procces of creating new collection from a function that is non hase genrater.
#  if you use return keyword inside the returns the it is normal return if it called hase genreter
#  it posible have yield it return in same function but it called hase genrater .
# normal function call directly but genrater to typecast 

# Example:-
# 1
# def sample():
#       print('hello')
#       yield 1
#       print('hi')
#       return 50
#       yield 2
#       print('bye')
#       yield 3
# print(list(sample()))


# # 2 print 1 to 10 squre using function
# def sqr():
#       out=[]
#       for i in range(1,11):
#             out.append(i**2)
#       return out
# print(sqr())
            

# 2 print 1 to 10 squre using genrater
# def sqr(): 
#       for i in range(1,11):
#             yield i**2
# print(list(sqr()))
      
      
      
      
      

###############################################################################################


# def insta(func):
#       def inner (*args, **kwargs):
#             print



##################################################################################################################################3

### fuction practice ###

# # 1 Add two numbers
# def number(a,b):
#       return a+b 
# var=number(3,5)
# print(var)
# #
# def number(a,b):
#       print(a+b)
# number(3,5)


# # 2 check Even or Odd
# def number(a):
#       if a%2==0:
#             return('even')
#       else:
#             return('odd')
# var=number(6)
# print(var)      


# # 3 Find maximum of three number
# def number(a,b,c):
#       if a>b and c<a:
#             return("a is max:",a)
#       elif b>a and c<b:
#             return("b is max:",b)
#       else:
#             return('c is max:',c)
# var=(number(5,63,7))
# print(var)
      

# # 4 factorial of a number   
# def num(a):
#       v=1
#       for i in range(1,a+1):
#             v=v*i
#       print( v)
# num(5)


# ###################################################################

# def add():
#       a=int(input('enter 1st no:'))
#       b=int(input('enter 2nd no:'))
#       print(a+b)
# add()
# print('hi')
# add()
# print('hello')



# n=eval(input('enter the number:'))
# p=eval(input('enter the number:'))
# for i in range (1,n+1):
#     k=p
#     for j in range(1,n):
#         if i>j:
#             print(k,end='')
#             k+=1
#         else:   
#             print('',end='')
#     print()






# 
# method of member of object. it is nt recverd not class in the procece of object creation it in by befault  


# class bank:
#       bname='ICICI'
#       bloc='mumbai'
#       ifsc='icic123423'
#       helpline=123424                  

# # 

# class hospital:
#       name='raj'
#       Add='kalamboli'
#       helpline=984848186
      
#       def __init__(self,p_name,p_add,p_helpline,p_phenomen):
#             self.p_name=p_name
#             self.p_add=p_add
#             self.p_phenomen=p_phenomeng 
