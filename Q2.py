Customer_name=input("enter a string:")
Product_price=float(input("enter the price:"))
Premium_member=bool(input("Is the customer a premium member? (Yes/No):"))
Coupon_code=input("enter the code:")
if Product_price>5000 and Premium_member:
    Discount=0.20
elif Coupon_code=="save10" or Premium_member:
    Discount=0.10
else:
    Discount=0.0
Final_price=Product_price*(1-Discount)