sum=0;
avg=0;
numOfNums=0;
n=0;
while(n!=-1):
    n = float(input("Enter number: "))
    if (n==-1):
        break
    
    sum+=n
    numOfNums+=1;

avg=sum/numOfNums

print("Avg:",avg)
print("sum:",sum)
