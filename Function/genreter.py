#  what is genreter   
#  it is procces of creating new collection from a function that is non hase genrater.
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
# 
# 2 print 1 to 10 squre using genrater
# def sqr(): 
#       for i in range(1,11):
#             yield i**2
# print(list(sqr()))
      
      
# # 3 print palindrom only
# l=['racecar','abcode','aakash','nitin']
# def extract_palindrom(l):
#     for i in l :
#         if i==i[::-1]:
#             yield i
# print(list(extract_palindrom(l)))


# # 4 print ord number a to z
# def get():
#     for i in range(97,123):
#         yield chr(i),i
# print(dict(get()))


# # 5 write a program a extract all the prime number to given range
# def prime(n):
#     for i in range(2,n):
#         if n%2==0:
#             return False
#     return True
# lower_range=int(input('Enter the lower Range :'))
# higher_range=int(input('Enter the higher Range :'))
# def prime_series(lower_range,higher_range):
#     for i in range(lower_range,higher_range):
#         if prime(i):
#             yield i
# print(list(prime_series(lower_range,higher_range)))
        
        
# 6 print a string in upper to lower and lower to upper. ex: s='GenER@tr2' 
# s='GenER@tr2'



