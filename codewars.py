# import itertools
# def solution(stones):
#     times = 0
#     for index in range(len(stones) - 1): 
#         if stones[index] == stones[index + 1]:
#             times += 1
#     return times


# others solution
# def solution(s):
#     return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])
# print(solution("RGBEGBRGGBBB"))
# solution("RGBEGBRGGBBB")


# Disemvowel Trolls
# def disemvowel(stri):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     return ''.join(char for char in stri if char not in vowels)
# print(disemvowel("This website is for losers LOL!"))

# Stones on the Table
# def solution(stones):
#     times = 0
#     for index in range(len(stones) - 1): 
#         if stones[index] == stones[index + 1]:
#             times += 1
#     return times


# Terminal game move function

# def move(position, roll):
#     return position+(roll*2)

#others solution on this problem

# move = lambda p,r: p+r*2
# exec("".join(map(chr,[int("".join(str({':(': 4, ':)': 0, ':/': 7, ':D': 1, ':P': 2, ':S': 3, ':{': 8, ';)': 9, '=)': 5, '=/': 6}[i]) for i in x.split())) for x in
# ":D :) :)  :D :) :D  :D :) :P  :S :P  :D :) ;)  :D :D :D  :D :D :{  :D \
# :) :D  :( :)  :D :D :P  :( :(  :S :P  :D :D :(  :( :D  =) :{  :S :P  :\
# D :D :(  :D :) :D  :D :D =/  :D :D :/  :D :D :(  :D :D :)  :S :P  :D :\
# D :P  :S :P  :( :S  :S :P  =) :)  :S :P  :( :P  :S :P  :D :D :("
# .split("  ")])))

# print(move(3,6))


# Isograms

# def is_isogram(string):
#     s = string.lower()
#     return len(set(s)) == len(s)

# print(is_isogram("aba"))  
# print(is_isogram("abc"))

# others solution
# is_isogram = lambda s: len(set(s.lower())) == len(s)

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True

# print(is_isogram("aba"))  
# print(is_isogram("abc"))






# string = "asdfg"
# st = set(string)
# stri = str(st)
# sttt = str(set(string))

# print(string)
# print(st)
# print(stri)
# print(sttt)