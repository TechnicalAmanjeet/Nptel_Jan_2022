# implementation of anagrams.

str1 = input("Enter 1st String : ")
str2 = input("Enter 2nd string : ")

# print(sorted(list(str1)))

if sorted(list(str1)) == sorted(list(str2)):
    print(f"{str1} and {str2} are anagrams of each other.")
else:
    print(f"{str1} and {str2} are not anagrams of each other.")