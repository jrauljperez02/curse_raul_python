#make a code that sum all the numbers in

# sum = 0
# for number in range (0,101,2):
    # sum += number
# print(f"Sum = {sum}")


sum = 0
for number in range (0,101):
    if number%2==0:
        sum += number
print(f"Sum = {sum}")
