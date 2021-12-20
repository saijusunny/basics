a=int(input("Enter your starting Value="))
b=int(input("Enter your final Value="))
if 0<a and 0<b:

    for x in range(a, b, 3):
        print(x)
    else:
        print("finally Finished")
elif 0>a and 0>b:
    print ("the starting and the ending value is negative")
elif 0>a and 0<b:
    print ("the startying value is negative")
elif 0<a and 0>b:   
     print ("the final value is negative")
