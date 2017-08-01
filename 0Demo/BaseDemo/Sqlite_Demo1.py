import logging
import sqlite3

class SQLiteManager(object):
    SHAPING_INSERT_QUERY = 'INSERT OR REPLACE INTO Data values (?, ?)'
    SHAPING_CREATE_QUERY = 'CREATE TABLE IF NOT EXISTS Data(id VARCHAR PRIMARY KEY NOT NULL,obj BLOB)'
    SHAPING_TABLE_NAME = 'Data'
    SHAPING_IP_COL = 0
    SHAPING_TC_COL = 1
    SHAPING_TIMOUT_COL = 2

    def __init__(self, file_name, logger=None):
        self.logger = logger or logging.getLogger()
        self.file_name = file_name
        with self._get_conn() as conn:
            conn.execute(SQLiteManager.SHAPING_CREATE_QUERY)
        conn.close()

    def get(self):
        query = 'SELECT * FROM Data'
        with self._get_conn() as conn:
            results = conn.execute(query).fetchall()
        conn.close()
        return results

    def add(self,id,obj):
        with self._get_conn() as conn:
            conn.execute(SQLiteManager.SHAPING_INSERT_QUERY,(id,obj))
        conn.close()

    def remove(self, id):
        query = 'DELETE FROM Data WHERE id = ?'
        with self._get_conn() as conn:
            conn.execute(query, (id,))
        conn.close()

    def _get_conn(self):
        try:
            conn = sqlite3.connect(self.file_name)
        except sqlite3.OperationalError:
            self.logger.error('Unable to access db file: {0}'.format(self.file_name))
            raise
        return conn

if __name__ == '__main__':
    s = SQLiteManager('Test.db')
    s.add('ABC','123ABC')
    print s.get()
    s.remove('ABC')