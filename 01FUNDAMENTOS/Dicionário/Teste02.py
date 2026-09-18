employee = {
    "name": "Marcos",
    "position": "Analyst",
    "salary": 3500
}

employee["salary"] += 500

for  key, value in employee.items():
    print(key, ":" ,value)