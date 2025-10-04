import sqlite3
import pandas as pd

def get_top_n_invoices(sqlite_path, n, min_total, max_total):
    """
    Trả về TOP N Invoice có tổng trị giá từ min_total đến max_total, sắp xếp giảm dần theo tổng trị giá.
    """
    conn = sqlite3.connect(sqlite_path)
    query = """
        SELECT InvoiceId, CustomerId, Total
        FROM Invoice
        WHERE Total BETWEEN ? AND ?
        ORDER BY Total DESC
        LIMIT ?
    """
    df = pd.read_sql_query(query, conn, params=(min_total, max_total, n))
    conn.close()
    return df

def get_top_n_customers_by_invoice_count(sqlite_path, n):
    """
    Trả về TOP N khách hàng có nhiều Invoice nhất.
    """
    conn = sqlite3.connect(sqlite_path)
    query = """
        SELECT CustomerId, COUNT(*) AS InvoiceCount
        FROM Invoice
        GROUP BY CustomerId
        ORDER BY InvoiceCount DESC
        LIMIT ?
    """
    df = pd.read_sql_query(query, conn, params=(n,))
    conn.close()
    return df

def get_top_n_customers_by_invoice_total(sqlite_path, n):
    """
    Trả về TOP N khách hàng có tổng giá trị Invoice cao nhất.
    """
    conn = sqlite3.connect(sqlite_path)
    query = """
        SELECT CustomerId, SUM(Total) AS TotalInvoice
        FROM Invoice
        GROUP BY CustomerId
        ORDER BY TotalInvoice DESC
        LIMIT ?
    """
    df = pd.read_sql_query(query, conn, params=(n,))
    conn.close()
    return df

if __name__ == "__main__":
    db_path = 'databases/Chinook_Sqlite.sqlite'
    print("TOP 5 Invoice trị giá từ 10 đến 1000:")
    print(get_top_n_invoices(db_path, 5, 10, 1000))
    print("\nTOP 5 khách hàng có nhiều Invoice nhất:")
    print(get_top_n_customers_by_invoice_count(db_path, 5))
    print("\nTOP 5 khách hàng có tổng Invoice cao nhất:")
    print(get_top_n_customers_by_invoice_total(db_path, 5))