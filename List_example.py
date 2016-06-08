l1_example=["a","b","c"]

#This is how you can give single line comment.
"""This is how
we can give multiple line comment"""

"""TRIAL is its possible to use mutiple line comment syntax and give just one line comment: Conclusion--> It works"""


print(l1_example[1])           # """ This is the proof that the mutiple line comment doesn't work in case, it you are trying to give in a line where code is there, Try removing # and run"""

print(len(l1_example))         #len fucntion can be used to get the lenght of list

l1_example.append("d")         #adding new value at the end of a list

# print("After appennd " + l1_example) # try to understand why it was not working and try to find out is there any possible method to print the "After append" with the list in same command.


print("After append")
print(l1_example)


l1_example.pop()                # Notice this line is just poping out the last element of the list but uts not actually printing it on console automatically for that you need to use below 
print(l1_example.pop())         # Notice that here the pop is popping out 'c' instead of 'd'. Bcasue pop is running second time here
print(l1_example)           


l1_example.extend(["h","i"])    # extend can be used to add the new list at the end of a alreday existing list
print(l1_example.extend(["k","l"]))  #Notice that this command is printing nothing but "None".
# print(/n)                     # Find how to print a blank line, tab space in pyhton
print("/n")
print(l1_example)               # Find out how to print a blank line with other variable in same line, for example print(/n l1example).


#l1_example.remove()            #remove method will not work without an argument, for example l1_example.remove().
#print(l1_example.remove(k))    # find out why print method doesn't print anything in following command.
# above command is not working because k is not given in side quotes --> 'k'
print(l1_example.remove('l'))   #Notice that this command is printing nothing but "None".
l1_example.remove('k')
print(l1_example)          


print(l1_example.insert(1,"ashish")) #Notice that this command is printing nothing but "None".
print(l1_example)                    #Insert method do not work if you want to insert mutiple values.







