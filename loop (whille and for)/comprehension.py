
# #
# ls=[i**2 if i%2==0 else i**3 for i in range (1,11) ]
# print(ls)

#################################################################################################################################################

# # # List comprehension # # #

# # # 1 wap to check that the type of element is individual or collection. if collection reverse it, else return the square of that
# # with isinstance
# ls=[3, [1, 2, 3], 5, (4, 5)]
# newls=[i[::-1] if isinstance(i,(list,tuple)) else i**2 for i in ls ]
# print(newls)

# # without isinstance    
# ls=[3, [1, 2, 3], 5, (4, 5)]
# lm=[i[::-1] if type(i) in [tuple,list] else i**2 for i in ls]
# print(lm)


# # # 2 WAP to check that the length of the names stored inside the list is even or odd. If even, reverse it and append.Else, append its length only.
# names = ["Alice", "Bobe", "Charlie", "David" , "ronq"]
# ls=[i[::-1] if len(i)%2==0 else len(i) for i in names]
# print(ls)


# # # 3  WAP to find the square of all the numbers between 1 to 50 if that number is divisible by 5.
# ls=[ i**2  for i in range(1,51) if i%5==0  ]
# print(ls)


# # # 4 WAP to get the following output:
      # # s = 'python is very easy'
      # # out = [(python, 6), (is, 2), ...]
# s = 'python is very easy'
# out=[(i,len(i)) for i in s.split()]
# print(out)


# # # 5 WAP to extract all the even numbers from a given collection.
# collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [i for i in collection if i % 2 == 0]
# print(evens)


# #  # 6 WAP to create a list which contains 10 multiples of 2.
# multiples_of_2 = [2 * i for i in range(1, 11)]
# print(multiples_of_2)

 
# # # #7 WAP to create a list that contains the sum of same‑indexed values of two lists taken from user as input with and without zip() function.  
# # with zip function
# a=[10,20,30,40]
# b=[1,2,3,4]
# c=[i+j for i,j in zip(a,b)]
# print(c)

# # # without zip function
# a=[10,20,30,40]
# b=[1,2,3,4]
# c=[a[i]+b[i] for i in range(len(a)) ]
# print(c)



###################################################################################################################################################


# # # Set comprehension # # #

# # 1. WAP to remove repeated values from a list and return in a set.
# lst = [1, 2, 2, 3, 4, 4, 5, 1, 6]
# unique_set = {i for i in lst}
# print(unique_set)


# # 2. WAP to get only the palindrome strings from a list and there should be no duplicates in the final output.
# words = ["madam", "racecar", "apple", "hello", "madam", "noon", "level", "world", "noon"]
# palindromes = {word for word in words if word == word[::-1]}
# print(palindromes)


#######################################################################################################################3


# # # dict comprehension # # #

# # # 1 WAP to create a dictionary of values and index pairs with and without enumerate() function.
# #without enumerate()
# a=['google',' mapple', 'apple', 'python', 'orange']
# b={i:a[i] for i in range(len(a))}
# print(b)

# # with enumerate()
# a=['google',' mapple', 'apple', 'python', 'orange']
# b={i:j for i,j in zip(range(len(a)), a)}
# print(b)


# # # 2 WAP to create a dictionary having the first character of each word and word pair if the word has even length from a list.
# #    ex=[google, mapple, apple, pythonn, genai]
# #    Output: {'g': google, 'm': mapple}

# # without enumerate()
# a=['google',' mapple', 'apple', 'python', 'orange'] 
# b={a[i][0]:a[i] for i in range(len(a)) if i%2==0}
# print(b)

# # with enumerate()
# a=['google','mapple', 'apple', 'python', 'orange'] 
# b={a[i][0]:j for i,j in zip(range(len(a)),a)}
# print(b)


# # # 3 WAP to check the length of a word in a list. If it is even add it is; else add the reverse of that as a value.
# # ex: ['google',' mapple', 'apple', 'python', 'orange'] 
# # Output: {google: google, apple: elppa}
# a=['google','mapple', 'apple', 'python', 'oranges'] 
# b={i:i if len(i)%2==0 else i[::-1] for i in a}
# print(b)


# # 4 Check that the value of a list is a palindrome or not. If palindrome key and value should be the same; else, the value should be the reverse of that.
# s = ["madam", "racecar", "apple", "hello", "madam", "noon", "level", "world", "noon"]
# b={i:i if i==i [::-1] else i[::-1] for i in s}
# print(b)


# #  5. ex: s = 'good morning'
# #    Output: {good: GOOD, morning: MORNING}
# s = 'good morning'
# a={i:i.upper() for i in s.split()}
# print(a)


# # #  6 Create a dictionary: if the length is odd, make the reverse of that as value, else add the length of the word as a value.
# s = ['rosemary flower', 'marigold flower', 'sun flower', 'banyan tree', 'mango tree']
# result = {i: len(i) if len(i) % 2 == 0 else i[::-1] for i in s}
# print(result)


# # # 7 Fetch only the 'flower' from the list by applying list comprehension.
# s = ['rosemary flower', 'marigold flower', 'sun flower', 'banyan tree', 'mango tree']
# flowers = ['flower' for i in s if 'flower' in i]
# print(flowers)
