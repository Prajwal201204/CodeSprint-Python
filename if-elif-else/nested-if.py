# 

# #  Nested if

# age=int(input('Enter the age'))
# gender=input('Enter the gender')
# if age>18:
#     if gender.lower()=='male':
#         print('Hello mr.u r elible to vote' )
#     elif gender.lower()=='famale':
#         print('Hello ms.u r eligible to vote')
#     else:
#         print('you are also eligible')
# else:
#     print('Not eligible')



# # 1 wap to check the number is even and greater than 5
# a=int(input('Enter the value'))
# if a>5:
#     if a%2==0:
#         print('even number')
#     else:
#         ('odd number')
# else:
#     print('not grater than 5')


# # 2 wap to check the number is odd and greater than 5
# a=int(input('Enter the value'))
# if a%2!=0:
#     if a%5==0 and a%7==0:
#         print(f'num is odd:{a}')
#     else:
#         print('value not divisible by 5 and 7')
# else:
#     print(f'even number {a}')
    
    
# # 3 wap to validate facebook username and password 
# username=input('Enter the value:')
# password=input('Enter the value:')
# if username=='python':
#     if password=='prajwal':
#         print('correct password')
#     else:
#         print('Not match password')
# else:
#     print('not match username')


## 4 wap to find middle element is even or odd take list from user |  first check that there is a middle element or not 
# s=[2,4,6,7,9,1,5]
# if len(s)%2!=0:     
#     a=len(s)//2
#     b=s[a]
#     if b%2==0:
#         print('middle even')
#     else:
#         print('middle odd')
# else:
#     print('no middle element in list')
    
   
## 5 wap value 4 is a even or odd show
# s=[2,4,6,7,9,1,5] 
# a=s[1:2]
# b=a[0]
# if b%2!=0:
#     print('odd')
# else:
#     print('even')


# # 6 check is a character is a vowel and lowercase
# strr=input('Enter the value:')
# if strr in 'aeiou':
#     if strr.islower():
#         print('lowercase vowel')
# else:
#     print('not vowel')
    

# # 7 largest of three numbers 
# a=(input('Enter the value a:'))
# b=(input('Enter the value b:'))
# c=(input('Enter the value c:'))
# if a<b:
#     if b<c:
#         print(f'c {c}')
#     else:
#         print(f'b {b}')
# else:
#     print(f'a {a}')
        
        
# # 8 check if number is 3-digit and divisible by both 3 and 7
# a=int(input('Enter the value a:'))
# if 100<=a<=999:
#     if a%3==0 and a%7==0:
#         print('divisible by 3 and 7')
#     else:
#         print('not divisible by 3 and 7')
# else:
#     print('not a 3-digit number')


# # 9 ATM withdrawal logic
# balance=10000
# withdraw=int(input('Enter the value a:'))
# if withdraw>0:
#     if withdraw<=balance:
#         if withdraw%100==0:
#             print('Transaction successful')
#         else:
#             print('Transaction unsuccessful')
#     else:
#         print('insufficient balance')
# else:
#     print('invalid amount')


# # 10. Wap to login into the Instagram with valid username and password.(enter password only if the user name is valid) 
# username=input('enter tha username:')
# if username=='Prajwal':
#     password=input('enter tha password:')
#     if password=='1234':
#         print('login sussesfull')
#     else:
#         print('not correct password')
# else:
#     print('user name not valid')
    

# # 11. Wap to print the middle value of a list only if it is string. 
# a=[10,'prajwal',(1,2)]
# if len(a)%2!=0:
#     mid=len(a)//2
#     if type(a[mid])==str:
#         print('string')
#     else:
#         print('not string')
# else:
#     print('not middel value')


# # 12. Wap to check whether the character is vowel or consonant. 
# a=(input('Enter the value:'))
# if 'a'<=a<='z' or 'A'<=a<='Z':
#     if a in 'aeiouAEIOU':
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('not character')


# # 13. Wap to find the greatest of 4 numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# if a > b:
#     if a > c:
#         if a > d:
#             print("Greatest number is", a)
#         else:
#             print("Greatest number is", d)
#     else:
#         if c > d:
#             print("Greatest number is", c)
#         else:
#             print("Greatest number is", d)
# else:
#     if b > c:
#         if b > d:
#             print("Greatest number is", b)
#         else:
#             print("Greatest number is", d)
#     else:
#         if c > d:
#             print("Greatest number is", c)
#         else:
#             print("Greatest number is", d)


# # 14. Wap to print the value as it is only if the length of the value is even. 
# num=[10,20,30,50,40,50]
# if len(num):
#     if len(num)%2==0:
#         print('even',len(num))
#     else:
#         print('not even',len(num))


# # 15. Wap to print the last value of a list only if it is palindrome string starting with vowel. 
# cha=[10,20,'tom','anna']
# if type(cha[-1])==str:
#     if cha[-1]==cha[-1][::-1]:
#         if cha[-1][0] in 'aeiouAEIOU':3
#             print(cha[-1])
#         else:
#             print('not vowel')
#     else:
#         print('not palandrom')
# else:
#     print('not string')
    

# #16. Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value. 
# a='applv'
# if len(a)%2==1:
#     if a[0] in 'aeiouAEIOU':
#         if a[-1] not in 'aeiouAEIOU':
#             print(a[::-1])
#         else:
#             print('end not a consonat')
#     else:
#         print('start not a vowel')
# else:
#     print('not middel value') 




# # 17. Write a program to print middle Character of the given string only if it is upper Case Character
# a='apPle'
# if len(a)%2!=0:
#     mid=len(a)//2
#     if 'A'<=a[mid]<='Z':
#         print(a[mid])
#     else:
#         print('not middel value uppercase')
# else:
#     print('not middel value')
    


# # 18.Wap to find the second greatest of 4 values
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# l = [a, b, c, d]
# l.sort()
# print("Second Greatest =", l[-2])



# # 19.Wap to find the smallest of 4 numbers. 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# l = [a, b, c, d]
# l.sort()
# print("Second Greatest =", l[0])



# # 20. write a program to check whether to check give carecter given vowel and consonat.
# ch=input('enter the value :')
# if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z') :
#     if  ch in 'aeiou':
#         print('this is vowel')
#     else:
#         print('consonent')
# else:
#     print('not charcter')
    
        
# # 21. write a program to check first character is uppercase and end with digit and reverse the string
# value=input('enter the value :')
# if 'A'<=value[0] <='Z':
#     if '0'<=value[-1] <='9':
#         print(value[::-1])
#     else:
#         print('not ended')
# else:
#     print('not started with uppercase')


# # 22. print mid value in given string 
# l=['abc',10,20,'Aakash',45,457,4+5j]  
# if len(l)%2==1:
#     mid=len(l)//2
#     if type(l[mid])==str:
#         print(l[mid])
#     else:
#         print('middel value not a string')
# else:
#     print('not a middel value ')
