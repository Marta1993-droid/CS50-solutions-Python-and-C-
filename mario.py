height = int(input("Number of stages"))

#Print pyramid height n. Every row has # n-1

#Pyramid upside down
for i in range(height):
    height=height-1
    print ("#"*height)

#Pyramid left orientated
for i in range(height+1):
    print ("#"*i)

#Pyramid right orientated
for i in range(height+1):
    row = height-1
    print (" "*(height-i) + "#"*i)

