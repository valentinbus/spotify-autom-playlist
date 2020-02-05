import psycopg2

print('okkkkk')

conn = psycopg2.connect(
    host="0.0.0.0",
    port=5433,
    database="postgres", 
    user="root", 
    password="root",
    connect_timeout=3
)

print('ok fin')
print(conn)
