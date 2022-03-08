import pytest
from connection import Create_connection


class TestEmployee:
    @classmethod
    def setup_class(cls):
        print("\nSetting Up Class")

    @classmethod
    def teardown_class(cls):
        print("\nTearing Down Class")

    @pytest.fixture
    def setup(self):
        obj = Create_connection()
        return obj

    def test_db_connection(self, setup):
        with pytest.raises(Exception):
            setup.get_connection(database="Python_SQL_Assignment", user="postgresql", password="password",
                                 host="localhost", port=5432)

    def test_engine(self, setup):
        with pytest.raises(Exception):
            setup.get_engine(user="postgresql", password="root@123", host="localhost",
                             port=5432, database="aman_new_temp")