
counter = 0
vehicles = ["type1","type2","type3","type4","type5","type6"]
#routes = [10,11,12,13,14,20,21,22,23,24,30,31,32,33,34,40,41,42,43,44,130,131,132,133,134,140,141,142,143,144]
#routes = [1,4]
routes = [0,1,2,3,4,5,6,7,8,9,10,11]
vcounter = 0
rcounter = 0

for i in range(2000):

    if i%5 == 0:
        counter +=5

    if i%10 == 0:
        vcounter += 1


    if vcounter-6 == 0:
        vcounter=0

    if rcounter-12 == 0:
        rcounter=0


    vehcile_id = vehicles[vcounter]+str(int(i))
    route_id = "r"+str(routes[rcounter])
    print("<vehicle id='"'{}'"' type='"'{}'"' route='"'{}'"' depart='"'{}'"'/>".format(i,vehicles[vcounter],route_id,counter))
    rcounter += 1