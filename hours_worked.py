#sets the hours that were worked
hours = int(input("Enter Hours : "))
#sets the rate that was worked at
rate = int(input("Enter rate : "))
#with the extra pay
if hours > 40:
  totalgrosspay = (rate *40) + (1.5 * rate * (hours-40))

#without the extra pay
else:
    totalgrosspay = (hours * rate)

print("Pay: $"+ str(totalgrosspay))

  
  

