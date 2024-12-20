tickets_available = 100
book_tickets = True

while book_tickets:
    if book_tickets:
        print("you can book ticket")
        user_data = int(input("how many tickets you want?"))
        tickets_available = tickets_available-user_data
        print(tickets_available)
        if tickets_available <= 0:
            book_tickets = False

if book_tickets == False:
        print("you can't book ticket")