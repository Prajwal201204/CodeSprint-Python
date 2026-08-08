# New topic
## enumerate, zip, zip_longest (itertools import)

####################################################################################

# #enumerate 
# # 1
# ls=[10,20,30,40]
# print(list(enumerate(ls)))

# # 2
# fruit=['apple','mango','banana']
# for i ,fruit in enumerate(fruit):
#     print(i , fruit)

#########################################################################

# # zip # #

# #1 withthout zip
# a=[10,20,30,40]
# b=[100,200,300,400]
# for i in range(len(a)):
#     print((a[i],b[i]))

# #2 with zip
# a=[10,20,30,40]
# b=[100,200,300,400]
# strr='hi'
# print(list(zip (a,b,strr)))

####################################################################################

# # zip_longest    (itertools import)

# # 1
# a=[10,20,30,40]
# b=[100,200,300,400]
# from itertools import zip_longest
# print(list(zip_longest(a,b)))
  
    
# # 2 sum a and b
# a=[10,20,30,40] 
# b=[100,200,300,400]
# c=[]
# from itertools import zip_longest
# for i,j in zip_longest(a,b):
#     if i ==None:
#         c.append(j)
#     elif j ==None:
#         c.append(i)
#     else:
#         c.append(i+j)
# print(c)

    
# # 2 sum a and b
# a=[10,20,30,40] 
# b=[100,200,300,400]
# c=[]
# from itertools import zip_longest
# for i,j in zip_longest(a,b):
#     if i ==None:
#         c.append(j)
#     elif j ==None:
#         c.append(i)
#     else:
#         c.append(i+j)
# print(c)
