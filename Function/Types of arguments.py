

#  # Types of arguments (5 Types of arguments)

# # 1 positional arguments :
# 
# def printer(a,b):
#     print(f'a:{a} | b: {b} a+b: {a+b}')
# printer(20,10)  



# # 2 keyword arguments :
# 
# def printer(a,b):
#     print(f'a:{a} | b: {b} a+b : {a+b}')
# printer(a=20,b=10) 



# # 3 default arguments :
# 
# # 1
# def printer(a,b=10):
#     print(f'a:{a} | b: {b} a+b : {a+b}')
# printer(20)

# # 2
# def addition(a=100,b=0):
#     print(f'a:{a} | b: {b} = {a+b}')
# addition(b=10 , a=120)



# # 4 varible length positional arguments (*arguments) 
#  
# def add(*arguments):
#     sum=0
#     # print(arguments,type(arguments))
#     for i in arguments:
#         sum +=i
#     print(f'total sum : {sum:.2f}')
# add(1,2,3,4,7.464)



# # # 5 varible length positional arguments (**keyword arguments) 
# 
# def func(**kwargs):
#     # print(kwargs,type(kwargs))
#     for i, j in kwargs.items():
#         print(i,j)
# func(a=100,b=200,hello='hii',bye2=200)



############################################################################################################################3

# # arguments example  

# # # 1 waf to get the following output:
# # a='happy morning be safe'
# # out={'happy': 1, 'morning': 2, 'be': 1, 'safe': 2}
# 
# a='happy morning be safe'
# dictt={}
# for i in a.split():
#     cnt=0
#     for j in i :
#         if j in 'aeiouAEIOU':
#             cnt +=1
#     dictt[i]=cnt
# print(dictt) 



# # # 2 get this output
# # s = "hai hello how are you"
# # out= 'iah olleh woh era uoy'
# 
# def reverse_words(s):
#     return " ".join([i[::-1] for i in s.split()])
# print(reverse_words("hai hello how are you"))



# # # 3 waf to extract the vowels from each word of a string
# # s = "hello buddy how are you"
# # out={'hello': 'eo', 'buddy': 'u', 'how': 'o', 'are': 'ae', 'you': 'ou'}
# 
# def get_vowels(s):
#     vowels = "aeiou"
#     words = s.split()
#     result = {}
#     for i in words:
#         temp = ""
#         for ch in i:
#             if ch in vowels:
#                 temp = temp + ch
#         result[i] = temp
#     return result
# s = "hello buddy how are you"
# print(get_vowels(s))
             
       
       
# # # 4 waf to get this output
# # s = 'python is very easy'
# # out={'python': 'pn', 'is': 'is', 'very': 'vy', 'easy': 'ey'}
# 
# def custom_output(sentence):
#     words = sentence.split()
#     result = {}
#     for i in words:
#         # take only first and last letters
#         if len(i) >= 2:
#             result[i] = i[0] + i[-1]
#         else:
#             result[i] = i
#     return result
# s = 'python is very easy'
# print(custom_output(s))
        
    
    




