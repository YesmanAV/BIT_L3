from datetime import datetime
from sqlalchemy import *


def add_to_origin_table(file_name):
    add_to_table(file_name, "Original")


def add_to_edited_table(file_name):
    add_to_table(file_name, "Edited")


def add_to_table(file_name, table_name):
    try:
        engine = create_engine('sqlite:///RECEIVED.db', echo=False)
        conn = engine.connect()
        meta = MetaData(engine)
        table = Table(
                table_name, meta,
                Column('id', Integer, primary_key=True),
                Column('file_name', String, nullable=False),
                Column('date_time', String, nullable=False),
            )
        meta.create_all(engine)
        s = table.select()
        result = conn.execute(s)
        copy_counter = 0
        index = file_name.find('.')
        for i in result:
            if i[1] == file_name or i[1] == file_name[:index] + str(copy_counter) + file_name[index:]:
                copy_counter = copy_counter + 1
        if copy_counter > 0:
            file_name = file_name[:index] + str(copy_counter) + file_name[index:]
        current_datetime = datetime.now()
        conn.execute(table.insert(), [
            {'file_name': file_name, 'date_time': str(current_datetime)}])
    except Exception as e:
        print("Error!", e.__class__, "occurred.")