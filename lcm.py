num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2nd number: "))
num3=int(input("enter the 3rd number: "))
big=max(num1,num2,num3)
if big%num1==0 and big%num2==0 and big%num3==0:
    print(f"{big} is the lcm")
else:
    temp=big
    while True:
        if temp%num1==0 and temp%num2==0 and temp%num3==0:
            print(f"{temp} is the lcm")
            break
        temp+=big