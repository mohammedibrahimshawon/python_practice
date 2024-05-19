#argument
#print('hello')
# x=5
# y=6
# z=11

# import sys
# print ('Number of arg:',len(sys.argv),'arguments')
# print ('argument list:',str(sys.argv))
# x=int(sys.argv[2])
# y=int(sys.argv[3])
# z=x+y
# print("x=",x,"y=",y,"z=",z) 

import sys

# Printing the number of arguments and the argument list
print('Number of arguments:', len(sys.argv) - 1)  # Subtracting 1 to exclude script name
print('Argument list:', str(sys.argv))

# Checking if enough arguments are provided
if len(sys.argv) >= 4:
    # Converting command-line arguments to integers
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    # Calculating the sum of the integers
    z = x + y
    print("x =", x, ", y =", y, ", z =", z)
else:
    print("Insufficient number of arguments provided. Please provide at least 2 integers.")
