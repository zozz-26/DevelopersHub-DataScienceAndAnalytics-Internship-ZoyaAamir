## Task 5: Interactive Business Dashboard in Streamlit

Built an interactive business dashboard analyzing sales, profit, and customer performance using the Global Superstore Dataset (51,290 records).

### Approach
- Cleaned dataset (dropped Postal Code column with 80% missing values)
- Performed EDA on sales by region, profit by category, and top customers
- Built Streamlit dashboard (app.py) with sidebar filters: Region, Category, Sub-Category
- Displayed KPIs: Total Sales, Total Profit, Top 5 Customers, Sales by Category

### How to Run
1. Install requirements: `pip install streamlit pandas matplotlib`
2. Place dataset CSV in the same folder
3. Run: `streamlit run app.py`

### Results & Insights
- Technology is the most profitable category (~$660K profit)
- Tom Ashbrook is the top customer (~$40K in sales)
- Dashboard allows dynamic filtering across regions and categories
