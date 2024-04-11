user = []

def user_create():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    contact = int(input("Enter user contact: "))
    address = input("Enter user address: ")
    dis = {"name": name, "email": email, "contact": contact, "address": address}
    user.append(dis)
    return dis

def user_list():
    for index, value in enumerate(user):
        print(f"User {index+1}: ")
        print(f"Name: {value['name']}")
        print(f"Email: {value['email']}")
        print(f"Contact: {value['contact']}")
        print(f"Address: {value['address']}")
        print()

def user_list_edit():
    user_list()
    id_num = int(input("Enter the index of the user you want to edit: ")) - 1
    if 0 <= id_num < len(user):
        user[id_num]["name"] = input("Enter new name: ")
        user[id_num]["email"] = input("Enter new email: ")
        user[id_num]["contact"] = int(input("Enter new contact: "))
        user[id_num]["address"] = input("Enter new address: ")
    else:
        print("Invalid index")

def delete_user():
    user_list()
    id_num = int(input("Enter the index of the user you want to delete: ")) - 1
    if 0 <= id_num < len(user):
        del user[id_num]
        print("User is deleted successfully ")
    else:
        print("Invalid index")

while True:
    print("\nUser Management System")
    print("1. Create User")
    print("2. List user")
    print("3. Edit User")
    print("4. Delete User")
    print("5. Exit")

    select = input("Enter your choice: ")

    if select == '1':
        result = user_create()
        print(result)
    elif select == '2':
        user_list()
    elif select == '3':
        user_list_edit()
    elif select == '4':
        delete_user()
    else:
        break