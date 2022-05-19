import pytest


class TestSuite:
    @classmethod

    def setup_class(cls):
        print("Se ejecuta una sola vez al inicio")

    def setup_method(self):
        print("Se ejecuta antes de cada test case")

    @pytest.mark.smoke
    def test_first(self):
        print("Test First")

    @pytest.mark.regression
    def test_second(self):
        print("Test Second")

    @pytest.mark.touch
    def test_third(self):
        print("Test Third")

    def do_something(self):
        pass

    def teardown_method(self):
        print("Se ejecuta al final de cada test case")   

    @classmethod
    def teardown_class(cls):
        print("Se ejecuta una sola vez al final")                 