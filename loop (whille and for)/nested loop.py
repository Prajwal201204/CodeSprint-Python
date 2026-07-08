# # 1
# s=[10,20,30,[1,2,3]]
# for i in s:
#     if type(i)==list:
#         for j in i:
#             print(j)
#     else:
#             print(i)


# # 2      
# ls = [[10, 20, 30], [100, 200, 300]]
# external = 0
# for i in ls:
#     internal = 0
#     for j in i:
#         internal += j
#     external += internal
#     print('internal : ', internal)
# print('External : ', external)


# #3
# num = int(input('Enter the number : '))
# isprime = True
# for i in range(2, num):
#     if num % i == 0:
#         isprime = False
#         break

# if isprime:
#     print('Prime number')
# else:
#     print('Not prime')


# 4
# cnt = 0
# newls = []
# for i in newls :
#     if i != 0 :
#         newls.append(i)
#     else :
#         cnt += 1

# print(newls + [0]*cnt)


# # 5
# ls = [1,2,0,0,8,4,5,2,0,4,0,5,0]
# j = 0
# for i in range(len(ls)):
#     if ls[i] != 0:
#         ls[i], ls[j] = ls[j], ls[i]
#         j += 1
# print(ls)




########################################################################################

# Nested For Loop: 

# # # 1. Wap to get the following output. without length function.
# # s = "power star"
# # out={'power': 5, 'star': 4}
# s = "power star"
# word=s.split()
# d={}
# for i in word:
#     count=0
#     for j in i:
#         count=count+1
#         d[i]=count
# print(d)
        
        
# # # 2.Wap to get the following output.        
# # s = "power star"
# # output={'power': 2, 'star': 1} -(no of vowels is key) 
# s = "power star"
# word=s.split()
# d={}
# for i in word:
#     count=0
#     for j in i:
#         if j in 'aeiou':
#             count=count+1
#             d[i]=count
# print(d)


# # # 3.Wap to get the following output. 
# # s = "kabab is love"
# # output={'kabab': ['babak', 2, 'kbb'], 'is': ['si', 1, 'i'], 'love': ['evol', 2, 'lv']} - [reverse,no of vowels,char at even index]
# s = "kabab is love"
# word=s.split()
# d={}
# rev=[]
# for i in range(len(word)):
#     rev=word[i][::-1]
#     count=0
#     for j in word[i]:
#         if j in 'aeiou':
#             count=count+1
#     even=''
#     for k in range(len(word[i])):
#         if k % 2==0:
#             even+=word[i][k]
#             d[word[i]]=[rev,count,even]
# print(d)


# # # 4. Wap to get the following output. 
# # s = "kabab is love"
# # output={'kb': ('kbb', 3, 'bbk'), 'is': ('s', 1, 's'), 'le': ('lv', 2, 'vl')} - { 1st+last char:  (consonant,no of consonant,rev of consonant)} 
# s = "kabab is love"
# word = s.split()
# d = {}
# for i in word:
#     key = i[0] + i[-1]
#     consonant = ""
#     count = 0
#     for j in i:
#         if j not in "aeiou":
#             consonant += j
#             count += 1
#     rev = consonant[::-1]
#     d[key] = (consonant, count, rev)
# print(d)


# # # 5. Wap to get the following output.
# # num=[100, 200, 35, 40, 60]
# # output=[335, 235, 400, 395, 375] - (total sum-value)
# a = [100, 200, 35, 40, 60]
# total = 0
# for i in a:
#     total += i
# out = []
# for i in a:
#     out.append(total - i)
# print(out)


# # # 6.Wap to get the following output. 
# #a='bacbcaabbaa'
# #Output='b4a5c2'
# s = "bacbcaabbaa"
# out = ""
# for i in s:
#     if i not in out:
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         out = out + i + str(count)
# print(out)


# # # 7. Wap to get the following output 
# # In=[100,200,50,400,300] 
# # N=300 
# # Out=[[100,200],[300]] 
# num=[100,200,50,400,300] 
# n=300 
# out=[]
# for i in range(len(num)):
#     if num[i]==n:
#         out.append(num[i])
#     for j in range(i+1,len(num)):
#         if num[i]+num[j]==n:
#             out.append([num[i],num[j]])
# print(out)
    

# # 8.Wap to check whether the number is strong or not. (method-1)
# num = 145
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact = fact * i
#     sum = sum + fact
#     temp = temp // 10
# if sum == num:
#     print("Strong Number")
# else:
#     print("Not Strong Number")
    
    
# # 8.Wap to check whether the number is strong or not. (method-2)
# num = 145
# total = 0
# for i in str(num):
#     digit = int(i)
#     fact = 1
#     for j in range(1, digit + 1):
#         fact = fact * j
#     total = total + fact
# if total == num:
#     print("Strong Number")
# else:
#     print("Not Strong Number")

