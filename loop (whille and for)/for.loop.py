
# #
# for var in 'hello':
#     print(var.upper())

# #
# strr='hello buddy'
# for i in range(0, len(strr),2):
#     print(strr[i])
    
# ##########################################################################

# for loop

# #1 wap to print all the characters of a given string
# strr=('Prajwal Nevase')
# for i in range(0,len(strr),1):
#     print(strr[i])
    
    

# # # 2 wap to segregate the values from 1-50 into even add odd numbers into list
# even=[]
# odd=[]
# for i in range(1,51):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print('even:',even)
# print('odd:',odd)
        


# # 3 wap to exract vowels and digits from a given string
# strr='hello@123'
# newstr=''
# for i in strr:
#     if i in 'aeiouAEIOU' or '0'<=i<='9':
#         newstr+=i
#         print(i,end='')
# print(newstr)
        
        

# # #4  wap to capitalize only the first letter of every word in the given list
# ls=['rahul','prajwal','omker']
# for i in ls:
#     print(chr(ord(i[0])-32)+i[1:])
        
        

# # # 5 wap toextract only indiviual data types from the list
# ls=['rahul','prajwal','omker',12,123.3,2+3j]
# for i in ls:
#     if type(i) not in (str,list,tuple,set,dict):
#         print(i)


# #5 wap toextract only indiviual data types from the list
# ls=['rahul','prajwal','omker',12,123.3,2+3j]
# for i in ls:
#     if type(i)==int:
#         print(i)
#     elif type(i)==float:
#         print(i)
#     elif type(i)==complex:
#         print(i)
#     elif type(i)==bool:
#         print(i)
#     # else:
#         # print('multi value data type:',i) 



# # 6 wap toextract only multivalue data types from the list
# ls=['rahul','prajwal','omker',[10,20,30],{12,212,4,45},12,123.3,2+3j]
# for i in ls:
#     if type(i)==str:
#         print(i)
#     elif type(i)==list:
#         print(i)
#     elif type(i)==tuple:
#         print(i)
#     elif type(i)==dict:
#         print(i)
#     elif type(i)==set:
#         print(i)
#     # else:
#     #     print(' single value data type ')



# # 7 wap to extract only the individual datatype from the list and sum of all the individual datatypes.
# ls=['rahul','prajwal','omker',[10,20,30],{12,212,4,45},12,33,34,123.3,2+3j,True,False]
# a=0
# for i in  ls:
#     if type(i)  in [int,float,bool]:
#         print(f'individual type:{i}({type(i)})')
#         a+=i
# print('sum',a)
    
        
        
# # 8 wap to print the count of alphabets and numbers and space in the given string    
# s="india got the independence in the year 1947"
# for i in s:
#     if range(0,len(s),1):
#         print(i)   
    
    
    
# 10  wap to create a dictionary and print the characters and its ascii value pair   
# s='hello world'
# dictt={}
# for i in s:
#     dictt[i]=ord(i)
# print(dictt)


# # 11 wap to create a dictionary and traverse into it and if the length is even print as it else reverse it.
# names=['apple','google','yahoo','microsft','gmail','walmart']
# dictt={}
# for i in names:
#     if len(i)%2==1:
#         dictt[i]=i[::-1]     # + str(len(i))
#     else:
#         dictt[i]=i
# print(dictt)
        
        

# # 12 wap to find the factorial of a number given by user 
# a=int(input('enter a number'))
# fact=1
# for i in range(1,a + 1):
#     fact*=i
# print('favtorial is:',a,fact)
    
    

# # 13 wpa to create a dictionary with element and its count pair
# ls=['yellow','green','red','white','red','white','yellow']
# dictt={}
# for i in ls:
#     if i in dictt:
#         dictt[i]+=1
#     else:
#         dictt[i]=1
# print(dictt)

        
# # # 14 wap to find the sum of all the number present inside a given string like "hello@123"
# a=('hello@123')
# total=0
# for i in a:
#     if i .isdigit():
#         total+=int(i)
# print('sum of digits:',total)



# # 15 wap to print the even positional characters from a given string using for loop
# a='hi123456'
# for i in range(0,len(a),):
#     print(a[i])   


# # # 16 wap to find the length of a string without using len() function
# a=('hello@123')
# length=0 
# for i in a:
#     length+=1
# print(length)


# 17. WAP to count the occurrences of all the characters present inside the given string.

# 18. WAP to remove the duplicates from a list taken by user.

# 19. WAP to print the even indexed values of a given list taken from user.

# # 20. WAP to replace all the characters from a given string with '.' which occurs more than once.
# # Example: hellohai → he..o.a.
# strr='hellohai'
# newls=''
# for i in strr:
#     if strr.count(i)>1:
#         newls+='-'
#     else:
#         newls+=i
# print(newls)
    

# # 21 show a index no and value
# ls=[10,20,30,40]
# a=[]
# for i in range(len(ls)):
#     a.append((i,ls[i]))
# print(a)


# # 22 wap to create a dictionary of word and its reverse pair from a given string 
# dictt={}
# s='tommorow is a weekend'
# words=s.split()
# for i in words:
#     dictt[i]=i[::-1]
# print(dictt)


# # 23 wap to print the value of two dictionary
# dict1={1:1,2:4,3:6}
# dict2={1:2,3:6,4:'hello'}
# print(dict(zip(dict1.values(),dict2.values())))


# # 24 print string name and one word ma kitna letter ha vo print karo
# s="helo buddu how are you"
# dictt={}
# for i in s.split():
#     dictt[i]=len(i)
# print(dictt)



# #######################################################################################

# practice time pass for loop

# # # print number from 1 to 5
# for i in range(1,6,1):
#     print (i)


# # print even numbers from 1 to 10 
# for i in range(1,11,1):
#     if i%2==0:
#         print(i)


# # print characters of a string
# a='123456789'
# for i in a:
#     print(i)



# # # print square of number from 1 to 5
# for i in range(1,6,1):
#     print(i**2)


# # # print 10 to 1 revers
# for i in range(10,0,-1):
#     print(i)

      
# # # print table of 3
# for i in range(1,11):
#     print (f'3x{i}={i*3}')


# # print 1 to 5 add total
# a=0
# for i in range(1,6):
#     a+=i
# print(a)
        

# # print 5 table
# for i in range(1,10):
#  print(i*5)



# # count number of vowels in a string
# a=('hello would')
# b=0
# for i in a:
#     if i in 'aeiou':
#         b+=1
# print('tis is vowel',b)



# # Reverse a string using for loop
# a=('prajwal')
# b=''
# for i in a:
#     b=i+b
# print(b)


# ##same index valu pair
# a=[10,20,30,40]
# b=[]                    
# for i in range(len(a)):
#     b.append((i, a[i]))
# print(b)




# ################################################




# # 1
# s=[10,20,30]
# for i in s:
#     print(i)

# # 2 find given function without using length function
# a=[[1,2,3],{1,23,4},(22,3,3,4)]
# count=0
# for i in a:
#     count+=1
# print(count)


# 3 only print vowels 
# a='adjgijo'
# vowel=''
# for i in a:
#     if i in 'aeiou':
#         vowel+=i
# print(vowel)


# # 4    
# a='Prajwal Nevase' 
# out=''
# for i in a:
#     if i==' ':
#         out+='_'
#     else:
#         out+=i
# print(out)
 
 
# # 5 
# l=[10,20,23,4,2,47,70]
# out=[]
# for i in l:
#     if i%5==0:
#         out.append(i)
# print(out)


# ###########################################################################################

# # for loop prac

# # 1.Wap to print all the integers present in a list. 
# a=['don',1,[1,2,3],20,(25,36)] 
# for i in range(len(a)):
#     if type(a[i])==int:
#         print(a[i])


# # 2.Wap to find the length of homogenous tuple without len(). 
# t = (10, 20, 30, 40, 50)
# count=0
# for i in t:
#     count+=1
# print(count)


# # 3.Wap to extract all the even numbers present in a list.
# num=[1,2,3,4,5,6]
# even=[]
# odd=[]
# for i in range(len(num)):
#     if num[i]%2==0:
#         even.append(num[i])
#     else:
#         odd.append(num[i])
# print('even=',even)
# print('odd=',odd)


# # 4.Wap to remove duplicates from list  
# num=[1,3,3,4,4,6,7]
# remove=[]
# for i in range(len(num)):
#     if num[i] not in remove:
#         remove.append(num[i])
# print(remove)


# # 5.Wap to reverse a string without using slicing. 
# a='Prajwal Nevase' 
# rev=''
# for i in range(len(a)):
#     rev=a[i]+rev
# print(rev)


# # 6.wap to extract all the lowercase characters in a string only if the ascii value is even. (method-1)
# a='PraJwaL'
# lower=''
# for i in range(len(a)):
#     if 'a'<=a[i]<='z':
#         b=ord(a[i])
#         if b%2==0:
#             lower=lower+a[i]
# print(lower)

        
# # 6.wap to extract all the lowercase characters in a string only if the ascii value is even. (method-2)
# a='PraJwaL'
# result = ""
# for i in a:
#     if i.islower() and ord(i) % 2 == 0:
#         result = result + i
# print(result)


# # 7.Wap to check whether the last digit of an integer is even or not. 
# a = 134
# for i in str(a):
#     last = int(i)
# if last % 2 == 0:
#     print("Even", last)
# else:
#     print("Odd", last)


# # 8.Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers. 
# d = {"a":10, 2: 20, "b": "Hello", "c": 30, 5: 40, "d": 50}
# extract={}
# for i, j in d.items():
#     if type(i)==str and type(j)==int:
#         extract[i]=j
# print(extract)
        
    
# # 8.Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers. 
# d = {"a":10, 2: 20, "b": "Hello", "c": 30, 5: 40, "d": 50}
# extract={}
# for i in d:
#     if type(i)==str and type(d[i])==int:
#         extract[i]=d[i]  
# print(extract)


# # 9.Wap to extract key value pairs from the dictionary only if both keys and values are exactly same. 
# d = {"a":10, 2: 20, "b": "Hello", "c": "c", 5: 5, "d": 50}
# extract={}
# for i in d:
#     if i==d[i]:
#         extract[i]=d[i]
# print(extract)


# # # 10. Wap to get the following output using len function. 
# # S='power star'
# # Out={'power':5,'star':4}
# s='power star'
# word=s.split()
# d={}
# for i in word:
#     d[i]=len(i)
# print(d)


# # 11.Wap to get the following output.
# # s='power star'
# # {'power': 'rewop', 'star': 'rats'}
# s='power star'
# word=s.split()
# d={}
# for i in word:
#     d[i]=i[::-1]
# print(d)


# # 12.wap to extract all the non default  values from a list. 
# a = [10, 0, "", "Python", [], [1, 2], False, True, None, 25]
# result = []
# for i in a:
#     if i:
#         result.append(i)
# print(result)


# # 13.Wap to check whether the list is homogenous or not.    
# l = [10,20,30,40,50]
# same = True
# for i in range(len(l)):
#     if type(l[i]) != type(l[0]):
#         same = False
# if same:
#     print("Homogeneous")
# else:
#     print("Not Homogeneous")


# # 14.Wap to replace the space by * present in a string 
# s='power star in a don'
# a=''
# for i in s:
#     if i == ' ':
#         a=a+'*'
#     else:
#         a=a+i
# print(a)
    

# # 15.Wap to count the number of occurrence of a specified character. 
# a='hello'
# count=0
# for i in range(len(a)):
#     if a[i]=='l':
#         count=count+1
# print(count)


# # #  16.Wap to get the following output. 
# # S = 'always keep smiling'
# # out='syawla peek gnilims'
# s= 'always keep smiling'
# rev=''
# word=s.split()
# for i in word:
#     a=i[::-1]
#     rev=rev+a+' '
# print(rev)


# # # 17.Wap to get the following output. 
# # s='push maadi kushi padi'
# # Output:{'push':'ph','maadi':'a','kushi':'s','padi':'pi'} 
# s='push maadi kushi padi'
# word=s.split()
# out={}
# for i in word:
#     if len(i)%2==0:
#         out[i]=i[0]+i[-1]
#         # print(out)
#     else:
#         mid=len(i)//2
#         out[i]=i[mid]
# print(out)


# # 18.Wap to toggle a string. 
# a='AbCdEfGHi'
# for i in range(len(a)):
#     if 'a'<=a[i]<='z':
#         print(chr(ord(a[i])-32))
#     elif 'A'<=a[i]<='Z':
#         print(chr(ord(a[i])+32))


# # # 19. Wap extract upper, lower, digit and special characters present in a string to different. output variable  
# a = "AbC@12xy#"
# upper = ""
# lower = ""
# digit = ""
# special = ""
# for i in a:
#     if 'A' <= i <= 'Z':
#         upper = upper + i
#     elif 'a' <= i <= 'z':
#         lower = lower + i
#     elif '0' <= i <= '9':
#         digit = digit + i
#     else:
#         special = special + i
# print("Upper :", upper)
# print("Lower :", lower)
# print("Digit :", digit)
# print("Special :", special)


# # # 20.Wap to get the following output. 
# # S = "hai hello"
# # Output={'hai':'ai', 'hello':'eo'}
# s="hai hello"
# word=s.split()
# d={}
# for i in word:
#     v=''
#     for j in i:
#         if j in 'aeiou':
#             v=v+j 
#         d[i]=v
# print(d)



