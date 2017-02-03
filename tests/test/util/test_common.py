'''
Created on 19 oct. 2016
@author: adiM
'''

from apartments.util.common import string_contains, check_char, check_digits, check_expense, \
    apartment_exists
from test.domain.test_operations import test_Init


def test_string_contains():
    s = "apartments"
    t = "artm"
    assert(string_contains(s, t) == True)
    
def test_check_char():
    s = "stringofchar"
    assert(check_char(s) == True)
    
def test_check_digits():
    s = "2234"
    assert(check_digits(s) == True)
    
def test_check_expense():
    x = "electricity"
    assert(check_expense(x) == True)
    
def test_apartment_exists():
    l = test_Init()
    assert(len(l) == 7)
    
    assert(apartment_exists(l, 8) == True)

#==================================================================================================

def test_all_common():
    test_string_contains()
    test_check_char()
    test_check_digits()
    test_check_expense()
    test_apartment_exists()
