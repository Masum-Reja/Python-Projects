import json
filename = ("info.json")

def Choise():
    print("I N F O R M A T I O N  D A T A ")
    print("Data Management System")
    print("(1) View data")
    print("(2) Add data")
    print("(3) Delete data")
    print("(4) Exit")

def view_data():
    with open(filename, "r") as f:
        temp = json.load(f)
        for entry in temp():
            f_name = entry["f_name"]
            l_name = entry["l_name"]
            id = entry["id"]
            section = entry["section"]
            dept = entry["dept"]
            email = entry["email"]
            number= entry["number"]
            end = entry["end"]

            print(f"First Name of Person : {f_name}")
            print(f"Last Name of Person : {l_name}")
            print(f"Last Name of Person : {id}")
            print(f"Last Name of Person : {section}")
            print(f"Last Name of Person : {dept}")
            print(f"Last Name of Person : {email}")
            print(f"Last Name of Person : {number}")
            print(f"End of Rigon  : {end}")
            print("\n\n")

def add_data():
    item_data={ }
    with open (filename,"r") as f:
        temp = json.load(f)
    item_data["f_name"] = input("First Name:")
    item_data["l_name"] = input("Last Name:")
    item_data["id"] = input("ID:")
    item_data["section"] = input("Section:")
    item_data["dpt"] = input("Department:")
    item_data["email"] = input("Email:")
    item_data["number"] = input("Contact Number:")
    item_data["end"] = input(f"End of this Rigon :")

    temp.append(item_data)
    with open (filename,"w") as f:
         json.dumps (temp, indent=4)

while True:
        Choise()
        choise = input(" \n Enter Number: ")

        if choise=="1":
            view_data()

        elif choise=="2":
            add_data()

        elif choise=="3":
            print("Delete : \n")

        elif choise=="4":
            print("Exit Program....!!")

            break

        else:
            print("Wrong Selection, Please Enter valid Input..")