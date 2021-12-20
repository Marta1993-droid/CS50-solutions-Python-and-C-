while True:
    try:
        popstart = int(input("Start size:"))
        popend = int(input("End size"))
    except ValueError:
        print("Enter a valid value")
        continue
    else:
        break

year = 0
while popstart<popend:
    popstart = popstart + (popstart/3) - (popstart/4);
    year+=1
print (year)

