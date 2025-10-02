def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # start with empty list

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ").strip().lower()
            if item:
                shopping_list.append(item)
                print(f" '{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == "2":
            item = input("Enter the item to remove: ").strip().lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' was not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("\n Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again later")


# Run the shopping list manager if this script is executed directly
if __name__ == "__main__":
    main()

