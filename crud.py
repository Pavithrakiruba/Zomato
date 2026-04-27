from db import Database

class ZomatoCRUD:
    def __init__(self):
        self.db = Database()

    # Add Customer
    def add_customer(self, data):
        query = """
        INSERT INTO customer_detail(customer_id, name, email, phone, location,
        signup_date, is_premium, preferred_cuisine, total_orders, average_rating)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.db.execute(query, data)

    # View Customers
    def get_customers(self):
        return self.db.fetch("SELECT * FROM customer_detail")

    # Delete Customer
    def delete_customer(self, cid):
        self.db.execute("DELETE FROM customer_detail WHERE customer_id=%s", (cid,))