# Food Delivery Data Analysis Project (Hackathon 2026)

## 📌 Project Overview
This repository contains my submission for the Data Analysis Hackathon. The project focuses on integrating and analyzing food delivery data from three distinct sources (CSV, JSON, and SQL) to simulate a real-world data ecosystem.

## 🛠️ Data Integration Workflow
To create a "Source of Truth," I performed the following steps using Python and Pandas:
- **Source 1:** `orders.csv` (Transactional Data)
- **Source 2:** `users.json` (User Master Data)
- **Source 3:** `restaurants.sql` (Restaurant Master Data)

**Join Strategy:** I used a **Left Join** to ensure all order records were retained while mapping user and restaurant information using `user_id` and `restaurant_id` as keys.

## 📊 Key Analysis Performed
The analysis focused on five major areas as required by the hackathon guidelines:
1. **Order Trends:** Analyzing how orders fluctuate over time.
2. **User Behavior:** Mapping patterns based on membership types (Gold vs. Regular).
3. **City & Cuisine Performance:** Identifying top-performing regions and food types.
4. **Membership Impact:** Evaluating revenue differences between member tiers.
5. **Revenue Distribution:** Calculating total revenue and seasonality trends.

## 📁 File Structure
- `main.py`: Script for loading and merging datasets.
- `analysis.py` & `analysis2.py`: Scripts used to generate MCQ answers and numerical insights.
- `final_food_delivery_dataset.csv`: The final integrated dataset.

## 🚀 Technical Skills Demonstrated
- Data Wrangling with **Pandas**
- Multi-format Data Integration (CSV, JSON, SQL)
- Statistical Analysis and Data Cleaning
- Working with **VS Code** and **Git**

---
**Author:** Akanksha Patel  
**Status:** Completed & Submitted
