'''
Created on 19 oct. 2016
@author: adiM
'''
from apartments.domain.apartment import get_apartment_id


def string_contains(s, t):
    '''
        Check if the string s contains the string t.
    '''
    return t in s


def check_digits(s):
    '''
        Checks if a string contains only digits
    '''
    return s.isdigit()


def check_char(s):
    '''
        Checks if a string contains only alphabetical caracters
    '''
    return s.isalpha()


def check_expense(x):
    '''
        Check if the given expense type is in the registered ones
    '''
    return x in ["water", "gas", "heating", "electricity", "other"]


def apartment_exists(building, apartment_id):
    '''
        Check if a specific aparment has expenses registered in the list
    '''
    ap_is = False
    for ap in building:
        if get_apartment_id(ap) == apartment_id:
            ap_is = True
    return ap_is
