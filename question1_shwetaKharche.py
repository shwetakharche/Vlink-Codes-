n=int(input())
count=0
if(n<0):
    print("please provide a positive valid positive integer")
else:
    for i in range(1,n+1):
        if(i*3<n):
            count+=1
    print(count)
