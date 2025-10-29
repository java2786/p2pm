""" 
Assignment 1: Indian Railway System
Create a program that manages train information using appropriate data structures: 
    1. Use tuples for train details (name, number, source, destination) 
    2. Use sets for available routes 
    3. Use dictionaries for station codes and train schedules
"""

train1 = {
    "1234": (
        ("Anandvihar Terminal Expresway",15058,"ghaziabad","gorakhpur"), 
        {{"gzb":("15:43","15:53")},{"pune":("17:09","17:15")},{"mumbai":("21:00","21:;23")},{"gorakhpur":{"23:47","-"}}}
    )
}

station_codes = {
    "gzb": "ghazibad",
    "ndl": "New Delhi"
}

trains = [train1]