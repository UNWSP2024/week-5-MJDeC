# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.
    ######################
    # WRITE YOUR CODE HERE
kilometers=int(input('Please enter the kilometer distance you would like converted to miles.'))
def conversion():
    miles=(kilometers*0.6214)
    print('That distance in miles is ',format(miles, '.2f'),'.')

conversion()
