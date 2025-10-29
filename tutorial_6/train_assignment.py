# train -> tuple -> (name, number, source, destination)
train1 = ("Anandvihar Terminal Expresway",15058,"ghaziabad","gorakhpur")
train2= ("Gomti expresway",12420,"ghaziabd","lucknow")
train3= ("Gorakhpur Intercity",15032,"lucknow","gorakhpur")
train4= ("Vaishali Expresway",12553,"gorakhpur","ghaziabad")

trains =[ train1 , train2 , train3 , train4 ]



#available routes
available_routes= {
    "ghaziabad - gorakhpur",
    "ghaziabad - lucknow",
    "lucknow - gorakhpur",
    "gorakhpur - ghaziabad"
}

# station codes & Train schedule
station_code= {
    "GZB" : "ghaziabad",
    "GKp" : "gorakhpur",
    "LKO" : "lucknow"
}

#train schedule 
train_schedule = {
    15058 : "departure: 17:45, arrival: 7:20 ",
    12420 : "departure: 13:31, arrival: 21:30 ",
    15032 : "departure: 16:05, arrival: 21:30 ",
    12553 : "departure: 16:55, arrival: 5:38 ",
}

print("TRAINS DETAIL")
for train in trains:
    print(f"train:{train[0]}, No. :{train[1]}, route : {train[2]}-{train[3]}")
print("Available routes")
print(available_routes) 

print("station code") 
for code , station in station_code.items():
    print(f"{code} : {station}")

print("train schedule")
for number, schedule in train_schedule.items():
    print(f"Train No. {number} : {schedule}")