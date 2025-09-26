def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice_raw = input("Enter your choice: ")
        try:
            choice = int(choice_raw)
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item == "":
                print("Item cannot be empty.")
            else:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                for idx, itm in enumerate(shopping_list, start=1):
                    print(f"{idx}. {itm}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

