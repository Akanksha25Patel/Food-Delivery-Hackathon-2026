import pandas as pd

# Final dataset load karein
df = pd.read_csv('final_food_delivery_dataset.csv')
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

print("--- HACKATHON PORTAL MATCHED ANSWERS ---")

# Q1: Gold members revenue by City
gold_df = df[df['membership'] == 'Gold']
q1 = gold_df.groupby('city')['total_amount'].sum().idxmax()
print(f"Q1 (Gold Revenue City): {q1}")

# Q2: Avg order value by Cuisine (Options: Indian, Chinese, Italian, Mexican)
q2 = df.groupby('cuisine')['total_amount'].mean().idxmax()
print(f"Q2 (Avg Order Cuisine): {q2}")

# Q3: Distinct users with total > 1000
user_sums = df.groupby('user_id')['total_amount'].sum()
q3_count = (user_sums > 1000).sum()
print(f"Q3 (Users count > 1000): {q3_count}")

# Q4: Rating range highest revenue
bins = [3.0, 3.5, 4.0, 4.5, 5.0]
labels = ['3.0 - 3.5', '3.6 - 4.0', '4.1 - 4.5', '4.6 - 5.0']
df['rating_range'] = pd.cut(df['rating'], bins=bins, labels=labels)
q4 = df.groupby('rating_range', observed=False)['total_amount'].sum().idxmax()
print(f"Q4 (Revenue Rating Range): {q4}")

# Q5: Gold members - Highest avg order value City
q5 = gold_df.groupby('city')['total_amount'].mean().idxmax()
print(f"Q5 (Gold Avg City): {q5}")

# Q6: Lowest distinct restaurants but high revenue
res_count = df.groupby('cuisine')['restaurant_id'].nunique()
cuisine_rev = df.groupby('cuisine')['total_amount'].sum()
q6 = (cuisine_rev / res_count).idxmax()
print(f"Q6 (Best Revenue/Restaurant Ratio): {q6}")

# Q7: Gold orders percentage
q7_pct = round((len(gold_df) / len(df)) * 100)
print(f"Q7 (Gold Orders %): {q7_pct}%")

# --- Q8 FIX: Sirf portal ke 4 options check karein ---
q8_options = ['Grand Cafe Punjabi', 'Grand Restaurant South Indian', 'Ruchi Mess Multicuisine', 'Ruchi Foods Chinese']
res_stats = df.groupby('restaurant_name_x').agg({'total_amount': ['mean', 'count']})
res_stats.columns = ['avg_value', 'order_count']
filtered_q8 = res_stats[(res_stats.index.isin(q8_options)) & (res_stats['order_count'] < 20)]
print(f"Q8 (Matched Restaurant): {filtered_q8['avg_value'].idxmax()}")

# --- Q9 FIX: Sirf portal ke combinations check karein ---
# Options: Gold+Indian, Gold+Italian, Regular+Indian, Regular+Chinese
q9_combos = [('Gold', 'Indian'), ('Gold', 'Italian'), ('Regular', 'Indian'), ('Regular', 'Chinese')]
q9_results = df.groupby(['membership', 'cuisine'])['total_amount'].sum()
# Sirf unhi combos ko nikalna jo options mein hain
matched_q9 = {combo: q9_results.get(combo, 0) for combo in q9_combos}
print(f"Q9 (Matched Combination): {max(matched_q9, key=matched_q9.get)}")

# Q10: Highest Revenue Quarter
df['quarter'] = df['order_date'].dt.quarter
q10_map = {1: 'Q1 (Jan-Mar)', 2: 'Q2 (Apr-Jun)', 3: 'Q3 (Jul-Sep)', 4: 'Q4 (Oct-Dec)'}
q10 = df.groupby('quarter')['total_amount'].sum().idxmax()
print(f"Q10 (Highest Revenue Quarter): {q10_map[q10]}")