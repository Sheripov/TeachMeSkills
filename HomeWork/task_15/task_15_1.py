"""
Создать таблицу продуктов. Атрибуты продукта:
id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id)
для продуктов. Создать пользовательский интерфейс.
"""

from sqlalchemy import create_engine, update
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test1.db", echo=True)
metadata = MetaData()
products_table = Table('product', metadata,
                       Column('id', Integer, primary_key=True, autoincrement=True),
                       Column('name', String, unique=True),
                       Column('price', Integer),
                       Column('quantity', Integer),
                       Column('comment', String),
                       )
metadata.create_all(engine)


class Product:
    def __init__(self, name, price, quantity, comment):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.comment = comment

    def __repr__(self):
        return "<Product('%s','%s', '%s', '%s')>" % (self.name, self.price, self.quantity, self.comment)


print(mapper(Product, products_table))


def add_product(name, price, quantity, comment):
    Session = sessionmaker(bind=engine)
    session = Session()
    products = Product(name, price, quantity, comment)
    session.add(products)
    # session.add_all([User('Alex', 'Petrov'), User('Ann', 'Ivanova')])
    session.commit()


add_product('apple', 2, 4, 'red apple')
# product = session.query(Product).filter_by(
#     name='apple'
# ).all()
#
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(Product).order_by(Product.id)
instance = query.all()
print(instance)

# for instance in session.query(Product).order_by(Product.id):
#     print(instance.name, instance.price)
