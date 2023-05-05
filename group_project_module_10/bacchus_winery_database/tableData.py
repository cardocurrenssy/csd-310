"""
 Ricardo Orlando | Monica Jones | Donnell Perkins
 Bellevue University
 Module 7 05/04/23
 
 A program that connects to a database and use queries to access the data
 """
import mysql.connector

config = {
    "user": "admin_bacchus",
    "password": "winery",
    "host": "127.0.0.1",
    "database": "bacchus_winery",
    "raise_on_warnings": True
}

#database connection 
db = mysql.connector.connect(**config)

mycursor = db.cursor()

#pulling data from the database for products
mycursor.execute("SELECT * FROM bacchusproducts")

product_Table = mycursor.fetchall()

print("---Bacchus Products Table---")

for row in product_Table:
    print(row)

#pulling data from the database for Distributors
mycursor.execute("SELECT * FROM distributors")

distributors_Table = mycursor.fetchall()

print("---Bacchus Distributors Table---")

for row in distributors_Table:
    print(row)

#pulling data from the database for Distributors Orders
mycursor.execute("SELECT * FROM distributorsorders")

distributors_Orders = mycursor.fetchall()

print("---Distributors Orders Table ---")

for row in distributors_Orders:
    print(row)

#pulling data from the database for employee
mycursor.execute("SELECT * FROM employee")

employee_Table = mycursor.fetchall()

print("---Bacchus Employees Table---")

for row in employee_Table:
    print(row)

#pulling data from the database for managers
mycursor.execute("SELECT * FROM managers")

managers_Table = mycursor.fetchall()

print("---Bacchus Managers Table---")

for row in managers_Table:
    print(row)

#pulling data from the database for payroll
mycursor.execute("SELECT * FROM payroll")

payroll_Table = mycursor.fetchall()

print("---Bacchus Payroll Table---")

for row in payroll_Table:
    print(row)


#pulling data from the database for positions
mycursor.execute("SELECT * FROM position")

position_Table = mycursor.fetchall()

print("---Bacchus Position Table---")

for row in position_Table:
    print(row)

#pulling data from the database for product inventory
mycursor.execute("SELECT * FROM productinventory")

pInventory_Table = mycursor.fetchall()

print("---Bacchus Product Inventory Table---")

for row in pInventory_Table:
    print(row)

#pulling data from the database for Supplier Issues
mycursor.execute("SELECT * FROM supplierissues")

sIssues_Table = mycursor.fetchall()

print("---Bacchus Supplier Issues Table---")

for row in sIssues_Table:
    print(row)

#pulling data from the database for Suppliers
mycursor.execute("SELECT * FROM suppliers")

suppliers_Table = mycursor.fetchall()

print("---Bacchus Suppliers Table---")

for row in suppliers_Table:
    print(row)


#pulling data from the database for Supplies
mycursor.execute("SELECT * FROM supplies")

supplies_Table = mycursor.fetchall()

print("---Bacchus Supplies Table---")

for row in supplies_Table:
    print(row)


#pulling data from the database for Supply Inventory
mycursor.execute("SELECT * FROM supplyinventory")

sInventory_Table = mycursor.fetchall()

print("---Bacchus Supply Inventory Table---")

for row in sInventory_Table:
    print(row)

#pulling data from the database for Supply Order
mycursor.execute("SELECT * FROM supplyorder")

sOrder_Table = mycursor.fetchall()

print("---Bacchus Supply Order Table---")

for row in sOrder_Table:
    print(row)