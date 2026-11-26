records = []

while True:
    print("\n===== LIBRARY FINE MANAGEMENT SYSTEM =====")
    print("1. Calculate Fine")
    print("2. View All Records")
    print("3. Pay Fine")
    print("4. Search student")
    print("5 Delete student")
    print("6. view fine smmary")
    print("7. Exit")

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
    elif choice=="4":
        name=input("enter student name to search:")
        found=False

        for record in records:
            if record[0].lower()==name.lower():
                print("\n Student:",record[0])
                print("Book:",record[1])
                print("Fine:",record[2])
                print("Status:",record[4])
                found=True
                if found==False:
                    print("student record not found")

    elif choice=="5":
        if len(records)==0:
            print("no records to delete")
        else:
            for i,record in enumerate(records,1):
                print(i,record[0],"-",record[1])
                number=int(input("Enter record number to delete:"))

                if 1<=number<=len(records):
                    records.pop(number-1)
                    print("Record deleted succesfully!")
                else:
                    print("Invalid record number.")
    
    

    elif choice=="6":
        total=0
        pending=0
        paid=0

        for record in records:
            total +=record[3]

            if record[4]=="unpaid":
                pending +=record[3]
            else:
                paid +=record[3]
                print("\n==== FINE SUMMARY ====")
                print("Total fine: rs",total)
                print("paid amount: rs",paid)
                print("pending amount: rs",pending)

    elif choice == "7":
        print("Thank you for using Library Fine Management System!")
        break

    else:
        print("Invalid choice! Please try again.")