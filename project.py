import re
import cowsay
import csv
import sys
import datetime
from pyfiglet import Figlet

figlet = Figlet()

def main():
# call the time() function to say if we are at lunch, dinner time or close
    t = time()
# Ask how many they are and return and int(between 1 and 8)
    n = reception()
# make a list of the customer calling the table() function
    table1 = table(n)
    order(t,table1)

def reception():
# I use figlet library to give the welcome to the customers
    figlet.setFont(font = 'doom')
    print(figlet.renderText("Welcome to Dinos"))

#Ask how many people they are and call and return "n"

# It ask how many they are and validate that give a correct format between
# minimun of 1 and maximun of 8 people, its inside a loop until give a correct format
    n = False
    while n == False:
        n = input("Table for how many?: ",)
        x = re.search(r'^[1-8]$',n)
        if x:
            n = int(n)
            break
        else:
            print("the minimum is 1 and maximum 8")
            n = False
    return(n)
    
def table(n):
# create a list where i will append the diners with name and custumer number
    table = []

# this "for" will go customer per customer asking if they already have a membership number
    for _ in range(n): 
        print("Commensal Nº ",_+1, end=" ")
        v = False
        cus = (input(" : Are you already a recurring customer? ",)).lower()
# I validate that only accept yes/no 
        while v == False:   
            v = re.search(r'^(yes|no)$',cus)
            if v:
#if the answer is "yes" will call the validate() function to check if is already in "customers.csv"
#and will append the name and discount of 10% in table[]
                if cus == "yes":
                    row = False 
                    while row == False:
                        customer = validate()

#in this line i call the check_customer() function to check if the membership number
#already exist in "customers.csv", if exist append Name and Discount into Table[]
#if doesn't exist ask to try again and call again the check_customer() function
#because is inside the loop While and will continue promping until the Membership
#number is correct 
                        row = (check_customer(customer))
                        if row == False:
                            print("This Membership number doesn't exist, try again")
                        else:
                            print()
                            print(row["Name"].capitalize(),"thank you for visiting us again 🙂")
                            table.append({"Name":row["Name"],"Discount":"10%"})
                            print()

#if not will call the new_member() funcion to append it in "cusotmers.csv" and for
#be a new one will assing 50% of disccount, after will appen the name and discount in table[]

                else:
                    row = new_member()
                    name = row["Name"].capitalize()
                    customer = row["Customer"]
                    print()
                    print(f'🎉🎉Welcome to our family {name}, your membership number is {customer} 🎉🎉')
                    print()
                    table.append({"Name":row["Name"],"Discount":"50%"})
            else:
                v = False
                cus = (input("The option are yes/no, are you already a recurring customer? ",)).lower()
    return(table)

"""
This function print the opening hour of the restaurant
and with the datetime function compare the current time to prompt
if the restaurant is ar lunch, dinner time or close
"""

def time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S').split(":")
    print()
    print("The opening hours of the restaurant are:")
    print() 
    print("Lunch: From 12hs to 16hs")
    print("Dinner: From 18hs to 24hs")
    hs = int(formatted_time[0])+2
    m = int(formatted_time[1])
    if hs >= 12 and hs <= 15:
        print(f"It's {hs}:{m} hs, We are on Lunch time👨‍🍳")
        return("Lunch")
    elif hs >= 18 and hs <= 23:
        print(f"It's {hs}:{m} hs, We are on Dinner time👨‍🍳")
        return("Dinner")
    else:
        sys.exit(f"It's {hs}:{m} hs, We are Close ☹️  Come back later \n")

"""
the order() function go one customer per customer, taking them from the table
its inform the discount they have and open the menu for lunch or dinner, this value is coming as input
then depending which menu they choose the program goes to the correct file('lunch.py'/'dinner.py') take the price
and apply the corresponding discount, finally 
add up the account of all customers and it shows the names of the customers and
 the total of the order using cowsay
"""

def order(t,table):
    final_price = 0
    names = ""
    for i in range(len(table)):
        print()
        figlet.setFont(font = 'digital')
        print(figlet.renderText(f"{table[i]['Name'].capitalize()} today you have {table[i]['Discount']} of discount!"))
        print()
        if t == "Lunch":
            print("The options of the day are:")
            with open(r'project/lunch.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f'{row["Menu"]}: {row["Description"]} at ${row["Price"]}')
        else:
            print("The options for the Dinner are:")
            print()
            with open(r'project/dinner.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f'{row["Menu"]}: {row["Description"]} at ${row["Price"]}')
        print()
        m = input("Wich Menu do you want? (1/2/3):",).strip()
        menu = str("menu "+m)
        d = table[i]["Discount"]
        d2 = re.findall(r'\d+',d)
        discount = int(d2[0])/100

        if t == "Lunch":
            with open(r'project/lunch.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if menu == row["Menu"]:
                        price = int(row["Price"])
                        price2 = price-(price*discount)
        else:
            with open(r'project/dinner.csv','r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if menu == row["Menu"]:
                        price = int(row["Price"])
                        price2 = price*(1-discount)
        final_price += price2
        names += table[i]['Name'].capitalize()+","                                
    print(cowsay.get_output_string('meow',f'{names} \n Enjoy the dinner \n You have to pay ${final_price}'))  

"""
the validate() function validate that the format of the number is well written
it will ask for the code until it written with the right format, then in return the membership number
"""

def validate():
    x = False
    while x == False:
        customer = input("What is your Membership Number?: ",)
        x = re.search(r'^DINOS([0]{3}[1]|[0][0-9][0-9][0-9]|[1][0]{3})$',customer)
        if x:
            return customer
        else:
            print("Incorrect format, the valid format is 'DINOSnnnn' with n: between 0001-1000, type again")
            x = False

"""
this funcion is checking if the given membership number is in "customers.csv"
check line per line to look for the membership number and return the whole row
if the membership number is not in "customers.csv" return False
"""

def check_customer(c):
    with open(r'project/customers.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if c == row["Customer"]:
                return (row)
        return False 

"""
this funcion ask for personal information to the new customer and add
a new line in "customers.csv" using the given personal information
and for the membership number call the membership_number() function
then return the whole row as dictionary
"""

def new_member():
    name = (input("What is your name?: ")).strip()
    age = (input("How old are you?: ")).strip()
    gender = (input("What gender do you belong to?: ")).strip()
    customer = membership_number().strip()
    with open(r'final_project/customers.csv','a') as file:
        file.write(f"{name},{age},{gender},{customer}\n")
    return ({"Name":name,"Age":age,"Gender":gender,"Customer":customer})


"""
count the number of lines of "customers.csv"
write the customer in format DINOS0000 and return customer 
"""

def membership_number():
    with open(r'project/customers.csv','r') as file:
        lines = file.readlines()
        total_lines = 0
        for line in lines:
            if line.lstrip() == "":
                l = 0
            else:
                l = 1
                total_lines += l
    number = (f"{total_lines:04d}")
    number = str(number)
    customer = "DINOS"+ number
    return customer


if __name__ == "__main__":
    main()

