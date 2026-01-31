import pandas as pd
import psycopg2

try:
    # Files load karein
    df_orders = pd.read_csv('orders.csv')
    df_users = pd.read_json('users.json')
    print("CSV aur JSON load ho gaye!")

    # Database se connect karein
    conn = psycopg2.connect(
        database="food_delivery",
        user="postgres",
        password="*****", # <--- Yahan apna asli password likhein
        host="127.0.0.1",
        port="5432"
    )
    df_restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
    conn.close()
    print("SQL Data load ho gaya!")

    # Data Merge (Join) karein
    # 1. Orders + Users
    merged_df = pd.merge(df_orders, df_users, on='user_id', how='left')
    # 2. Result + Restaurants
    final_df = pd.merge(merged_df, df_restaurants, on='restaurant_id', how='left')

    # Final file save karein
    final_df.to_csv('final_food_delivery_dataset.csv', index=False)
    print("SUCCESS: final_food_delivery_dataset.csv ban gayi hai!")

except Exception as e:
    print(f"Error: {e}")