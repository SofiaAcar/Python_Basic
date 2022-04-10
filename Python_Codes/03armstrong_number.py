# Armstrong Number
num1 = input("Enter a number to check: ")
total = 0
allowed = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

if set(num1) - allowed == set():
    for i in num1:
        total += pow(int(i), len(num1))
    if total == int(num1):
        print(num1, "is an Armstrong number.")
    else:
        print(num1, "is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numeric, \
float, or negative values!")
