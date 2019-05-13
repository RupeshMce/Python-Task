num= int(input())
#num = 3
nextval = 1

for i in range(1,num+1):
    #print(i)
    if (i%2!=0):
        for j in range(i):
            print(nextval,end=" ")
            nextval +=1
             
        #print("\n")
    else:
        endval=nextval +i
        for j in range(i):
           # print(endval)
            endval -= 1
            print(endval,end=" ")
            nextval+=1
    print(" ")
        