#i write a function in other place,if i write now again this function then it will be time killer and 
#also memeory killer . 
#we can use module for it.
from function import function  #import from function file and import function(function is a function inside the function file)
result= function(100)
print(result)

#import from kargs_multiple.py and import full_name function
from kargs_multiple import full_name as name #here i just write name as a sort from of full_name function if i call it name then work will be as full_name
nam=name('digonto', 'biswas')
print(nam)

#but here problem is full function is running and printing


#if i want to import full file then just need to write 

from deafult_args_kargs import *  # every file is imported and running