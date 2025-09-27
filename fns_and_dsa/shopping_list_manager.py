# shopping_list_manager.py
def display_menu():
    """Show the menu options to the user."""
    print("\nShopping List Manager")
    print("---------------------")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Start with an empty shopping list
    shopping_list = []

    # Keep asking the user for actions until they choose to exit
    while True:
        display_menu()
        # Read the user's menu choice and remove extra spaces
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item:  # only add non-empty strings
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("No item entered. Nothing was added.")

        elif choice == '2':
            # Remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue

            item = input("Enter the item to remove: ").strip()
            if not item:
                print("No item entered. Nothing was removed.")
                continue

            # Try to find a case-insensitive match in the list
            found_index = None
            for index, existing in enumerate(shopping_list):
                if existing.lower() == item.lower():
                    found_index = index
                    break

            if found_index is not None:
                removed = shopping_list.pop(found_index)
                print(f"'{removed}' has been removed from your shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")

        elif choice == '3':
            # View the current shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour shopping list:")
                for i, itm in enumerate(shopping_list, start=1):
                    print(f"{i}. {itm}")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices gracefully
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, exit nicely instead of showing a traceback
        print("\nInterrupted. Goodbye!")
