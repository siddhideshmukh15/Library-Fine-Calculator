records = []

while True:
    print("\n===== LIBRARY FINE MANAGEMENT SYSTEM =====")
    print("1. Calculate Fine")
    print("2. View All Records")
    print("3. Pay Fine")
    print("4. Search Student")
    print("5. Delete Record")
    print("6. Fine Summary")
    print("7. View Unpaid Records")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student = input("Enter student name: ")
        book = input("Enter book name: ")
        days = int(input("Enter late days: "))

        if days < 0:
            print("Invalid days!")
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

            print("Fine calculated!")
            print("Total Fine: Rs.", fine)

    elif choice == "2":
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
                    print("Already paid.")
            else:
                print("Invalid number.")

    elif choice == "4":
        name = input("Enter student name: ")
        found = False

        for record in records:
            if record[0].lower() == name.lower():
                print("Student:", record[0])
                print("Book:", record[1])
                print("Fine: Rs.", record[3])
                print("Status:", record[4])
                found = True

        if found == False:
            print("Record not found.")

    elif choice == "5":
        if len(records) == 0:
            print("No records to delete.")
        else:
            for i, record in enumerate(records, 1):
                print(i, record[0], "-", record[1])

            number = int(input("Enter record number to delete: "))

            if 1 <= number <= len(records):
                records.pop(number - 1)
                print("Record deleted!")
            else:
                print("Invalid number.")

    elif choice == "6":
        total = 0
        paid = 0
        pending = 0

        for record in records:
            total += record[3]

            if record[4] == "Paid":
                paid += record[3]
            else:
                pending += record[3]

        print("\n===== FINE SUMMARY =====")
        print("Total Records:", len(records))
        print("Total Fine: Rs.", total)
        print("Paid Amount: Rs.", paid)
        print("Pending Amount: Rs.", pending)

    elif choice == "7":
        found = False

        for i, record in enumerate(records, 1):
            if record[4] == "Unpaid":
                print(i, record[0], "-", record[1],
                      "- Rs.", record[3])
                found = True

        if found == False:
            print("No unpaid records.")


    elif choice == "8":
        print("Thank you for using Library Fine Management System!")
        break

    else:
        print("Invalid choice!")