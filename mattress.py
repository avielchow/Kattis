dimensions = input().split()
dimensions = [int(x) for x in dimensions]
box = [dimensions[0], dimensions[1]]
mattress = [dimensions[2],dimensions[3]]

box.sort()
mattress.sort()

if box[0] >= mattress[0]:
    if box[1] >= mattress[1]:
        print ("yes")
    else:
        print ("no")
else:
    print ("no")
