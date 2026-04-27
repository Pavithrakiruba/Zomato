import streamlit as st
import pandas as pd
from crud import ZomatoCRUD
from insights import Insights

crud = ZomatoCRUD()
ins = Insights()
st.set_page_config(
    page_title="Zomato Clone",
    layout="wide")
st.markdown("""
<style>
.stApp {
    background-color: #FFD700;  /* Yellow background */
}

/* Heading style */
.main-title {
    color: #E23744;  /* Zomato red */
    font-size: 42px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Zomato</h1>', unsafe_allow_html=True)
st.write("Discover the best food & drinks in your city 🍴")

menu = st.sidebar.selectbox("Menu", 
    ["Add Customer", "View Customers", "Insights"])

# ---------------------------
# Add Customer
# ---------------------------
if menu == "Add Customer":
    st.subheader("Add New Customer")
    customer_id=st.text_input("Customer_id")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Location")
    signup_date=st.text_input("Signup_date")
    is_premium=st.text_input("is_premium")
    preferred_cuisine=st.text_input("preferred_cuisine")
    total_orders=st.text_input("total_orders")
    average_rating=st.text_input("average_rating")

    if st.button("Add"):
        crud.add_customer((customer_id, name, email, phone, location, signup_date, 
                           is_premium, preferred_cuisine, total_orders, average_rating))
        st.success("Customer Added Successfully!")

# ---------------------------
# View Customers
# ---------------------------
elif menu == "View Customers":
    st.subheader("Customer List")

    data = crud.get_customers()
    df = pd.DataFrame(data, columns=[
        "customer_id", "name", "email", "phone", "location", "signup_date", "is_premium", "preferred_cuisine",
        "total_orders", "average_rating"
    ])
    st.dataframe(df)

# ---------------------------
# Insights Dashboard
# ---------------------------
elif menu == "Insights":
    st.subheader("📊 Business Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Peak Order Hours")
        data = ins.peak_orders()
        df = pd.DataFrame(data, columns=["Hour", "Orders"])
        st.bar_chart(df.set_index("Hour"))

    with col2:
        st.write("### Top Customers")
        data = ins.top_customers()
        df = pd.DataFrame(data, columns=["Customer_id", "Orders"])
        st.dataframe(df)

    st.write("### Delayed Deliveries")
    data = ins.delayed_orders()
    df = pd.DataFrame(data)
    st.dataframe(df)