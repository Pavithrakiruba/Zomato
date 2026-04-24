from faker import Faker
f=Faker()
import pandas as pd
from datetime import datetime
import numpy as np
import random 
import csv
f=Faker(locale='en_IN')
class Dataset:
    def create_customers(self,num_records):
        customers=[]
        for _ in range (num_records):
            customers.append({
            "customer_id": _ +1,
            "name": f.name(),
            "email":f.email(),
            "phone":f.phone_number(),
            "location":f.address(),
            "signup_date":f.date_between(start_date="-2y",end_date="today"),
            "is_premium":random.choice([0,1]),
            "preferred_cuisine":random.choice(["Indian","Chinese","Italian","Mexican","Thai"]),
            "total_orders":random.randint(0,50),
            "average_rating":round(random.uniform(3.0,5.0),1),
            })
        df = pd.DataFrame(customers)
        df.to_csv('customers.csv', index=False)
        return df
    

    def create_restaurant(self, num_records):
        restaurant = []
        for i in range(num_records):
            restaurant.append({
            "restaurant_id": i + 1,
            "restaurant_name": f.random_element(["A2B","ManojBhavan","SaiSangeeth","Sangeetha","HotChips","SaravanaBhavan","BalajiBhavan","AryaBhavan"]),
            "cuisine_type": f.random_element(["Indian","Chinese","Italian","Mexican","Thai"]),
            "location": f.city(),
            "owner_name": f.name(),
            "average_delivery_time": f.time(),
            "contact_number": f.phone_number(),
            "rating": f.random_int(min=1, max=5),
            "total_orders": f.random_int(min=1, max=100),
            "is_active": f.random_element([0,1])
        })

        df1 = pd.DataFrame(restaurant)
        df1.to_csv('Restaurant.csv', index=False)
        return df1

    def create_Order_table(self,num_records):
        order_table=[]
        for _ in range(num_records):
            order_table.append ({
            "Order_id": _ +1,
            "Customer_id":f.random_int(),
            "Restaurant_id":f.random_int(),
            "Order_date":f.date_between(start_date="-1y",end_date="today"),
            "Delivery_time":f.time(),
            "Status":f.random.choice(["preparing","on the way","Delivered","packing"]),
            "Total_amount":f.random_int(100,2000),
            "Payment_mode":f.random.choice(["cash_on_delivery","Gpay","bank_transfer","Card_payment","UPI"]),
            "Discount_applied":f.random.choice(["discount_applied","not_applicable"]),
            "Feedback_rating":f.random.choice(["1","2","3","4","5"])})
        df2=pd.DataFrame(order_table)
        df2.to_csv('Order_table.csv',index=False)
        return df2
    
    def create_Delivery_Table(self,num_records):
        Delivery_table=[]
        for _ in range(num_records):
            Delivery_table.append({
            "Delivery_id": _ + 1,
            "Order_id": f.random_int(min=1, max=100),
            "Delivery_Person_id": f.random_int(min=1, max=50),
            "Delivery_status":f.random.choice(["delivered","on the way","pending","packing"]),
            "Distance_in_KM":f.random_digit(),
            "Delivery_time":f.time(),
            "Estimated_time":f.time(),
            "Delivery_fees":f.random_int(50,500),
            "Vehicle_Type":f.random.choice(["bike","auto","scooty","bicycle","car"])
        })
        df3=pd.DataFrame(Delivery_table)
        df3.to_csv('Delivery_table.csv',index=False)
        return df3
    
    def Delivery_person_table(self, num_records):
        delivery = []
        for i in range(num_records):
            delivery.append({
            "Delivery_person_id": i + 1,  
            "Name": f.name(),
            "Contact_number": f.msisdn()[0:10], 
            "Vehicle_type": f.random_element(["bike", "auto", "scooty", "bicycle", "car"]),
            "Total_deliveries": f.random_int(min=0, max=500),
            "Average_rating": round(f.random.uniform(1, 5), 2),  
            "Location": f.city()  
        })

        df4 = pd.DataFrame(delivery)
        df4.to_csv('Delivery_person_table.csv', index=False)
        return df4
data=Dataset()

#df=data.create_customers(150)
#df1=data.create_restaurant(150)
#df2=data.create_Order_table(150)
#df3=data.create_Delivery_Table(150)
df4=data.Delivery_person_table(150)

