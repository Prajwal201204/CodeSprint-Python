
# # Varible scope (3-type (local ,Globle, Non local))

# # # Local
# 
# alpha=200
# def func():
#     alpha=150 
#     print('inside func :', alpha)
# func()
# print('outside': ,alpha)



# # # Globle
# 
# alpha=200
# def func():
#     global alpha
#     alpha=150 
#     print('inside func :', alpha)
# func()
# print('outside :' ,alpha)



# # # Non local 
# 
# def outer():
#     a=100
#     def inner():
#         a=120
#         print('inside inner func:',a)
#     inner()
#     print('outside inner :' ,a)
# outer()


####################################################################

# # # example
# 
# a=100
# def outer():
#     global a
#     a=120
#     def inner():
#         # global a
#         a=200
#         print('Inside inner :', a)
#     inner()
#     print('Inside outer:', a)
# outer()
# print('outside everything:', a)



