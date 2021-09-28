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
