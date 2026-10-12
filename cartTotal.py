# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = "999"
smartWatch = "1599"
PS5 = "1299"
iPad = "599"


productName = input("Enter Product Name: ")


quantity = int(input("Enter the Quantity of the Product: "))
#typecasting in int


if productName == "headPhone":
    totalPrice = int(headPhone) * quantity


elif productName == "smartWatch":
    totalPrice = int(smartWatch) * quantity

elif productName == "PS5":
    totalPrice = int(PS5) * quantity

elif productName == "iPad":
    totalPrice = int(iPad) * quantity

#typecasting and calculating the total price based on the product selected and the quantity entered by the user    


print(f"Total Amount To Be Paid: {totalPrice}")