import db


def func():
    name = input("Kindly enter your name: ")
    print(f"Hello {name}! Here are the available functions:")
    functions = ['Insert', 'Delete', 'Orderby', 'Display']
    for idx, func_name in enumerate(functions, start=1):
        print(f"{idx}. {func_name}")

    while True:
        try:
            choice = int(input("Select the number of the function you want to perform (1-4): "))
            if choice == 1:
                db.insert()
            elif choice == 2:
                db.delete_one()
            elif choice == 3:
                db.orderby()
            elif choice == 4:
                db.display()
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


