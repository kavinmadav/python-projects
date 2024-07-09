#Find even and odd numbers from a list, and store them separately in a new list


list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

evenlist=[]
oddlist=[]

print("The numbers in  the list",list)
for num in list:
      if num %2 == 0:
         evenlist.append(num)
      else:
          oddlist.append(num)
print("\nThe odd numbers are",oddlist)
print("The even numbers are",evenlist)