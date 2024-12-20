def my_function(x):
    if x == 0:
        return 0
    else:
        return my_function(x - 1) + x 

print(my_function(5)) #this will work fine
print(my_function(1000)) #this will cause RecursionError