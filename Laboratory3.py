"""Computing total shopping expenses"""

print("Discounts")
print("At least 5,000 but below 8,000        5%\n"
      "At least 8,000 but below 11,000      10%\n"
      "At least 11,000 but below 14,000     20%\n"
      "At least 14,000 but below 17,000     25%\n"
      "At least 17,000                      30%\n")




print("Enter the prices of items")

t1=int(input("Enter Item Price 1: "))
t2=int(input("Enter Item Price 2: "))
t3=int(input("Enter Item Price 3: "))
t4=int(input("Enter Item Price 4: "))
t5=int(input("Enter Item Price 5: "))

total= t1 + t2 + t3 + t4 + t5

if total>=5000 and total<8000:
    dis = total * 0.05
    com = total - dis
    print("========================================================")  
    print("5% discount applied")
    print("Total Price :", com)
    print("========================================================")   
elif total>=8000 and total<10999:
    dis = total * 0.1
    com = total - dis
    print("========================================================")  
    print("10% discount applied")
    print("Total Price :", com)
    print("========================================================")   
elif total>=11000 and total<13999:
    dis = total * 0.2
    com = total - dis
    print("========================================================")  
    print("20% discount applied")
    print("Total Price :", com)
    print("========================================================")   
elif total>=14000 and total<16999:
    dis = total * 0.25
    com = total - dis
    print("========================================================")  
    print("25% discount applied")
    print("Total Price :", com)
    print("========================================================")   
elif total>=17000:
    dis = total * 0.3
    com = total - dis
    print("========================================================")  
    print("30% discount applied")
    print("Total Price :", com)
    print("========================================================")   
else:
    print("========================================================")  
    print("No Discount")
    print("Total Price :", total)
    print("========================================================")   
    

