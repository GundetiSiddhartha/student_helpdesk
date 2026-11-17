
class StudentHelpdesk:
    def __init__(self):
        self.tickets = []

    def create_ticket(self):
        student_id = input("Enter Student ID: ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        attachment = input("Enter Attachment Name (optional): ")

        ticket = {
            "Ticket ID": len(self.tickets) + 1,
            "Student ID": student_id,
            "Category": category,
            "Description": description,
            "Attachment": attachment if attachment else "No Attachment",
            "Status": "Open"
        }

        self.tickets.append(ticket)

        print("\nTicket Created Successfully!")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")
            return

        for ticket in self.tickets:
            for key, value in ticket.items():
                print(key + ":", value)
            print("----------------------")

    def update_status(self):
        ticket_id = int(input("Enter Ticket ID: "))

        for ticket in self.tickets:
            if ticket["Ticket ID"] == ticket_id:
                status = input("Enter New Status: ")
                ticket["Status"] = status
                print("Ticket Status Updated!")
                return

        print("Ticket Not Found")


# Main Program
helpdesk = StudentHelpdesk()

while True:
    print("\n--- STUDENT HELPDESK ---")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Update Ticket Status")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        helpdesk.create_ticket()
    elif choice == "2":
        helpdesk.view_tickets()
    elif choice == "3":
        helpdesk.update_status()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
