# Prime Numbers
kalan = []
number = int(input("Enter a number: "))
for i in range(1,number):
    kalan.append(number % i)
if number == 2:
    print(f"({number}) is a prime number.")
elif 0 in kalan[1:]:
    print(f"({number}) is not a prime number.")
else:
    print(f"({number}) is a prime number.")