#Benjamin Holman, SPC ID 2371353
'''
Define two separate functions
the both will take the radius of a circle
as an argument.
the first function will return the area
the other will be a void function that prints the circumference
the main function promts the user for the radius
and then executes the function
'''
#import math so I can use it Pi
import math as ma
#define first function for area
def total_area(r):
    return ma.pi * r **2
#define function for the circumference
def circum(r):
    circumference = 2 * ma.pi * r
    print(f'The circumference is {circumference:,.3f}')

    

def main():
    #get user input
   radius = float(input('Enter radius of circle '))
   #run the two separate functions by calling them now
   area = total_area(radius)
   print(f'The area of a circle with radius of {radius} is {area:,.4f}')
   circum(radius)
#end the code with this so I can use the functions elsewhere
if __name__ == '__main__':
    main()
