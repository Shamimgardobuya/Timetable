# from time import time


# from curses import keyname
# from msilib.schema import EventMapping


Monday={"Breakfast":"Mandazi","Lunch":"Fish","Supper":"Chapatti"}
# print(Monday["Breakfast"]) 
Tuesday={"Breakfast":"Bread","Lunch":"Potatoes","Supper":"Ugali"}
Wednesday={"Breakfast":"Sausage with Tea","Lunch":"Rice","Supper":"Chicken"}
Thursday={"Breakfast":"Kebab with Tea","Lunch":"Vermecelli","Supper":"Matoke and Groundnuts"}
Friday={"Breakfast":"Maize with Tea","Lunch":"Mangoes with Banana","Supper":"Sweet Potatoes with milk"}
Saturday={"Breakfast":"Humbergur with Tea","Lunch":"Rice with Fried beef","Supper":"Pumpkin with Beans"}
Sunday={"Breakfast":"Chapatti with Tea","Lunch":"Pilau","Supper":"Popcorn Soda"}
day = Monday or Tuesday or Wednesday or Thursday or Friday or Saturday or Sunday
print("This is The School Menu. To view The Menu, You can enter Day of Week and Time e.g Morning:")
day=input("Enter the day:")
# print(day)
# time=["Morning","Afternoon","Evening"]
time=input("Enter the meal time: ")
# print(time)


if ((day=='Monday') and (time=="Morning")):
        print(Monday["Breakfast"]) 
elif ((day=='Monday') and (time=="Afternoon")):
        print(Monday.get("Lunch"))
elif ((day =='Monday') and (time=="Evening")):
        print(Monday.get("Supper"))
        
elif day==(('Tuesday') and (time=="Morning")):
                print(Tuesday.get("Breakfast"))
elif day==(('Tuesday') and (time=="Afternoon")):
                print(Tuesday.get("Lunch"))
elif day==(('Tuesday') and (time=="Evening")):
                print(Tuesday.get("Supper"))

elif day==(('Wednesday') and (time=="Morning")):
         print(Wednesday.get("Breakfast"))
elif day==(('Wednesday') and (time=="Afternoon")):
         print(Wednesday.get("Lunch"))
elif day==(('Wednesday') and (time=="Evening")):
         print(Wednesday.get("Supper"))
         
         
elif day==(('Thursday') and (time=="Morning")):
         print(Thursday.get("Breakfast"))
elif day=='Thursday' and time=="Afternoon":
         print(Thursday.get("Lunch"))
elif day==(('Thursday') and (time=="Evening")):
         print(Thursday.get("Supper"))
         
         
elif day==(('Friday') and (time=="Morning")):
         print(Thursday.get("Breakfast"))         
elif day==(('Friday') and (time=="Afternoon")):
         print(Friday.get("lunch"))    
elif day==(('Friday') and (time=="Evening")):
         print(Friday.get("Supper")) 
         
         
elif day==(('Saturday') and (time=="Morning")):
         print(Saturday.get("Breakfast"))  
elif day==(('Saturday' )and (time=="Afternoon")):
         print(Saturday.get("lunch"))    
elif day==(('Saturday')and (time=="Evening")):
         print(Saturday.get("Supper")) 
         
         
elif day==(('Sunday') and (time==("Morning"))):
         print(Sunday.get("Breakfast")) 
          
elif day==(('Sunday') and (time=="Afternoon")):
         print(Sunday.get("lunch"))    
elif day==(('Sunday') and (time=="Evening")):
         print(Sunday.get("Supper")) 
else:
        print('hello')
                  
                   
                               
                                            
         
         
         
                  
        
