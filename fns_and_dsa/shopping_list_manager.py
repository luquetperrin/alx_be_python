def display_menu():
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item: ")
            shopping_list.append(item)

        elif choice == '2':
            item = input("Enter item: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item not found")

        elif choice == '3':
            for i in shopping_list:
                print(i)

        elif choice == '4':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



