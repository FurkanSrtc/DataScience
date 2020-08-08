days = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"}

print(days)
val=input("select 2 days: ")

del days[val[0]] 
del days[val[1]] 

print(days)