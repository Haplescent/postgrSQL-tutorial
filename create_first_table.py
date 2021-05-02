from sqlalchemy import *
from config import host, port, database, user, password

conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()

first_tb = Table('first_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('isHappy', Boolean, nullable=False)
)

metadata.create_all(engine)
query = insert(first_tb).values(id=1, name="Student", isHappy=True)
ResultProxy = connection.execute(query)

