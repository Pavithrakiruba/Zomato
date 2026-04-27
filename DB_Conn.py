import mysql.connector as db
import pandas as pd
try:
    conn = db.connect(
        host="localhost",
        user="root",
        password="Kalandharun8",
        database="zomatodb",
        connection_timeout=10
    )

    print("✅ Connected!")
    
except Exception as e:
    print("❌ ERROR:", e)

cursor = conn.cursor()

'''
df = pd.read_csv("D:/Zomato_Food/customers.csv")
print("CSV rows:", len(df))
print(df.head())


# ✅ Data cleaning
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
df['signup_date'] = df['signup_date'].dt.strftime('%Y-%m-%d')

df['is_premium'] = df['is_premium'].astype(int)
df = df.where(pd.notnull(df), None)
cols = [
    'customer_id','name','email','phone','location',
    'signup_date','is_premium','preferred_cuisine',
    'total_orders','average_rating'
]

data = list(df[cols].itertuples(index=False, name=None))

print("Prepared rows:", len(data))


insert_query = """
INSERT INTO customer_detail 
(customer_id, name, email, phone, location, signup_date, is_premium, preferred_cuisine, total_orders, average_rating) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print("Bulk inserted:", cursor.rowcount)
except Exception as e:
    print("ERROR:", e)
cursor.close()
conn.close()


#Restaurant table insertion:
df1= pd.read_csv("D:/Zomato_Food/Restaurant.csv")
print("CSV rows:", len(df1))
print(df1.head())

cols = [
    'restaurant_id','restaurant_name','cuisine_type','location','owner_name','average_delivery_time',
    'contact_number','rating','total_orders','is_active'
]

data = list(df1[cols].itertuples(index=False, name=None))

print("Prepared rows:", len(data))


insert_query = """
INSERT INTO restaurant_detail
(restaurant_id,restaurant_name,cuisine_type,location,owner_name,average_delivery_time,contact_number,rating,total_orders,is_active) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
try:
    cursor.executemany(insert_query, data)
    conn.commit()
    print("✅ Bulk inserted:", cursor.rowcount)
except Exception as e:
    print("❌ ERROR:", e)
cursor.close()
conn.close()

# Order Table insertion
df2=pd.read_csv("D:/zomato_food/Order_table.csv")
print("CSV rows:",len(df2))
print(df2.head())
df2['Order_date'] = pd.to_datetime(df2['Order_date']).dt.date
df2['Delivery_time'] = pd.to_datetime(df2['Delivery_time']).dt.time
df2['Feedback_rating'] = df2['Feedback_rating'].astype(int)
#correct column order
cols=['Order_id','Customer_id','Restaurant_id','Order_date','Delivery_time','Status',
      'Total_amount','Payment_mode','Discount_applied','Feedback_rating']
data=list(df2[cols].itertuples(index=False,name=None))
print("Prepared rows:",len(data))
insert_query="""insert into Order_Table(Order_id,Customer_id,Restaurant_id,Order_date,Delivery_time,
Status,Total_amount,Payment_mode,Discount_applied,Feedback_rating)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
try:
    cursor.executemany(insert_query,data)
    conn.commit()
    print("Bulk inserted:",cursor.rowcount)
except Exception as e:
    print("Error:",e)    
    cursor.close()
    conn.close()
#Delivery_table insertion

df3=pd.read_csv("D:/zomato_food/Delivery_table.csv")
print("CSV Rows:",len(df3))
print(df3.head())
cols=['Delivery_id','Order_id','Delivery_Person_id','Delivery_status',
      'Distance_in_KM','Delivery_time','Estimated_time','Delivery_fees','Vehicle_Type']
data=list(df3[cols].itertuples(index=False,name=None))
print("prepared rows:",len(data))
insert_query="""insert into Delivery_table(Delivery_id,Order_id,Delivery_Person_id,Delivery_status,
Distance_in_KM,Delivery_time,Estimated_time,Delivery_fees,Vehicle_Type)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
try:
    cursor.executemany(insert_query,data)
    conn.commit()
    print("Bulk inserted:",cursor.rowcount)
except Exception as e:
    print("Error:",e)
    cursor.close()
    conn.close()
# Delivery person table insertion
df4=pd.read_csv("D:/zomato_food/Delivery_person_table.csv")
print("CSV rows:",len(df4))
print(df4.head())

cols=['Delivery_person_id','Name','Contact_number',
      'Vehicle_type','Total_deliveries','Average_rating','Location']
data=list(df4[cols].itertuples(index=False,name=None))
print("prepared rows:",len(data))
insert_query = """
INSERT INTO Delivery_person_table (Delivery_person_id,Name,Contact_number,Vehicle_type,
    Total_deliveries,Average_rating,Location) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
try:
    cursor.executemany(insert_query,data)
    conn.commit()
    print("bulk inserted",cursor.rowcount)
except Exception as e:
    print("Error:",e)
    cursor.close()
    conn.close()'''