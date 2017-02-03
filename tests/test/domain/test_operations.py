'''
Created on 19 oct. 2016

@author: adiM
'''
from apartments.domain.apartment import create_apartment
from apartments.domain.operations import add_apartment, remove_apartment, remove_apartments_inrange, \
    remove_expense_all, replace_expense, apartment_total_expense, sum_of_expense, \
    total_apartment_expense_list, expense_type_total, filter_expense_type, \
    filter_value


def test_Init():
    building = []
    building.append(create_apartment(8, "gas", 215))
    building.append(create_apartment(8, "gas", 120))
    building.append(create_apartment(12, "electricity", 110))
    building.append(create_apartment(3, "gas", 170))
    building.append(create_apartment(15, "other", 50))
    building.append(create_apartment(16, "water", 165))
    building.append(create_apartment(8, "electricity", 200))
    return building

def test_add_apartment():
    l = test_Init()
    assert(len(l) == 7)
    
    add_apartment(l, create_apartment(9, "water", 200))
    assert(len(l) == 8)

def test_remove_apartment():
    l = test_Init()
    assert(len(l) == 7)
    
    remove_apartment(l, 8)
    assert(len(l) == 4)
    
def test_remove_apartments_inrange():
    l = test_Init()
    assert(len(l) == 7)
    
    remove_apartments_inrange(l, 8, 16)
    assert(len(l) == 5)
    
def test_remove_expense_all():
    l = test_Init()
    assert(len(l) == 7)
    
    remove_expense_all(l, "electricity")
    assert(len(l) == 5)
    
def test_replace_expense():
    l = test_Init()
    assert(len(l) == 7)
    
    apartment = create_apartment(8, "gas", 200)
    replace_expense(l, apartment)
    assert(l[0]["ammount"] == 200)
    
def test_apartment_total_expense():
    l = test_Init()
    assert(len(l) == 7)
    
    assert(apartment_total_expense(l, 8) == 535)
    
def test_sum_of_expense():
    l = test_Init()
    assert(len(l) == 7)
    
    assert(sum_of_expense(l, "gas") == 505)
    
def test_total_expense_list():
    l = test_Init()
    assert(len(l) == 7)
    
    exp = total_apartment_expense_list(l, 8)
    assert(exp[0] == 335)
    
def test_expense_type_total():
    l = test_Init()
    assert(len(l) == 7)
    
    assert(expense_type_total(l)['gas'] == 505)
    
def test_filter_expense_type():
    l = test_Init()
    assert(len(l) == 7)
    
    filter_expense_type(l, 'gas')
    assert(len(l) == 3)
    
def test_filter_value():
    l = test_Init()
    assert(len(l) == 7)
    
    filter_value(l, 180)
    assert(len(l) == 5)

#==============================================================================================================
    
def test_all_operations():
    test_add_apartment()
    test_remove_apartment()
    test_remove_apartments_inrange()
    test_remove_expense_all()
    test_replace_expense()
    test_apartment_total_expense()
    test_sum_of_expense()
    test_total_expense_list()
    test_expense_type_total()
    test_filter_expense_type()
    test_filter_value()
