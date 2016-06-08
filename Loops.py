ilist=['TCS','Wipro','Infosys']   #Note: '' and "" both works fine while defining list

print(ilist)

for i in ilist:
    print(i)


count=0
while count < len(ilist):
    print(ilist[count])
    count=count+1
    #count++                 invaliad syntax in python (Check if can be used after adding some library)



#Code to insert the founding year of companies above
ilist.insert(1,1968)
ilist.insert(3,1981)
ilist.append(1945)
print(ilist)

#Instead of inserting values you can delcare the list freshly.(Beacase inserting at right place is easy only for small list.
#Incase of larg list it will be difficult

#We can also have nested list.
ilist.insert(2,['Mumbai','Delhi','Kochi','Banglore','Pune'])
ilist.insert(5,['Pune','Banagalore','Pune'])
#ilist.insert(8,['Bangalore','Chandigarh','Pune'])           #Check why it is not working.
ilist.insert(len(ilist),['Bangalore','Chandigarh','Pune'])      

print(ilist)



print(ilist[3][2])         #By mistake I found: using ilist[3][2] actually we are accessing, 2nd index i.e 3rd character of 3rd indexed element i.e wipro --->Final result 'p'

print(ilist[2][2])


ilist.insert(2,3,"ITPL","Vedhi","Electronic city")

#try to find out how you can insert list within a list within a list i.e 3rd nested list? Is it possible to use insert for that?

