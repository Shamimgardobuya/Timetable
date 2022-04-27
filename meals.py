# from time import time


Monday={"Breakfast":"Mandazi","Lunch":"Fish","Supper":"Chapatti"}
Tuesday={"Breakfast":"Bread","Lunch":"Potatoes","Supper":"Ugali"}
Wednesday={"Breakfast":"Sausage with Tea","Lunch":"Rice","Supper":"Chicken"}
day=input("Enter the day:")
time=input("Enter the meal time: ")
time=day.values()
day = Monday or Tuesday or Wednesday

if day=="Monday" or Tuesday or Wednesday :
        print(day and time)
# elif day=="Tuesday":
#         print(Tuesday.get("Breakfast"))
        
