data = [
    {
        "name": "udin",
        "sex": "male",
        "age": 10,
        "marital": "single",
        "social": "student"
    },
    {
        "name": "ujang",
        "sex": "male",
        "age": 25,
        "marital": "married",
        "social": "employee"
    },
    {
        "name": "icih",
        "sex": "female",
        "age": 10,
        "marital": "single",
        "social": "student"
    },
    {
        "name": "eneng",
        "sex": "female",
        "age": 100,
        "marital": "married",
        "social": "employee"
    },
    {
        "name": "asep",
        "sex": "male",
        "age": 20,
        "marital": "single",
        "social": "employee"
    }
]

def group_people(data):
    groups = {}
    for item in data:
        sex = item["sex"]
        age = item["age"]
        marital = item["marital"]
        social = item["social"]
        key = (sex, age, marital, social)
        if key in groups:
            groups[key].append(item)
        else:
            groups[key] = [item]
    return groups

result = group_people(data)
print(result)
