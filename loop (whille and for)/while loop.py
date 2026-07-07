## 1 print number from 1 to 5 using a while loop
# a=1
# while a<=5:
#     print(a)
#     a=a+1


# # 2 print even numbers from 2 to 20
# a=2
# while a<=20:
#     print(a)
#     a=a+2
    
    
# # 3 print sum of number from 2 to 5
# a=1
# total=0
# while a<=5:
#     total+=a
#     a+=1
# print('total',total)
#     # a+=1
    
    
# # 4 print all characters of a string one by one using while loop
# ls=(input('Enter the value:'))
# i=0
# while i<len(ls):
#     print(ls[i])
#     i+=1    

            
# # # 5 count how many vowels are in a string
# ls=input('Enter the value:')
# i=0
# count=0
# while i<len(ls):
#     if ls[i] in 'aeiou':
#         count+=1
#     i+=1
# print(count)


# # 6 Add only even number (1 to 50) to a list
# ls=50
# i=0
# even=[]
# while i<=ls:
#     if i%2==0:
#         even=even+[i]
#     i+=1
# print(even) 


############################################################################################################################3
# WHILE

# 1. WAP to do print the series of lower case a-z characters
# 2. WAP to print both upper case and lower case characters A a B b C c
# 3. WAP to print all the even numbers between 1 to 50
# N. WAP to print the square and square root of all the numbers from a list given by user
# 4. WAP to print all the even numbers between 1 to 50 in reverse order
# 5. WAP to count the number of occurrences of a particular character in the given string
# N. WAP to find the factorial of a number given by user


# # 6 wap to print all the even positional characters of a given string
# ls=(input('Enter the value:'))
# i=0
# while i<len(ls):
#     if i%2==0:
#         print(ls[i])
#     i+=1


# # # 7 wap to segregate even and odd numbers between 1 to 100 in two different named lists
# ls=int(input('Enter the value:'))
# i=0
# odd=[]
# even=[]
# while i<=ls:
#     if i%2==0:
#         even.append(i)
#         # print(even)
#     else:
#         odd.append(i)
#         # print(odd)
#     i+=1
# print('even',even)
# print('odd',odd)


# # 8 wap to print the table of a number like 5 * 1=5 take this number from the user
# ls=int(input('Enter the value:'))
# i=1
# while i<=10:
#     # if i*10:
#     print(f'{ls}*{i}={i*ls}')
#     i+=1
    
    
# # # 9 wap to print the data from a list length of then is even
# ls=eval(input('Enter the value:'))
# i=0
# while i<len(ls):
#     if len(ls[i])%2==0:
#         print(ls[i])
#     i+=1


# # 10 wap to print the data from a list only if it is of collection datatype
# ls=eval(input('Enter the value:'))
# i=0
# while i<len(ls):
#     if type(ls[i]) in (list,tuple,set,dict,str):
#         print(ls[i])
#     i+=1


# # 11 wap to print the names from a list whose name is starting with a vowel
# ls=['vaidehi','prajwal','om','elephant','inocent','ram']
# i=0
# while i <len(ls):
#     if ls[i] [0] in 'aeiou':
#         print(ls[i], end=' ')
#     i+=1


# # 12 wap to print all the names from a list and their first character should be capital and rest of the word should be in lower case only
# ls=eval(input('Enter the value:'))
# i=0
# newls=[]
# while  i<len(ls):
#     newls.append(chr(ord(ls[i][0])-32)+ls[i][1:])
#     i+=1
# print(newls)


# # # 13 wap to print the sum of all numbers present inside the given list
# ls=[1,2,3,4,5]
# i=0
# total=0
# while i<len(ls):
#     total+=ls[i]
#     i+=1       
# print('total', total)



# # 14 wap to find the sum of all the number from a given range from user which  are divisible by 5 and 7 and get all of them in a new list
# start=int(input('Enter the value:'))
# end=int(input('Enter the value:'))
# newls=[]
# i=start
# total=0
# while i<end:
#     if i%5==0 and i%7==0:
#         newls.append(i)
#         total+=i
#     i+=1
# print(newls)
# print(total)


# # 15 wap to extract all the vowels and digits from a given string  (s='hrllo@123) out=eo123
# a='hello@123'
# i=0
# count=''
# while i<len(a):
#     if a[i] in 'aeiouAEIOU' or '0'<=a[i]<='9':
#         count+=a[i]
#     i+=1
# print(count)


# # # 16 wap to find the number of same bits of same length strings 
# s1='010101010000111'
# s2='001001101111001'
# i=0
# count=0
# while i<len(s1):
#     if s1[i]==s2[i]:
#         count+=1
#     i+=1
# print(count)


# # # 17 wap to get occurences of each elements in a given list
# ls=['red','red','green','green','yellow','red','orange','orange']  #| output ={'red': 2, 'green': 2, 'yellow': 1, 'orange': 2}
# dictt={}
# i=0
# while i<len(ls):
#     if ls[i] not in dictt:
#         dictt[ls[i]]=1
#     else:
#         dictt[ls[i]]+=1
#     i+=1
# print(dictt)


    
# # # 18 pailindrome check
# strr=input('enter the string:')
# start=0
# end=len(strr)-1
# while start<end:
#     if strr[start]!=strr[end]:
#         print(strr[start],strr[end])
#         print('Not pailindrome')
#         break
#     start+=1
#     end-=1
#     print('pailindrome')


# # 19 pailindrome check  (method-2)
# strr=input('enter the string:')
# ispal=1
# start=0
# end=len(strr)-1
# while start<end:
#     if strr[start]!=strr[end]:
#         ispal=0
#         break
#     start+=1
#     end-=1
# if ispal==1:
#     print('palindrome string')
# else:
#     print('not pallindrome')


# # 20 Anagram string
# isana=True 
# if len(s1)!=len(s2):
#     print('not anagram')
# else:
#     i=0
#     while i<len(s1):
#         if s1[i] not in s2 or s1 count (s1[1])



##########################################################################3
### while loop prac 

# # 1 reverse 
# n=1234
# rev=0
# while n!=0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)


# # 2
# strr=input('enter the string:')
# start=0
# end=len(strr)-1
# while start<end:
#     if strr[start]!=strr[end]:
#         print(strr[start],strr[end])
#         print('Not pailindrome')
#         break
#     start+=1
#     end-=1
#     print('pailindrome')


# # # 3 sum od all list
# l=[10,20,30,40,50]
# sum=0
# i=0
# while i<len(l):
#     sum+=l[i]
#     i+=1
# print(sum) 


# # 4 odd number sum
# l=[10,20,31,79,63,30,40,50]
# sum=0
# i=0
# while i<len(l):
#     if l[i]%2!=0:
#         sum+=l[i]
#     i+=1
# print(sum)


# # # 5 print only even number and sum
# l=[10,20,31,79,63,30,40,50]
# sum=0
# i=0
# while i<len(l):
#     if l[i]%2==0:
#         sum+=l[i]
#     i+=1
# print(sum)


    
# # 6 revers list 
# l=[10,20,31,79,63,30,40,50]
# i=len(l)-1
# while i>=0:
#     print(l[i])
#     i-=1


# # 7 strong number 
# n=int(input('enter the value:'))
# sum=0
# temp=n
# while temp!=0:
#     ld=temp%10
#     fact=1
#     i=1
#     while i<=ld:
#         fact=fact*i
#         i+=1
#     sum=sum+fact
#     temp=temp//10
# if sum==n:
#     print('strong number')
# else:
#     print('not a strong number') 


# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# while loop practise 

# # 1. Wap to print python for 5 times
# a='python'
# i=1
# while i <=5:
#     print('python')
#     i+=1


# # 2. Wap to print n natural numbers.
# a=50
# i=1
# while i<=a:
#     print(i)
#     i+=1 


# # 3. Wap to print multiplication table for n.
# n=int(input('enter tha value:'))
# i=1
# while i<=10:
#     print(f"{n} * {i}= {n*i}")
#     i+=1


# # 4. Wap to find the sum of n natural numbers. 
# a=5
# i=0
# total=0
# while i<=a:
#     total=total+i
#     i+=1
# print(total)
    
    
# # 5. Wap to find the product of n natural numbers or factorial of a number. 
# n=int(input('enter tha value:'))
# product=1
# i=1
# while i <=n:
#     product=product*i
#     i+=1
# print(f"factorial={product}")
    
    
# # 6. Wap to print all the characters of a string. 
# a='prajwal'
# i=0
# while i < len(a):
#     print(a[i])
#     i+=1
    
    
# 7.Wap to print all the characters present at even index of a string. (method-1)
# a='Prajwal'
# i=0
# while i<=len(a):
#     print(a[i])
#     i+=2


# # 7.Wap to print all the characters present at even index of a string. (method-2)
# a='prajwal'
# i=0
# while i<=len(a):
#     if i%2==0:
#         print(a[i])
#     i+=1


# # 8. Wap to extract all the lowercase characters present in a string.
# cha=input('enter the value:')
# i=0
# while i<len(cha):
#     if 'a'<=cha[i]<='z':
#         print(cha[i])
#     i+=1
 
 
# #  9. Wap to extract all the vowels present in a string. 
# a=input('enter the value:')
# i=0
# while i < len(a):
#     if a[i] in 'aeiouAEIOU':
#         print(a[i])
#     i+=1


# # 10. Wap to print factors of a integer number. 
# a=12
# i=1
# while i <= a:
#     if a%i==0:
#         print(i)
#     i+=1


# # 11.Wap to toggle a string. (Toggle ka matlab:Uppercase → Lowercase , Lowercase → Uppercase)
# a='PraJwaL'
# i=0
# while i<len(a):
#     if 'a'<=a[i]<='z':
#         print(chr(ord(a[i])-32))
#     elif 'A'<=a[i]<='Z':
#         print(chr(ord(a[i])+32))
#     i+=1


# # 12.Wap to reverse the given number.  
# a=int(input('enter the value:'))
# rev = 0
# while a > 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10
# print(rev)
    

# # 13. Wap to find the sum of individual digits of a number. 
# a=int(input('enter the value:'))
# total=0
# while a>0:
#     digit=a%10
#     total=total+digit
#     a=a//10
# print(total)


# # 14. Wap to check whether the number is perfect or not. 
# num = int(input("Enter number: "))
# i = 1
# total = 0
# while i < num:
#     if num % i == 0:
#         total = total + i
#     i += 1
# if total == num:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")


# # 15.Wap to login to phonepe by entering correct otp
# otp=2004
# user=int(input('enter the otp:'))
# while user != otp:
#     print('wrong otp')
#     user=int(input('enter the otp: '))
# print('login sussesfull')


# # 16. Wap to run infinite loop until user enters the correct password. 
# password=1234
# user=int(input('Enter the password: '))
# while True:
#     password !=user
#     user=int(input('Enter the password: '))
#     if password==user: 
#         print('correct password')
#         break
#     else:
#         print('wring password')


# # 17.Wap to extaract all the even integers present in a tuple at odd index. 
# a=(10,4,5,10,8,19,7,6)
# i=1
# while i<len(a):
#     if a[i]%2==0:  
#         print(a[i])
#     i+=2


# # 18.Wap to remove duplicates from a list without converting into set. 
# a=[10,4,5,10,8,19,5,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)
  
        
# # 19.Wap to find the sum of all the odd numbers between the given range. (method=1) 
# a=int(input('Enter the star: '))
# b=int(input('Enter the end: '))
# total=0
# while a<=b:
#     if a%2==1:
#         total=total+a
#     a+=1
# print(total)


# 19.Wap to find the sum of all the odd numbers between the given range. (method=2) 
# a=[1,2,3,4,5,6,7,8]
# i=0
# total=0
# while i<len(a):
#     if a[i]%2==1:
#         total=total+a[i]
#     i+=1
# print(total)


# 20.Wap to find the greatest number in a given list of integers. (method=1) 
# a=[1,'pra',(1,2,3),19,15]
# i=0
# greatest=None
# while i<len(a):
#     if type(a[i])== int:
#         if greatest==None:
#             greatest=a[i]
#         elif a[i] > greatest:
#             greatest=a[i]
#     i+=1
# print(greatest)


# # 20.Wap to find the greatest number in a given list of integers. (method=2) 
# a = [100, 25, 255, 10, 959, 45, 6]
# i=0
# grestest=a[0]
# while i<len(a):
#     if a[i]>grestest:
#         grestest=a[i]
#     i+=1
# print(grestest)

    
    
# # 21.Wap to find the sum of cube of a number in a string. (Method-1)
# a=[2,'pra',(1,2,3),19,15]
# i=0
# total=0
# while i<len(a):
#     if type(a[i])==int:
#         cube=a[i]**3
#         total=total+cube
#     i+=1
# print(total)


# # 21.Wap to find the sum of cube of a number in a string. (Method-2)
# a='2a3f6h7'
# i=0
# total=0
# while i<len(a):
#     if a[i].isdigit():
#         total=total+int(a[i])**3
#     i+=1
# print(total)
        

# # 21.Wap to check whether the number is Armstrong or not. 
# a=153
# temp=a
# total=0
# i=0
# while i<a:
#     b=a%10
#     cube=b**3
#     total=total+cube
#     a=a//10 
# i+=1
# if total==temp:
#     print('Armstrong number')
# else:
#     print('not Armstrong')   


# # 22.  Wap to get the following output.  A='1001110001',B='0011010101'out=4(count of positions having same values) 
# A='1001110001'
# B='0011010101'
# out=0
# i=0
# while i<len(A):
#     if A[i]==B[i]:
#         out=out+1
#     i+=1
# print(out)
        

# # 23.Wap to check the given number is prime or not. 
# a=7
# i=2
# count=0
# while i<a:
#     if a%i==0:
#         count=count+1
#     i+=1
# if count==0:
#     print('prime')
# else:
#     print('not prime')


# # 24.Wap  to check whether the number is palindrome or not.     
# a = 202
# temp = a
# rev = 0
# while a > 0:
#     digit = a % 10
#     rev = rev * 10 + digit
#     a = a // 10
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    

# # 25.Wap to find the HCF of two numbers.     
# a = 12
# b = 18
# hcf = 1
# i = 1
# while i <= a:
#     if a % i == 0:
#         if b % i == 0:
#             hcf = i
#     i += 1
# print("HCF =", hcf)


# # 26.Wap to convert binary to decinaml. 
# binary = int(input("Enter a binary number: "))
# decimal = 0
# power = 0
# while binary > 0:
#     digit = binary % 10
#     decimal = decimal + digit * (2 ** power)
#     power += 1
#     binary = binary // 10
# print("Decimal =", decimal)


# # 27.Wap to convert decimal to binary. 
# a = 10
# binary = ""
# while a > 0:
#     rem = a % 2
#     binary = str(rem) + binary
#     a = a // 2
# print(binary)


# # 28.Wap to count the number of words in a string. 
# s = "I love Python"
# i=0
# count=1
# while i<len(s):
#     if s[i]==' ':
#         count=count+1
#     i+=1
# print(count)


# # 29.Wap to guess the number.
# num=2004
# guess=int(input('guess the number'))
# while guess!=num:
#         print('wring guess')
#         guess=int(input('guess the number'))
# if guess==num:
#     print('correct guess')


# # 30.Wap to find the common elements in two sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A = list(A)
# i = 0
# comm = set()
# while i < len(A):
#     if A[i] in B:
#         comm.add(A[i])
#     i += 1
# print(comm)


# # 31.Wap to find the product of all the digits present in a number. 
# a = 1234
# product = 1
# while a > 0:
#     digit = a % 10
#     product = product * digit
#     a = a // 10
# print("Product =", product)