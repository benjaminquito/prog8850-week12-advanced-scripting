import pymysql
import threading

def execute_query(query):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Secret123",
        database="prog8850"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"\nQuery: {query}\nRows: {len(results)}")
    cursor.close()
    conn.close()

queries = [
    "SELECT * FROM large_table WHERE age < 30",
    "SELECT * FROM large_table WHERE age >= 30 AND age < 60",
    "SELECT * FROM large_table WHERE age >= 60"
]

threads = []

for q in queries:
    t = threading.Thread(target=execute_query, args=(q,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nAll threads completed.")
