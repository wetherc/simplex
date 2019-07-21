import logging
import re
from sqlalchemy import create_engine
from pathlib import Path
from urllib.parse import quote_plus as urlquote


class SimplexStorageManagementAPI:

    def __init__(self):
        self.ref = None
        self.host = '127.0.0.1'
        self.user = 'root'
        self.port = 3306
        self.password = None
        self.namespace = 'simplex'
        self.conns = []
        self.disableUTF8MB4 = False

        self.CHARSETS = {
            'CHARSET_DEFAULT': 'utf8mb4',
            'CHARSET_SORT': 'utf8mb4',
            'CHARSET_FULLTEXT': 'utf8mb4',
            'COLLATE_TEXT': 'utf8mb4_bin',
            'COLLATE_SORT': 'utf8mb4_unicode_ci',
            'COLLATE_FULLTEXT': 'utf8mb4_unicode_ci'
        }

        # [TODO: @chris]
        # Not currently implemented
        self.TABLE_STATUS = None
        self.TABLE_HOSTSTATE = None

    def set_host(self, host):
        self.host = host
        return self

    def set_port(self, port):
        self.port = port
        return self

    def set_user(self, user):
        self.user = user
        return self

    def set_password(self, password):
        self.password = urlquote(password)
        return self

    def set_namespace(self, namespace):
        self.namespace = namespace
        return self

    def set_conn(self):
        self.conns.append(
            create_engine('mysql://{}:{}@{}:{}'.format(
                self.user,
                self.password,
                self.host,
                self.port
            ))
        )
        return self.conns

    def set_disable_utf8_mb4(self, disable_utf8_mb4):
        self.disableUTF8MB4 = disable_utf8_mb4
        return self

    def close_conns(self):
        for conn in self.conns:
            conn.close()

    # [TODO: @chris]
    #   - Improve logging for patches
    #   - Log applied patches and durations in db
    #   - Let patches be marked as applied
    #   - Add create_table(), create_db() functions
    def apply_patch_sql(self, sql):
        sql = Path(sql)
        with open(sql, mode='r') as s:
            sql = s.read()

        queries = sql.rstrip().split(';')
        queries = [query for query in filter(None, queries)]

        if len(self.conns) == 0:
            self.set_conn()

        conn = self.conns[0]
        conn = conn.connect()

        for query in queries:
            query = re.sub(
                r'\{\$NAMESPACE\}',
                self.namespace,
                query)

            for charset, value in self.CHARSETS.items():
                query = re.sub(
                    '{{\${0}}}'.format(charset),
                    value,
                    query
                )

            # try:
            conn.execute(query)
            # [TODO: @chris]
            # Fix error handling here
            # except:
            #     logger = logging.getLogger()
            #     logger.critical('Placeholder for a useful error message')

        conn.close()
