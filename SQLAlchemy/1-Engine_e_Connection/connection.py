from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@localhost:3306/dev")
conn = engine.connect()
response = conn.execute("SELECT * FROM livros;")

[print(row) for row in response]
