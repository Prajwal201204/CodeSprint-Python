# map

# # 1 use map() to convert a list of strings to uppercase:
# # out=words=['apple','banana','cherry']
# word=['apple','banana','cherry']
# uppers=map(lambda x:x.upper(),word)
# print(list(uppers))


# # 2 add two lists element-wise using map():
# a=[1,2,3]
# b=[4,5,6]
# c=map(lambda x,y:x+y,a,b)
# print(list(c))
      

# # 5. Use map() to multiply each element by its index:
# nums = [10, 20, 30, 40]
# result = list(map(lambda x: x[1]*x[0], enumerate(nums)))
# print(result) 


# # 6. Convert a list of temperatures in Celsius to Fahrenheit using map():
# celsius = [0, 20, 37, 100]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit) 


# # 7. Use map() to strip whitespace from a list of strings:
# names = [' Alice ', ' Bob ', ' Charlie ']
# stripped = list(map(str.strip, names))
# print(stripped)  


# # 8. Given a list of strings containing numbers, convert them to integers using map():
# str_numbers = ['10', '20', '30', '40']
# integers = list(map(int, str_numbers))
# print(integers) 


# # 9. Use map() to compute the cube of numbers in a list:
# values = [2, 3, 4, 5]
# cubes = list(map(lambda x: x**3, values))
# print(cubes) 


# # 10. Combine first and last names using map():
# first_names = ['John', 'Jane', 'Alice']
# last_names = ['Doe', 'Smith', 'Johnson']
# full_names = list(map(lambda f, l: f + ' ' + l, first_names, last_names))
# print(full_names)  


# # 11. Convert a list of binary strings to decimal using map():
# binaries = ['1010', '1111', '0001', '1001']
# decimals = list(map(lambda x: int(x, 2), binaries))
# print(decimals) 


# # 12. Use map() to round all floats in a list to 2 decimal places:
# floats = [3.14159, 2.71828, 1.61803]
# rounded = list(map(lambda x: round(x, 2), floats))
# print(rounded)  


# # 13. Capitalize the first letter of each word using map():
# words = ['hello', 'world', 'python']
# capitalized = list(map(str.capitalize, words))
# print(capitalized)  


# # 14. Use map() to convert a list of (feet, inches) to total inches:
# measurements = [(5, 10), (6, 2), (4, 11)]
# total_inches = list(map(lambda x: x[0]*12 + x[1], measurements))
# print(total_inches) 


# # 15. Given a list of full names as strings, use map() to split them into first and last name:
# full_names = ['John Doe', 'Jane Smith', 'Alice Johnson']
# split_names = list(map(lambda x: x.split(), full_names))
# print(split_names)  