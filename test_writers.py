import pytest
from writers import check_data

def test_check_data():
    assert check_data({"HN":"11","Lab_NO":"1986","Test code":["12", "34", "67"]}) == False
    assert check_data({"HN":"1234","Lab_NO":"1986","Test code":["11", "34", "67"]}) == False
    assert check_data({"HN":"1234","Lab_NO":"1986","Test code":["11", "12", "67"]}) == True
    assert check_data({"HN":"1234","Lab_NO":"1986","Test code":["11", "13", "12","12222"]}) == True