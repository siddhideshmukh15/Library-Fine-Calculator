print("==== LIBRARY FINE CALCLATOR ====")

while True:
    print("\n 1.Calulator Fine")
    print("2.Exit")

    choice=input("Enter your choice:")

    if choice =="1":
        book_name=input("Enter book name:")
        days=int(input("Enter number of late days:"))

        if days<0:
            print("Invalid number of days!")

        elif days==0:
            fine=0
            print("Book returned on time.No fine!")
        elif days<=5:
            fine=days*2
        elif days<=10:
            fine=(5*2)+(days-5)*5

        else:
            fine=(5*2)+(5*5)+(days-10)*10
        if days>=0:
            print("\n==== FINE DETAILS ====")
            print("Book Name:",book_name)
            print("Late Days:",days)
            print("Total Fine: rs",fine)
    elif choice=="2":
        print("Thank you for using Library Fine calculator!")
        break
    else:
        print("Invalid choice!please try again.")