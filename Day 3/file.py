#file create open and write
with open('message.txt','w') as file:
    file.write("i love you, Phython!")

# append in file
with open('message.txt','a') as file:
    file.write("You are the best language")

#read and terminal output

with open("abc.txt","w") as a:
    a.write("Hello alphabet")
with open('abc.txt','r') as a:
    text=a.read()
print(text)
   

