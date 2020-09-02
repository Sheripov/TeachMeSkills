from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
conn = engine.connect()
trans = conn.begin()
conn.execute(
 "insert into user (firstname, lastname) values (:firstname, :lastname)",
 firstname="Pasha", lastname='Ivanov')
trans.commit()
conn.close()