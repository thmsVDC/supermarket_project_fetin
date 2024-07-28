from database.database import Database
from database.supermarket.supermarket_database_management import (create_product, read_product, update_product, delete_product)
from database.manager.manager_database_management import create_manager, read_manager, update_manager, delete_manager

db = Database(database="fetin", collection="supermarket")


def clear_screen():
    print("\n" * 50)


def show_menu():
    print("1. Supermarket menu")
    print("2. Manager menu")
    print("3. Exit")


def show_supermarket_menu():
    print("Welcome!")
    print("1. Add a product")
    print("2. Search for a product")
    print("3. Edit a product")
    print("4. Delete a product")
    print("5. Back")
    choice = input("Enter your choice: ")

    clear_screen()

    return choice


def show_manager_menu():
    print("Welcome!")
    print("1. Add a manager")
    print("2. Search for a manager")
    print("3. Edit a manager")
    print("4. Delete a manager")
    print("5. Back")
    choice = input("Enter your choice: ")

    clear_screen()

    return choice


def supermarket_management():
    while True:
        clear_screen()
        choice = show_supermarket_menu()

        clear_screen()

        match choice:
            case '1':
                create_product()
                input("Press Enter to continue...")

            case '2':
                read_product()
                input("Press Enter to continue...")

            case '3':
                update_product()
                input("Press Enter to continue...")

            case '4':
                delete_product()
                input("Press Enter to continue...")

            case '5':
                print("Backing to main menu...")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")
                input("Press Enter to continue...")


def manager_management():
    while True:
        clear_screen()
        choice = show_manager_menu()

        clear_screen()

        match choice:
            case '1':
                create_manager()
                input("Press Enter to continue...")

            case '2':
                read_manager()
                input("Press Enter to continue...")

            case '3':
                update_manager()
                input("Press Enter to continue...")

            case '4':
                delete_manager()
                input("Press Enter to continue...")

            case '5':
                print("Backing to main menu...")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")
                input("Press Enter to continue...")


def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Enter your choice: ")

        clear_screen()

        match choice:
            case '1':
                supermarket_management()
            case '2':
                manager_management()
            case '3':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 3.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    main()
