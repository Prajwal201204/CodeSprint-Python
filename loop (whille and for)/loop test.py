# #  1 Shift all the zeros to right
# ls = [0, 1, 2, 3, 0, 0, 4, 5, 8, 0]
# out = [i for i in ls if i != 0] + [0] * ls.count(0)
# print(out)


# # 2 waf to get the following output
# # s = 'happy morning be safe'
# # out={'happy': 1, 'morning': 2, 'be': 1, 'safe': 2}
# # Count vowels in each word

# s = 'happy morning be safe'
# d = {}
# for word in s.split():
#     count = sum(1 for ch in word if ch in 'aeiou')
#     d[word] = count
# print(d)


# # # 3 Reverse each word 
# s = 'hai hello how are you'
# out = ' '.join(i[::-1] for i in s.split())
# print(out)


# # 4 Extract vowels from each word of a string
# s = 'hello buddy how are you'
# d = {}
# for word in s.split():
#     vowels = ''.join(ch for ch in word if ch in 'aeiou')
#     d[word] = vowels
# print(d)


# # 5  Fetch last digit without slicing or type conversion
# n = 12345
# last_digit = n % 10
# print(last_digit)


