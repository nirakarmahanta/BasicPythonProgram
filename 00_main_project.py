#Author : Nirakar Mahanta
#This is the main project concept of donation system

a = float(input("Enter the amount: "))

don_money = a - (a * 0.09)

comp_money = a - don_money

print("The amount transfer to the orphanage is: ","{:.2f}".format(don_money))
print("The amount transfer to the Company is: ","{:.2f}".format(comp_money))