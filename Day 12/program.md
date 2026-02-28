def add_product():
    name = input("Enter product name: ")
    price = input("Enter price: ")

    file = open("stock.txt", "a")
    file.write(name + "," + price + "\n")
    file.close()

    print("Product added successfully!\n")

def view_products():
    file = open("stock.txt", "r")
    print("\nAvailable Products:")
    print(file.read())
    file.close()

while True:
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        break
    else:
        print("Invalid choice!\n")


output:
1.Add product
2.view product
3.Exit
Enter your choice:1

Enter product name:oil
Enter price:150
product added successfully.
