x, y = input("Input the (x,y) coordinate with one decimal place :").split(' ')
x = round(float(x), 1)
y = round(float(y), 1)

if (x == 0.0):
    print("({}, {})".format(x, y), "is on the y axis")
elif(y == 0.0):
    print("({}, {})".format(x, y), "is on the x axis")
elif(x > 0.0 and y > 0.0 ):
    print("({}, {})".format(x, y), "is in quadrant I")
elif(x < 0.0 and y > 0.0):
    print("({}, {})".format(x, y), "is in quadrant II")
elif (x < 0.0 and y < 0.0):
    print("({}, {})".format(x, y), "is in quadrant III")
else:
    print("({}, {})".format(x, y), "is in quadrant IV")


