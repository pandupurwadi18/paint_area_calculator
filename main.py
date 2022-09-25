# -- Paint Area Calculator --
# Pandu Purwadi

#packages math to round up
import math

#makes definition to calculate paint area
def paint_calc(height, width, cover):
    result = math.ceil((height*width)/cover)
    print(f"You'll need {result} cans of paint.")

#input user 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)