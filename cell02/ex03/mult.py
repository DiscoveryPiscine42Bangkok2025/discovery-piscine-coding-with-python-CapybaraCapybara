first = int(input("Enter the first number:"))
sec = int(input("Enter the second number:"))
sum = first*sec
print(f'{first} x {sec} = {sum}')
if (sum > 0):
    print("The result is positive.")
elif (sum == 0):
    print("The result is positive and negative.")
else:
    print("The result is negative.")
