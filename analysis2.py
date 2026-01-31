import pandas as pd

# Final merged dataset load karein
df = pd.read_csv('final_food_delivery_dataset.csv')

print("--- NUMERICAL ANSWERS (Baki bache hue boxes ke liye) ---")

# N1: How many total orders were placed by users with Gold membership?
gold_df = df[df['membership'] == 'Gold']
print(f"N1 (Total Gold Orders): {len(gold_df)}")

# N2: Total revenue (rounded to nearest integer) generated from Hyderabad?
hyd_rev = df[df['city'] == 'Hyderabad']['total_amount'].sum()
print(f"N2 (Hyderabad Total Revenue): {round(hyd_rev)}")

# N3: How many distinct users placed at least one order?
print(f"N3 (Total Distinct Users): {df['user_id'].nunique()}")

# N4: What is the average order value (rounded to 2 decimals) for Gold members?
avg_gold_val = gold_df['total_amount'].mean()
print(f"N4 (Avg Order Value - Gold): {round(avg_gold_val, 2)}")

# N5: How many orders were placed for restaurants with rating >= 4.5?
high_rating_orders = len(df[df['rating'] >= 4.5])
print(f"N5 (Orders with Rating >= 4.5): {high_rating_orders}")

# N6: How many orders were placed in the top revenue city among Gold members only?
top_gold_city = gold_df.groupby('city')['total_amount'].sum().idxmax()
top_city_gold_orders = len(gold_df[gold_df['city'] == top_gold_city])
print(f"N6 (Orders in Top Gold City - {top_gold_city}): {top_city_gold_orders}")


print("\n--- 2. FILL IN THE BLANKS (image_f40262.png & image_f3f7fe.png) ---")

print("1. Column used to join orders and users: user_id")
print("2. Format of restaurant information: SQL")
print(f"3. Total number of rows in final dataset: {len(df)}")
print("4. Missing records in users.json result in: NaN (ya Null)")
print("5. Pandas function used to combine datasets: merge")
print("6. Column membership originates from: users.json")
print("7. Join key for restaurant details: restaurant_id")
print("8. Column for type of food: cuisine")
print("9. If a user places multiple orders, their details appear: Multiple (ya 'as many as orders')")