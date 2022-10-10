car={
        "Brand" : ["Tesla","hello"],
        "Model" : "X",
        "Year"  : "2020"
        }

#x=car.keys() #Returns the list of keys in dictionary
#y=car.values() #Returns the values of dictionary
#car["color"] = "Black"
#print(car[Brand])

#3print(car)


#print(x)
#print(y)

v=input(print("Enter the values? "))
if v in car.values():
    print(car.items())

