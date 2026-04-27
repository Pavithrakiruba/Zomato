from db import Database

class Insights:
    def __init__(self):
        self.db = Database()

    # Peak Order Time
    def peak_orders(self):
        return self.db.fetch("""
        SELECT HOUR(order_date) as hour, COUNT(*) 
        FROM Order_table
        GROUP BY hour
        ORDER BY COUNT(*) DESC
        LIMIT 5
        """)

    # Top Customers
    def top_customers(self):
        return self.db.fetch("""
        SELECT customer_id, COUNT(*) as total_orders
        FROM Order_table
        GROUP BY customer_id
        ORDER BY total_orders DESC
        LIMIT 5
        """)

    # Delayed Deliveries
    def delayed_orders(self):
        return self.db.fetch("""
        SELECT * FROM Delivery_table
        WHERE delivery_time > estimated_time
        """)