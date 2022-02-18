# You are given a string S. Write a function count_letters which will return a dictionary containing letters 
# (including special character) in string S as keys and their count in string S as values

def count_letters(S):
    dict = {}
    for key in S:
        if key not in dict.keys():
            dict[key] = S.count(key)
    return dict


S = input("enter values : ")
d = count_letters(S)
print(d)
# s = "Hii Amanjeet"
# print(s.count("e"))
