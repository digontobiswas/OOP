numbers=[12,56,98,78,56,12,6,98]

for number in numbers:
    print(number)

# here index is not availavle 
# by using below code we can get also index
for i, num in enumerate(numbers):
    print(i, num)