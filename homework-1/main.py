"""Скрипт для заполнения данными таблиц в БД Postgres."""
if __name__=='__main__':
    import csv
    import psycopg2


    def csv_open(name_file):  # 'north_data/customers_data.csv'  north_data/employees_data.csv  north_data/orders_data.csv
        with open(name_file) as file:
            csv_list = csv.DictReader(file)
            return list(csv_list)

    csv_list_orders = csv_open('north_data/orders_data.csv')
    csv_list_employees = csv_open('north_data/employees_data.csv')
    csv_list_customers = csv_open('north_data/customers_data.csv')


    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )

    with conn.cursor() as curs:

        for employe in csv_list_employees:
            curs.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (
                employe['employee_id'], employe['first_name'], employe['last_name'], employe['title'],
                employe['birth_date'], employe['notes']))
            curs.execute("SELECT * FROM employees")
            data_employe = curs.fetchall()

        for customer in csv_list_customers:
            curs.execute('INSERT INTO customers VALUES (%s, %s, %s)', (
                customer['customer_id'], customer['company_name'],
                customer['contact_name']))
            curs.execute("SELECT * FROM employees")
            data_customer = curs.fetchall()

        for order in csv_list_orders:
            curs.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (
                order['order_id'], order['customer_id'], order['employee_id'], order['order_date'],
                order['ship_city']))
            curs.execute("SELECT * FROM employees")
            data_order = curs.fetchall()

    conn.close()