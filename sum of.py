a=int(input("Enter your limit="))
if a<0:
    print("Enter a poisitive number")
else:
    sum=0
    for i in range(a, 0, -1):
        sum+=i
    print(sum)
   
