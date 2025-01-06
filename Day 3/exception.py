# result= 45/0
# this code will be show zerodivision error

# this error i can handel with try execpt

try:
    result=45/0
except:
    print("error happend")
print("done")

#error but then code execute, so we can handel error by this method
try:
    result=45/0
except:
    print("error happend")

finally:
    print("error but code execute and i am here")
print("done")