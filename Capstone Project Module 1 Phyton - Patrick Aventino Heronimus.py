print('Capstone Project Module 1')
print('Motorcycle Dealer Data\n')

motorcycle = [
    { 
    'Brand'         : 'Yamaha',
    'Name'          : 'Aerox',
    'Stock'         : 5,
    'Engine Size'   : '155 cc',
    'Petrol'        : 'Pertalite',
    'Transmission'  : 'CVT'
    },  
    {
    'Brand'         : 'Yamaha',
    'Name'          : 'NMAX',
    'Stock'         : 4,
    'Engine Size'   : '155 cc',
    'Petrol'        : 'Pertalite',
    'Transmission'  : 'CVT'
    },
    {
    'Brand'         : 'Yamaha',
    'Name'          : 'R15',
    'Stock'         : 3,
    'Engine Size'   : '150 cc',
    'Petrol'        : 'Pertamax',
    'Transmission'  : 'Manual'
    },
    {
    'Brand'         : 'Honda',
    'Name'          : 'Vario',
    'Stock'         : 6,
    'Engine Size'   : '160 cc',
    'Petrol'        : 'Pertamax',
    'Transmission'  : 'CVT'
    },
    {
    'Brand'         : 'Honda',
    'Name'          : 'CBR',
    'Stock'         : 2,
    'Engine Size'   : '250 cc',
    'Petrol'        : 'Pertamax Turbo',
    'Transmission'  : 'Manual'
    },
    {
    'Brand'         : 'Kawasaki',
    'Name'          : 'Ninja',
    'Stock'         : 2,
    'Engine Size'   : '250 cc',
    'Petrol'        : 'Pertamax Turbo',
    'Transmission'  : 'Manual'
    },
]

def option():
    while True:
        print('Welcome to Honduras Motorcycle Dealer\n')
        print('Main Menu')
        print('1. Show Motorcycle List')
        print('2. Add a Motorcycle')
        print('3. Update Motorcycle Stock')
        print('4. Delete a Motorcycle')
        print('5. Exit Program')

        input_number = (input('Please input a number: '))
        if input_number == "1":
            read_option()
        elif input_number == "2":
            create_option()
        elif input_number == "3":
            update_option()
        elif input_number == "4":
            delete_option()
        elif input_number == "5":
            print('Thankyou, See You Next Time!')
            break
        else:
            print('The number that you choose is not valid, please enter another number')

def read_option():
    while True:
        index = 0
        print('Select Your Motorcycle')
        print('1. Yamaha')
        print('2. Honda')
        print('3. Kawasaki')
        print('4. Show All')
        print('5. Back to Main Menu')

        input_read_option = input('Please input a number: ')
        if input_read_option == "1":
            print('Index\t\t| Name\t\t| Stock\t\t| Engine Size\t\t| Petrol\t\t| Transmission\t\t|')
            for i in range(len(motorcycle)):
                if motorcycle[i]['Brand'] == 'Yamaha':
                    index += 1
                    print(f"{index}\t\t| {motorcycle[i]['Name']}\t\t| {motorcycle[i]['Stock']}\t\t| {motorcycle[i]['Engine Size']}\t\t| {motorcycle[i]['Petrol']}\t\t| {motorcycle[i]['Transmission']}\t\t|")
        elif input_read_option == "2":
            print('Index\t\t| Name\t\t| Stock\t\t| Engine Size\t\t| Petrol\t\t| Transmission\t\t|')
            for i in range(len(motorcycle)):
                if motorcycle[i]['Brand'] == 'Honda':
                    index += 1
                    print(f"{index}\t\t| {motorcycle[i]['Name']}\t\t| {motorcycle[i]['Stock']}\t\t| {motorcycle[i]['Engine Size']}\t\t| {motorcycle[i]['Petrol']}\t\t| {motorcycle[i]['Transmission']}\t\t|")
        elif input_read_option == "3":
            print('Index\t\t| Name\t\t| Stock\t\t| Engine Size\t\t| Petrol\t\t| Transmission\t\t|')
            for i in range(len(motorcycle)):
                if motorcycle[i]['Brand'] == 'Kawasaki':
                    index += 1
                    print(f"{index}\t\t| {motorcycle[i]['Name']}\t\t| {motorcycle[i]['Stock']}\t\t| {motorcycle[i]['Engine Size']}\t\t| {motorcycle[i]['Petrol']}\t\t| {motorcycle[i]['Transmission']}\t\t|")
        elif input_read_option == "4":
            print('Index\t\t| Brand\t\t| Name\t\t| Stock\t\t| Engine Size\t\t| Petrol\t\t| Transmission\t\t|')
            for i in range(len(motorcycle)):
                print(f"{i+1}\t\t| {motorcycle[i]['Brand']}\t\t| {motorcycle[i]['Name']}\t\t| {motorcycle[i]['Stock']}\t\t| {motorcycle[i]['Engine Size']}\t\t| {motorcycle[i]['Petrol']}\t\t| {motorcycle[i]['Transmission']}\t\t|")
        elif input_read_option == "5":
            break
        else:
            print('The number that you choose is not valid, please enter another number')

def create_option():
    while True:
        print('Create New Motorcycle Database\n')
        print('1. Create New Data')
        print('2. Back to Previous Menu')

        input_create = input('Enter the number: ')
        if input_create == "1":
            input_function1()
        elif input_create == "2":
            return
        else:
            print('The number that you choose is not valid, please enter another number')

def input_function1():
        create_name = input('Enter the motorcycle name: ')
        for i in motorcycle:
            if i["Name"] == create_name.capitalize():
                print('Data already exist in the database')
                return
            
        create_brand = input('Enter the motorcycle brand: ')
        create_stock = int(input('Enter the motorcycle stock: '))
        create_engine_size = input('Enter the motorcycle capacity: ')
        create_petrol = input('Enter the motorcycle fuel: ')
        create_transmission = input('Enter the motorcycle transmission: ')

        while True:
            input_save_data = input('Do you want to save the data?(y/n) : ')
            if input_save_data == "y":
                motorcycle.append({
                    "Brand"         :create_brand.capitalize(),
                    "Name"          :create_name.capitalize(),
                    "Stock"         :create_stock,
                    "Engine Size"   :create_engine_size,
                    "Petrol"        :create_petrol.capitalize(),
                    "Transmission"  :create_transmission.capitalize(),
                })
                print('Data succesfully saved')
                return
            elif input_save_data == "n":
                print('Cancelled saving data')
                return
            else: 
                print('Your input is not valid, please choose y or n')
        

def update_option():
    while True:
        print('Update Motorcycle Database\n')
        print('1. Update Stock')
        print('2. Back to Previous Menu')
        input_create = input('Enter the number: ')
        if input_create == "1":
            input_function2()
        elif input_create == "2":
            return
        else:
            print('The number that you choose is not valid, please enter another number')
        
def input_function2():
    create_name = input('Enter the motorcycle name: ')
    for i in motorcycle:
        if i["Name"] == create_name.capitalize():
            print(f'Motorcycle {i["Name"]} stock is {i["Stock"]}')
            change_stock = input('Do you want to update the stock? (y/n):  ')
            if change_stock == "y":
                print('1. Add Stock')
                print('2. Decrease Stock')
                input_stock = input('Enter the number: ')
                if input_stock == "1":
                    modify_stock = int(input('Enter the number that you want to add: '))
                elif input_stock == "2":
                    modify_stock = -int(input('Enter the number that you want to decrease: '))
                else:
                    print('The number that you choose is not valid, please enter another number')
            elif change_stock == "n":
                return
            else:
                print('Your input is not valid, please choose y or n')
            
            while True:
                input_update_data = input('Do you want to save the data?(y/n) : ')
                if input_update_data == "y":
                    i["Stock"] += modify_stock
                    print("Your database has been updated")
                    print(f'Motorcycle {i["Name"]} stock is now {i["Stock"]}')
                    return
                elif input_update_data == "n":
                    print('Cancelled updating data')
                    return
                else:
                    print('Your input is not valid, please choose y or n')
    else:
        print('The data you are looking for does not exist')
        return

def delete_option():
    while True:
        print('Delete Database')
        print('1. Delete a Database')
        print('2. Back to Previous Menu')
        input_delete = input('Enter the number: ')
        if input_delete == "1":
            delete_function()
        elif input_delete == "2":
            return
        else:
            print('The number that you choose is not valid, please enter another number')

def delete_function():
    print('Index\t| Brand\t| Name\t|')
    for i in range(len(motorcycle)):
        print(f"{i+1}\t| {motorcycle[i]['Brand']}\t| {motorcycle[i]['Name']}\t|")
    input_delete1 = int(input('Select the index number that you want to delete: '))
    x = False
    for i in range(len(motorcycle)):
        if input_delete1 == i+1:
            while True:
                input_delete2 = input('Are you sure you want to delete the data? (y/n): ')
                x = True
                if input_delete2 == 'y':  
                    del motorcycle[i]
                    print('The data has been deleted')
                    break
                elif input_delete2 == 'n':
                    print('Cancelled deleting data')
                    break
                else:
                    print('Your input is not valid, please choose y or n')
    if x == False:
        print('The data does not exist in this database')

option()    


          