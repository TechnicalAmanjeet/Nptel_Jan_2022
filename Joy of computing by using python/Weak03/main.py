# ********* weak 3 practice **********

# List datatype in python.
# myList = range(11)  # create a list of number from 0 to 10 and stores in myList variable.
myList = [1, "Amanjeet", "Ram", "shyam"]
# print(myList)

# we can iterate through loop as well.
# for element in myList:
#     print(element)

# list datatype contains following properties.
# print(dir(list))
# print(len(dir(list)))

# ******** 2. List manipulation in python ********
myList1 = ["Amanjeet", "Ram", "Riya", "Kajal"]
# myList1.append("Neha")  # add neha at the end of the list.
# print(myList1)
#

#
# last_element_of_list = myList1.pop()  # remove last element of list and return that element
# print(myList1)
# print(last_element_of_list)
#
# myList1.remove("Ram")  # remove the element "Ram" is it's inside the list
# print(myList1)
# # print(element_after_remove)
#

#
# print(len(myList1))  # print how many element in the list.
#
# print(myList1.count("Neha"))  # print how many times neha is inside the list


# ********* 3. List operations. ***********

# myList1.sort()  # sort the list in ascending order
# print(myList1)
# myList1.insert(1, "Kismat")  # insert kismat at the index 1.
# print(myList1)
#
# myList1.reverse()  # reverse the list
# print(myList1)


# ******* 4. Slicing ***********

print(myList1[:])  # default value => mylist1[:] == mylist1 => True
print(myList1 == myList1[:])

# slicing syntax => list[start_index : end_index + 1]
# by using above syntax we will return a list which start from start_index element and goes till the end index element
first_3_element = myList1[:3]  # print first 3 element of list
print(first_3_element)

last_3_element = myList1[len(myList1)-3 : ]
# print(myList1)
print(last_3_element)

