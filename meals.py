from time import time


Monday={"Breakfast":"Mandazi","Lunch":"Fish","Supper":"Chapatti"}
Tuesday={"Breakfast":"Bread","Lunch":"Potatoes","Supper":"Ugali"}
Wednesday={"Breakfast":"Sausage with Tea","Lunch":"Rice","Supper":"Chicken"}

time=input("Enter the meal time: ")
day=input("Enter the day: ")
if day=="Monday":
        print(Monday)
elif day=="Tuesday":
        print(Tuesday.get("Breakfast"))
        
