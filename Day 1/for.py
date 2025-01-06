number = [5,10,15,20,25]
sum =0
for num in number: #here num is meaning like i
    print(num)
    sum= sum+num
print("sum is",sum)
# for loop in charrecter
text="pagla howar tore"

for i in text:
    if i==" ":
        continue
    print(i)

#printing a secuence number like 1 t0 100 in python can be by using range= range(start, end+1)

print(range(1, 11)) #for printing 1 to 10 but output is range(1, 11)

for i in range(1,11):
    print(i)    #this output is 1 to 10 print

# range(start, end+1, increase/decrease)

for a in range(10, 0, -2):
    print(a)   #it will be output 10 to 2 