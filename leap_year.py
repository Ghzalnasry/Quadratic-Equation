year = int(input("Enter the year number")

if(year % 400 == 0) and (year % 100 == 0):
print(f"{year} is leap year!")
elif(year % 4 == 0) and (year % 100 == 0):
print(f"{year} is leap year!")
else:
print(f"{year} isn't leap year")