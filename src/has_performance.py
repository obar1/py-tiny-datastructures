import ipytest
import duckdb
import pytest


class HasPerformance:
    def __init__(self):
        self.con = duckdb.connect(":memory:")
        self.con.sql(
            "\n"
            + "            CREATE SEQUENCE id_sequence START 1;\n"
            + "            CREATE TABLE tbl (id INTEGER DEFAULT nextval('id_sequence'), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, s VARCHAR);\n"
            + "            "
        )

    def save(self, txt: str):
        (
            "save some txt\n"
            + "\n"
            + "        Args:\n"
            + "            txt (str): any txt\n"
            + "        "
        )
        self.con.sql(f"INSERT INTO tbl (s) VALUES ('{txt}');")
