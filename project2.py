#WRITE A TABLES FROM 1 TO 5 (Upto 10 times)
s=1
while s<=5:
    print("TABLE",s,"\n")
    i=1
    while i<=10:
        print(s,'*',i,'=',s*i)
        i+=1
    print('\n')
    s+=1
