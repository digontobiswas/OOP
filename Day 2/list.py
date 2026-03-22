# is's similar to array
numbers= [45,50,55, 60,70,80,90,100,110,120]
print(numbers[-2]) #prnt will be 110
print(numbers[8]) #prnt will be 110

print(numbers[3:8-1])  #by this way we can devide a array and we can print out desier list arrname[start:end-1] end-1 willbe print

#step list_name[start:end:step]
print(numbers[3:8:2]) #start will be from 3 index and end will be in 7 index(8-1) and printing step will be positive 2 so , missing element will be 1 

#we can do step in revese way just need to keep before stpe (-)
print(numbers[7:2:-2])
print(numbers[4:]) #from 4th index to last
print(numbers[ :8]) # start will be from 0th inxed and end will be in 7th index (8-1)
print(numbers[:]) # SORTCUT TO COPY A LIST
print(numbers[::2]) # IT WILL BE MAINTAIN START TO END BY MY GIVERN STEP
print(numbers[::-2]) #SORTCUT TO REVERSE LIST.IT WILL BE MAINTAIN STEP IN REVERSE WAY.LIST WILL BE ALSO REVERSE

