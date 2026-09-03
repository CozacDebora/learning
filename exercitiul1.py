# speed = distance / time
# distance = speed * time
# time = distance / speed


print ("What would you like to calculate?")
print ("a. speed")
print ("b. distance")
print ("c. time")

calculate=input("a, b or c:")
print ("choose your values:")

if calculate == "a":
    distance=float(input("distance:"))
    time=float(input("time:"))
    speed=distance/time
    print (f"speed = {speed}")
elif calculate == "b":
    speed=float(input("speed:"))
    time=float(input("time:"))
    distance=speed*time
    print (f"distance = {distance}")
elif calculate == "c":
    speed=float(input("speed:"))
    distance=float(input("distance:"))
    time=distance/speed
    print(f"time = {time}")
else: print("eroare")