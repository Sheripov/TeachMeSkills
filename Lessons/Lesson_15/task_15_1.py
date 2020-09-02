from sqlalchemy import create_engine
e = create_engine("sqlite:///test.db")
e.execute("""
INSERT INTO user (firstname, lastname)
VALUES ('Farruh', 'Sheripov')
""")