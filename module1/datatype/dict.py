student_details = {
    "name" : "Kannan",
    "dept" : "IMS", 
    "batch" : 30,
    "mobile_no" : 9875632174,
    "personal_details": {
        "fatherName" : "SAS",
        "occupation": "Business"
    },
    "name" : "varun"
}


# print(student_details, type(student_details))

print(student_details["name"])
print(student_details["personal_details"]["fatherName"])

print(type(student_details["mobile_no"]))