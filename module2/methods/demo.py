#string format:

# response = "Hi from {}, and i'm welcoming you to the event {}"
response = "Hi from {name}, and i'm welcoming you to the event {event}"


# print(response.format("New year party","Kannan"))
print(response.format(event="New year party",name="Kannan"))

statement = "100$"

value = f"i have the amount of {statement}"
print(value)