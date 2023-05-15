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

#First Report for employee hours 
mycursor.execute("""SELECT empF_name AS 'First Name', empL_name AS 'Last Name', hired_Date AS 'Hire Date', position_title AS 'Position', positionType AS 'Hourly or Salary',
                timeCard AS 'Hours' FROM payroll INNER JOIN employee ON payroll.EmployeeID=employee.EmployeeID INNER JOIN position ON payroll.positionID=position.positionID""" )

#grab the data from the database
employees = mycursor.fetchall()

print("---- EMPLOYEE HOURS ---")

# Display the hours of the employees 
for employee in employees:
    print("First Name: {}\nLast Name: {}\nHire Date {}\n Position: {}\nPosition Type: {}\n Hours: {}\n" .format(employee[0],employee[1],employee[2], employee[3],employee[4],employee[5]))


#Second Report for product ordered 
mycursor.execute(""" SELECT distributorsname AS 'Distributor', productname AS 'Product', order_date AS 'Order Date', totalCost AS 'Order Amount' FROM distributorsorders INNER JOIN
                 distributors ON distributorsorders.distributorsID=distributors.distributorsID INNER JOIN bacchusproducts ON distributorsorders.productsID=bacchusproducts.productsID""")

sales = mycursor.fetchall()

print("---- SALE ORDERS ---")

# Display the amount of sales for the products
for sale in sales:
    print("Distributor: {}\nProducts: {}\nOrder Date: {}\nTotal Amount ${}\n".format(sale[0],sale[1],sale[2],sale[3]))

#Third Report for supply ordered 
mycursor.execute("""SELECT date_submitted AS 'Order Date', suppliers_name AS 'Supplier Name', supplyorderID AS 'Order ID', expected_delivery AS 'Expect Delivery', actual_delivery AS 'Actual Delivery', 
                supplyName AS 'Supply Name', issueDescription AS 'Order Issues' FROM supplyorder INNER JOIN supplierissues ON supplyorder.issueID=supplierissues.issueID INNER JOIN supplies ON 
                supplyorder.supplyID=supplies.supplyID INNER JOIN suppliers ON supplyorder.suppliersID=suppliers.suppliersID""")

orders = mycursor.fetchall()

print("---- SUPPLY ORDERS ---")

#Display the delivery problems from Suppliers 
for order in orders:
    print("Order Date: {}\nSupplier: {}\nOrder ID: {}\nExpected Delivery Date: {}\nActual Delivery Date: {}\nSupply Name: {}\nIssue Description: {}\n".format(order[0],order[1],order[2],order[3],order[4],order[5], order[6]))

def product_sales(cursor,wineName):
    #method is used to pull a single product sale from the database
    mycursor.execute(""" SELECT distributorsname AS 'Distributor', productname AS 'Product', order_date AS 'Order Date', totalCost AS 'Order Amount' FROM distributorsorders INNER JOIN
                 distributors ON distributorsorders.distributorsID=distributors.distributorsID INNER JOIN bacchusproducts ON distributorsorders.productsID=bacchusproducts.productsID""")

    sales = mycursor.fetchall()

    print("---- SALE ORDER FOR " + wineName +" ---")
 
# Display the amount of sales for the products
    for sale in sales:
        if wineName == sale[1]:
            print("Distributor: {}\nProducts: {}\nOrder Date: {}\nTotal Amount ${}\n".format(sale[0],sale[1],sale[2],sale[3]))


#calling the function 
product_sales(mycursor,"merlot")
