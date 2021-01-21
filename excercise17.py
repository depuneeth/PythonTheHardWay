cars = 60
buses = 50
trains = 30
trucks = 60

if cars < buses:
    print("people strength is more")

if trains > cars:
    print("trains are lesser than cars")

if cars > trains:
    print("cars are more available than trains")

trains += 30

if trains >= cars:
    print("trains and buses are available")

if trains <= cars:
    print("train ticket rates are cheaper")


if trucks > cars:
    print("cars are not available")
elif trucks <= trains:
    print("trucks and trains carry goods")
else:
    print("this is an end")
