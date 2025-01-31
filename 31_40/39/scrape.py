import os
import sqlite3


class Database:
    ''' Class For Interacting with Database '''
    def path():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_name = 'autoblog.db'
        file_path = os.path.join(current_directory, db_name)
        return file_path
    
    def db_create():
        file_path = Database.path()
        connection = sqlite3.connect(file_path)
        cursor = connection.cursor()
        create_table = '''
                        create table if not exists entry(
                            id integer primary key,
                            time_stamp text,
                            link text,
                            post_original text,
                            title text,
                            post text
                        )
                        '''
        cursor.execute(create_table)
        connection.commit()
        connection.close()