def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f" '{item}' has been added to shoppin list.")
        
        elif choice == "2":
            item = input("Enter the item to add: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}' has been added to shoppin list.")
            else:
                print(f" '{item}' was not found in your shopping list.")
            
        elif choice == "3":
           if item in shopping_list:
               print("Your shopping list:")
               for i, item in enumerate(shopping_list, start=1):
                   (f"{i}. {item}")
                   
        elif choice == "4":
            print("Exiting shopping list Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()