
import pandas as pd

########################## Data import #########################
Excel_file = 'my_shop_data.xlsx'
df_customers = pd.read_excel(Excel_file, sheet_name="customers")
df_order = pd.read_excel(Excel_file, sheet_name="order")
df_employee = pd.read_excel(Excel_file, sheet_name="employee")
df_products = pd.read_excel(Excel_file, sheet_name="products")
######################## End data import #######################

def get_data():
    # Employee name
    df_employee['emp_name'] = df_employee['firstname'] + ' ' + df_employee['lastname'] #laver listen emp_name

    # Product name
    df_products['productname'] = df_products['productname']

    # Data - Add: total, order, year, month
    df_order['total'] = df_order['unitprice'] * df_order['quantity']

    # ***************************************
    # Data - Relationer
    # ***************************************
    order = pd.merge(df_order, df_products, on='product_id')
    order = pd.merge(order, df_employee, on='employee_id')

    # Order - Select colomns
    order = order[['order_id',
                'quantity','product_id', 'productname', 'type',
                'employee_id', 'emp_name',
                'total']]

    # Retuner til app.py
    return order
