records = []

while True:
    print("\n===== LIBRARY FINE MANAGEMENT SYSTEM =====")
    print("1. Calculate Fine")
    print("2. View All Records")
    print("3. Pay Fine")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = input("Enter student name: ")
        book = input("Enter book name: ")
        days = int(input("Enter late days: "))

        if days < 0:
            print("Invalid number of days!")

        else:
            if days == 0:
                fine = 0
            elif days <= 5:
                fine = days * 2
            elif days <= 10:
                fine = 10 + (days - 5) * 5
            else:
                fine = 35 + (days - 10) * 10

            records.append([student, book, days, fine, "Unpaid"])

            print("\nFine calculated successfully!")
            print("Student:", student)
            print("Book:", book)
            print("Total Fine: Rs.", fine)

    elif choice == "2":
        print("\n===== ALL FINE RECORDS =====")

        if len(records) == 0:
            print("No records found.")
        else:
            for i, record in enumerate(records, 1):
                print("\nRecord:", i)
                print("Student:", record[0])
                print("Book:", record[1])
                print("Late Days:", record[2])
                print("Fine: Rs.", record[3])
                print("Status:", record[4])

    elif choice == "3":
        if len(records) == 0:
            print("No records found.")
        else:
            for i, record in enumerate(records, 1):
                print(i, record[0], "-", record[1],
                      "- Rs.", record[3], "-", record[4])

            number = int(input("Enter record number to pay: "))

            if 1 <= number <= len(records):
                if records[number - 1][4] == "Unpaid":
                    records[number - 1][4] = "Paid"
                    print("Fine paid successfully!")
                else:
                    print("Fine is already paid.")
            else:
                print("Invalid record number.")

    

    elif choice == "4":
        print("Thank you for using Library Fine Management System!")
        break

    else:
        print("Invalid choice! Please try again.")