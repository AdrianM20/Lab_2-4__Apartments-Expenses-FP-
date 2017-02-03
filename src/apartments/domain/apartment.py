'''
Created on 19 oct. 2016
@author: adiM
'''


def create_apartment(apartment_id, expense_type, ammount):
    '''
        Returns a dictionary representing a specific expense
        Input: Input: apartment number, ammount as integers and the type of expense as a string
        Output: a dictionary containing apartment id, expense type and ammount
    '''
    return {"apartment_id": apartment_id, "expense_type": expense_type, "ammount": ammount}


def get_apartment_id(apartment):
    '''
        Return the id of one specific apartment
        Input: apartment - a dictionary
        Output: apartment id
    '''
    return apartment["apartment_id"]


def get_expense_type(apartment):
    '''
        Return the type of one specific apartment expense
        Input: apartment - a dictionary
        Output: expense type
    '''
    return apartment["expense_type"]


def get_ammount(apartment):
    '''
        Return the ammount of one specific apartment expense
        Input: apartment - a dictionary
        Output: expense ammount
    '''
    return apartment["ammount"]


def set_apartment_id(apartment, apartment_id):
    '''
        Replace the id of one specific apartment with a new given id
        Input: apartment - a dictionary, apartment_id -integer
        Output: changes the id of the given apartment
    '''
    apartment["apartment_id"] = apartment_id


def set_expense_type(apartment, expense_type):
    '''
        Replace the type of one specific apartment expense with a new given one
        Input: apartment - a dictionary, expense_type - string
        Output: changes the type of the given apartment expense
    '''
    apartment["expense_type"] = expense_type


def set_ammount(apartment, ammount):
    '''
        Replace the ammount of one specific apartment expense with a new given one
        Input: apartment - a dictionary, ammount - integer
        Output: changes the ammount of the given apartment expense
    '''
    apartment["ammount"] = ammount
