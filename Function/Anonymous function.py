# # Anonymous function (lambda function)

# # #1
# # square=lambda*args : print(args)
# # square(2,3,4,5,67,8,9)

# # # 2
# # sum= lambda x,y : [x+y,x*y]
# # print(sum(10,20))

# # # 3
# # opr=lambda x: x**2 if x%2==0 else None
# # print(opr(3))
# # print(opr(4))
 
# # # 4 
# # func=lambda*x : [i**2 for i in x]
# # print(func(10,2,3,4,7,86,46))

# # # 5 
# # print((lambda x : x*2)(100))


# ##########################################################################################3

# # lambda function Example

# # # 1 waf to find square and cub of a given number 
# # sum= lambda x : [x**2,x**3]
# # print(sum(6))

# # # # 2 wap to check that the given string is a palindrome or
# # strr=lambda x : 'Palindrome' if x==x[::-1] else 'not Palindrome'
# # print(strr('momsg'))

# # # 3 check if a given number is a palindrome
# # strr=lambda x:'palindrome' if x==x[::-1] else 'not palindrome'
# # print(strr('101'))

# # #  4 wap to convert negative number to positive number 
# # num=lambda x:x if x>=0 else -x
# # print(num(-99))

# # # # 5 wap to return all key of a dictionary
# # dictt=lambda a: list(a.keys())
# # a={'a':10 ,'b':20,'c':30 }
# # print(dictt(a))
 
# # 6 waf to return the first and last element of a sequence
# # listv=lambda x: (x[0] , x[-1])
# # x=[10,20,30,40]
# # print(listv(x))

# # 7 waf to reurn the length of a iterable / collection 
# # list=lambda x:len(x)
# # x=[10,20,30,40]
# # print(list(x))

# # 8 find the sum of same indixed value of two diff list
# x = [10, 20, 30, 40]
# j = [1, 2, 3, 4]
# result = list(map(lambda a:a [0] + a [1], zip(x, j)))
# print(result)


# # # 9 You have a dict of name = gender and get a list of name with mr and miss
# # dict1 = {'Rahul': 'male', 'Riya': 'female'}
# # out=['mr.rahul', 'miss.riya']      Name should always be in lowercase.
# 
# dict1 = {'Rahul': 'male', 'Riya': 'female'}
# out = list(map(lambda x: ("mr." if dict1[x] == 'male' else "miss.") + x.lower(), dict1))
# print(out)




















































































