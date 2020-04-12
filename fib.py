def Recur_Febinocci(number):
    if number<=1:
        return number
    else:
        return (Recur_Febinocci(number-1)+Recur_Febinocci(number-2))
term=int(input("Enter Number of Terms"))
if term<=0:
    print("Enter Positive Numbers Only")
else:
    print("Fibonacci Series")
    for numbers in range(term):
        print(Recur_Febinocci(numbers))
