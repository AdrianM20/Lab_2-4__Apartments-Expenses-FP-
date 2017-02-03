'''
Created on 19 oct. 2016
@author: adiM
'''

from apartments.domain.apartment import create_apartment, get_ammount, get_apartment_id, \
    get_expense_type, set_apartment_id, set_expense_type, set_ammount
    
    
def test_create_apartment():
    apartment = {"apartment_id":1, "expense_type":"gas", "ammount":200}
    assert(create_apartment(1, "gas", 200) == apartment)
    
def test_get_apartment_id():
    apartment = create_apartment(1, "gas", 200)
    assert(get_apartment_id(apartment) == 1)
    
def test_get_expense_type():
    apartment = create_apartment(1, "gas", 200)
    assert(get_expense_type(apartment) == "gas")
    
def test_get_ammount():
    apartment = create_apartment(1, "gas", 200)
    assert(get_ammount(apartment) == 200)
    
def test_set_apartment_id():
    apartment = create_apartment(1, "gas", 200)
    set_apartment_id(apartment, 3)
    assert(get_apartment_id(apartment) == 3)
    
def test_set_expense_type():
    apartment = create_apartment(1, "gas", 200)
    set_expense_type(apartment, "water")
    assert(get_expense_type(apartment) == "water")
    
def test_set_ammount():
    apartment = create_apartment(1, "gas", 200)
    set_ammount(apartment, 100)
    assert(get_ammount(apartment) == 100)
    
#==================================================================================================    

def test_all_entities():
    test_create_apartment()
    test_get_apartment_id()
    test_get_expense_type()
    test_get_ammount()
    test_set_apartment_id()
    test_set_expense_type()
    test_set_ammount()
