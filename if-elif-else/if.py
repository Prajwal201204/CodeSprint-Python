# # # 1
# a=int(input('Enter the number'))
# if a%2==1:
#     print('odd') 
    
# # # 2
# a=int(input('Enter the number'))
# if a%2==0:
#     print('even')
    
# # # 3
# a=(input('Enter the number'))
# if a==a[::-1]:
#     print('pallindrom')
# if a!=a[::-1]:
#     print('Not pallindrom')

# # # 4
# a=230
# b=50
# if a>b:
#     print(a,'not greater')
# if a<b:
#     print(b,'greater')

# # 5
# strr=(input('Enter the string:'))
# if len(strr)%2==0:
#     print('even length')
# if len(strr)%2!=0:
#     print('odd length')

## 6
# prog_list=(input('Enter the string'))
# prog=(input('Enter the length:'))
# if prog.lower()in prog_list:
#     print(f'{prog} is present')
# if prog.lower()not in prog_list:
#     print(f'{prog} is not present')


# # 7 
# a=int(input('Enter the num'))
# if a>=0:
#     print('given number is Positive') 


# # 8 
# a=input('enter the string:')
# if a[0]  in 'aeiou':
#     print('consonat')
# else:
#     print('not consonat')


# # 9
# a=input('enter the string:')
# if a[-1] in 'aeiou':
#     print('this is vowel')


# # 10
# a=input('enter the string:')
# if a.isupper():
#     print('upper')
# if not a.isupper():
#     print('NOT upper')


# # 11
# a=int(input('enter the num:'))
# if a>1 and a<5:
#     print('python is easy')


# # 12 check if a number is divisible by 5
# a=int(input('enter the num:'))
# if a%5==0:
#     print('divisible by 5')


# # 13 check if the string contains the word "python"
# a=(input('enter the string:'))
# if 'python' in a.lower():
#     print('present the python word')


# # # 14 check if the last digit of a number is 0
# a=int(input('enter the num:'))
# if a%5==0:
    # print('last digit num 0')


# # 15 check if the number is a 3-digit number
# a=int(input('enter the num:'))
# if a>100 and a<999:
#     print('these is a 3-digit number')


# # 16 check if the character is a digit
# a=(input('enter the num:'))
# if a.isdigit():
#     print('all character digit')


# # 17 check if number is negative
# a=int(input('enter the num:'))
# if a<0:
#     print('value is nagetive') 
    
    
# # 18 check if the length of a string is more than 5
# a=(input('enter the num:'))
# if len(a)>5:
#     print('length is more than 5')


# # 19 check if a given year is a leap year 
# a=int(input('enter the num:'))
# if a%4==0:
#     print('leap year')


# # 20 check if two strings are equal
# a=(input('enter the num:'))
# b=(input('enter the num:'))
# if a==b:
#     print('string are equal') 
    
     
# # 21 check if the number is between 1 and 100
# a=int(input('enter the num:')) 
# if a>=1 and a<=100:
#     print('num is between 1 and 100')


# # 22 check if the sum of two number is greater than 100
# a=int(input('enter the num:'))
# b=int(input('enter the num:'))
# if a+b >100:
#     print('greater than 100')


# # 23 check if the first and last digit of a number are same
# a=(input('enter the num:'))
# if a[0]==a[-1]:
#     print('first and last digit are same')


# # 24 check if a person is eligible for a discount (age<18 or age >60)
# a=int(input('enter the num:'))
# if a<18 or a>60:
#     print('discount eligible' ) 


# # 25 check if the username start with a capital letter
# a=(input('enter the num:'))
# if a[0].isupper():
#     print('start with capital letter') 


# # 26 check if a 3-digit number has all digits same  (like 111,222)
# a=(input('enter the num:'))
# if a[0]==a[1]==a[2]:
#     print('all digit are same')
    
    
# # 27 check if a string has at least one vowel
# a=(input('enter the num:'))
# if  'a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a:
#     print('vowel')


# # 28 check if two numbers are both odd or both even
# a=int(input('enter the num:'))
# b=int(input('enter the num:'))
# if a%2==b%2:
#     print('both are odd or both are even')


   


##############################################################################################################


# practice  if question 

# # 1. Wap to print the square of a number only if it is even.
# num=int(input('Enter the value:'))
# if num%2==0:
#     print(num**2)


# # 2. Wap to check whether the character is vowel or not. 
# char=input('Enter the value:')
# if char in 'aeiouAEIOU':
#     print('vowel')
# if char not in 'aeiouAEIOU':
#     print('not vowel')

# # 3. Wap to print Ascii value of a character only if it is upper case. 
# char=input('Enter the value:')
# if 'A'<=char<='Z':
#     print(ord(char))

# # 4. Wap to print the cube of a number only if it is divisible by 9 or 6
# num=int(input('enter the value:'))
# if num%9==0 and num%6==0:
#     print(num**3)

# # 5. Wap to check whether the given integer is 3 Digit number. 
# num=int(input('enter the value:'))
# if 100<=num<=999:
#     print('3 digit no')

# # 6. Wap to check whether the last digit of a given number is 5. 
# num=int(input('enter the value:'))
# if num%10==5:
#     print('given no 5',num)

# # 7. Wap to check whether the given data is float. 
# num=eval(input('enter the value:'))
# if type(num)==float:
#     print('given data is float')

# # 8. Wap to check whether the data is single value data. 
# num=eval(input('enter the value:'))
# if type(num)==int:
#     print('single value data')

# # # 9. Wap to check whether the given character is digit or not. 
# num=(input('enter the value:'))
# if '0'<=num<='9':
#     print('digit')

# # 10. Wap to check whether the given integer is multiple of 3. 
# num=int(input('enter the value:'))
# if type(num)==int and num%3==0:
#     print('multiplay by 3')
