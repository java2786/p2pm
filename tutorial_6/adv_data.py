students = {
    123: {
        "name": "Ramesh",
        "subjects": {"math":78, "physics": 81},
        "contacts": ["9876543", "demo@gmail.com"]
    },
    324: {
        "name": "Mukesh",
        "subjects": {"math":67, "physics": 90},
        "contacts": ["7878765", "test@gmail.com"]
    }
}

# print(students.get(123).get("name"))

keys = students.keys()
for key in keys:
    # print(key)
    print(students.get(key).get("name"))
    print(type(students.get(key).get("subjects")))
    print(students.get(key).get("subjects").get("math"))
    print(students.get(key).get("contacts")[0])

