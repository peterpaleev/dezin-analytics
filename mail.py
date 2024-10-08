# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Define raw material costs per liter (in ₽)
raw_material_costs = {
    'Дезин': 345,
    'Медихэнд': 46,
    'Дезискраб': 108,
    'Дезисепти ОП': 93,
    'Дезисепти Ультра': 72,
    'Дезихэнд': 35
}

# Function to input dynamic product amounts
def input_product_amounts():
    print("Enter product amounts in liters, separated by commas (e.g., 1,5,10,50):")
    amounts_str = input()
    amounts = [float(x.strip()) for x in amounts_str.split(',')]
    return amounts

# Function to input additional costs
def input_additional_costs():
    print("Enter additional costs in the format 'Cost_Name:Amount', separated by commas (e.g., Labor:10,Packaging:5):")
    costs_str = input()
    additional_costs = {}
    for item in costs_str.split(','):
        key, value = item.split(':')
        additional_costs[key.strip()] = float(value.strip())
    return additional_costs

# Function to input margin percentages
def input_margins():
    print("Enter margins in percentages for customer categories in the format 'Customer_Type:Margin', separated by commas (e.g., B2B:10,Retail:20):")
    margins_str = input()
    margins = {}
    for item in margins_str.split(','):
        key, value = item.split(':')
        margins[key.strip()] = float(value.strip())
    return margins

# Function to calculate prices
def calculate_prices(product, amounts, additional_costs, margins):
    base_cost_per_liter = raw_material_costs[product]
    results = []
    for amount in amounts:
        total_raw_material_cost = base_cost_per_liter * amount
        total_additional_cost = sum(additional_costs.values())
        cost = total_raw_material_cost + total_additional_cost
        for customer_type, margin in margins.items():
            final_price = cost * (1 + margin / 100)
            results.append({
                'Product': product,
                'Amount (L)': amount,
                'Customer Type': customer_type,
                'Raw Material Cost (₽)': total_raw_material_cost,
                'Additional Costs (₽)': total_additional_cost,
                'Total Cost (₽)': cost,
                'Margin (%)': margin,
                'Final Price (₽)': final_price
            })
    return pd.DataFrame(results)

# Function to generate price table
def generate_price_table():
    # Select product
    print("Select a product from the following list:")
    for idx, product in enumerate(raw_material_costs.keys()):
        print(f"{idx+1}. {product}")
    product_choice = int(input("Enter the number corresponding to the product: "))
    product = list(raw_material_costs.keys())[product_choice - 1]

    # Input amounts
    amounts = input_product_amounts()

    # Input additional costs
    additional_costs = input_additional_costs()

    # Input margins
    margins = input_margins()

    # Calculate prices
    price_table_df = calculate_prices(product, amounts, additional_costs, margins)
    print("\nGenerated Price Table:")
    print(price_table_df)

    # Export options
    print("\nDo you want to export the price table? (yes/no)")
    export_choice = input().lower()
    if export_choice == 'yes':
        export_price_table(price_table_df)

    # Save configurations
    print("\nDo you want to save these configurations for future use? (yes/no)")
    save_choice = input().lower()
    if save_choice == 'yes':
        save_configurations(product, amounts, additional_costs, margins)

    # Visualize unit economics
    visualize_unit_economics(price_table_df)

# Function to export price table
def export_price_table(df):
    # Create exports directory if it doesn't exist
    if not os.path.exists('exports'):
        os.makedirs('exports')
    # Export to Excel
    df.to_excel('exports/price_table.xlsx', index=False)
    # Export to CSV
    df.to_csv('exports/price_table.csv', index=False)
    print("Price table exported to 'exports/price_table.xlsx' and 'exports/price_table.csv'.")

# Function to save configurations
def save_configurations(product, amounts, additional_costs, margins):
    config = {
        'Product': product,
        'Amounts': amounts,
        'Additional Costs': additional_costs,
        'Margins': margins
    }
    # Create configs directory if it doesn't exist
    if not os.path.exists('configs'):
        os.makedirs('configs')
    # Save to a file
    pd.to_pickle(config, f'configs/{product}_config.pkl')
    print(f"Configurations saved to 'configs/{product}_config.pkl'.")

# Function to visualize unit economics
def visualize_unit_economics(df):
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style="whitegrid")
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='Amount (L)', y='Final Price (₽)', hue='Customer Type')
    plt.title('Final Price by Amount and Customer Type')
    plt.savefig('exports/unit_economics.png')
    plt.show()
    print("Unit economics chart saved to 'exports/unit_economics.png'.")

# Function to load configurations
def load_configurations():
    print("Enter the name of the product configuration to load (e.g., Дезин):")
    product = input()
    try:
        config = pd.read_pickle(f'configs/{product}_config.pkl')
        print(f"Configurations for {product} loaded successfully.")
        return config['Product'], config['Amounts'], config['Additional Costs'], config['Margins']
    except FileNotFoundError:
        print("Configuration file not found.")
        return None, None, None, None

# Function to track and display KPIs
def track_kpis():
    # Load business performance data from Excel files
    try:
        production_data = pd.read_excel('production_data.xlsx')
        sales_data = pd.read_excel('sales_data.xlsx')
        cost_data = pd.read_excel('cost_data.xlsx')
    except FileNotFoundError:
        print("Business performance data files not found. Please ensure 'production_data.xlsx', 'sales_data.xlsx', and 'cost_data.xlsx' are in the current directory.")
        return

    # Calculate KPIs
    total_revenue = sales_data['Revenue'].sum()
    total_costs = cost_data['Amount'].sum()
    gross_margin = total_revenue - total_costs
    net_profit = gross_margin  # Simplified
    production_volume = production_data['Volume'].sum()

    print("\nBusiness Performance KPIs:")
    print(f"Total Revenue: {total_revenue} ₽")
    print(f"Total Costs: {total_costs} ₽")
    print(f"Gross Margin: {gross_margin} ₽")
    print(f"Net Profit: {net_profit} ₽")
    print(f"Production Volume: {production_volume} liters")

    # Visualizations
    visualize_business_performance(sales_data, cost_data)

# Function to visualize business performance
def visualize_business_performance(sales_data, cost_data):
    # Ensure 'Date' columns are datetime
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])
    cost_data['Date'] = pd.to_datetime(cost_data['Date'])

    # Prepare data
    revenue_over_time = sales_data.groupby('Date')['Revenue'].sum().reset_index()
    costs_over_time = cost_data.groupby('Date')['Amount'].sum().reset_index()

    # Merge data
    performance_df = pd.merge(revenue_over_time, costs_over_time, on='Date', how='outer').fillna(0)
    performance_df['Gross Margin'] = performance_df['Revenue'] - performance_df['Amount']

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(performance_df['Date'], performance_df['Revenue'], label='Total Revenue', marker='o')
    plt.plot(performance_df['Date'], performance_df['Amount'], label='Total Costs', marker='o')
    plt.plot(performance_df['Date'], performance_df['Gross Margin'], label='Gross Margin', marker='o')
    plt.legend()
    plt.title('Business Performance Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount (₽)')
    plt.grid(True)
    plt.savefig('exports/business_performance.png')
    plt.show()
    print("Business performance chart saved to 'exports/business_performance.png'.")

    # Pie chart for cost structure
    cost_types = cost_data.groupby('Cost_Type')['Amount'].sum().reset_index()
    plt.figure(figsize=(8,8))
    plt.pie(cost_types['Amount'], labels=cost_types['Cost_Type'], autopct='%1.1f%%', startangle=140)
    plt.title('Cost Structure')
    plt.savefig('exports/cost_structure.png')
    plt.show()
    print("Cost structure pie chart saved to 'exports/cost_structure.png'.")

# Main function
def main():
    while True:
        print("\nSelect an option:")
        print("1. Generate Price Table")
        print("2. Load Saved Configuration and Generate Price Table")
        print("3. Track and Display Business Performance KPIs")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            generate_price_table()
        elif choice == '2':
            product, amounts, additional_costs, margins = load_configurations()
            if product:
                # Calculate prices with loaded configurations
                price_table_df = calculate_prices(product, amounts, additional_costs, margins)
                print("\nGenerated Price Table:")
                print(price_table_df)
                # Export options
                print("\nDo you want to export the price table? (yes/no)")
                export_choice = input().lower()
                if export_choice == 'yes':
                    export_price_table(price_table_df)
                # Visualize unit economics
                visualize_unit_economics(price_table_df)
        elif choice == '3':
            track_kpis()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
