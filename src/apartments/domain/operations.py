'''
Created on 19 oct. 2016
@author: adiM
'''

# from _functools import reduce
from apartments.domain.apartment import get_apartment_id, get_ammount, get_expense_type, set_ammount
from copy import deepcopy


def validate_apartment(apartment):
    """Validate an apartment entity.
    
    Arguments:
        student - which has an apartment_id:int, expense_type:string, ammount:int
    Returns: -
    Exceptions:
        Exception - if the apartment is not valid, i.e., ammount has to be greater than 0
    """
    if get_apartment_id(apartment) < 1:
        raise Exception("Apartment id has to be greater or equal to 1")
    if get_ammount(apartment) < 1:
        raise Exception("The ammount of expense has to be greater than 0")


def find_by_id(building, apartment_id):
    '''
        Returns a list of expenses for a given aparment id or returns none if the id is not found
        Input: building - list of expenses, apartment_id - integer
        Output: list of expenses for the given apartment id
                None - if the id is not found
    '''
    l = [ap for ap in building if get_apartment_id(ap) == apartment_id]
    return None if len(l) == 0 else l[0]


def add_apartment(building, apartment):
    '''
        Adds new apartment expense to the building list
        Input: building - list of expenses, apartment - dictionary entry
        Output: adds the apartment dictionary to the list
    '''
    building.append(apartment)


def remove_apartment(building, apartment_id):
    '''
        Removes a specified apartment from the list
        Input: building - list of expenses, apartment_id - integer
        Output: removes all the entries having the given ID
    '''
    building[:] = [ap for ap in building if get_apartment_id(ap) != apartment_id]


def remove_apartments_inrange(building, start_ap, end_ap):
    '''
        Removes apartments which id's are in between start_ap and end_ap
        Input: building - list of expenses, start and end apartments - integers
        Output: Removes apartments in range start-end
    '''
    building[:] = [ap for ap in building if not get_apartment_id(ap) in range(start_ap + 1, end_ap)]


def remove_expense_all(building, expense_type):
    '''
        Removes all entries of a specified expense type
        Input: building - list of expenses, expense_type - string
        Output: Removes the requested expense from all expense entries
    '''
    building[:] = [ap for ap in building if get_expense_type(ap) != expense_type]


def replace_expense(building, apartment):
    '''
        Replaces an existing expense ammount for one apartment
        Input: building - list of expenses, apartment - dictionary entry
        Output: Replaces the requested expense of the specified apartment with the new value
    '''
    for ap in building:
        if get_apartment_id(ap) == get_apartment_id(apartment):
            if get_expense_type(ap) == get_expense_type(apartment):
                set_ammount(ap, get_ammount(apartment))
                break


def apartment_total_expense(building, apartment_id):
    '''
        Returns the total expenses for a given apartment
        Input: building - list of expenses, aparment_id - integer
        Output: Sum of expenses for the given apartment
    '''
    total_expense = 0
    for ap in building:
        if get_apartment_id(ap) == apartment_id:
            total_expense += get_ammount(ap)
    return total_expense


def sum_of_expense(building, expense_type):
    '''
        Returns the total cost of a given expense type
        Input: building - list of expenses, expense_type - string
        Output: Total costs for the specified expense type
    '''
    expense_sum = 0
    for ap in building:
        if get_expense_type(ap) == expense_type:
            expense_sum += get_ammount(ap)
    return expense_sum


def total_apartment_expense_list(building, apartment_id):
    '''
        Returns the total for each expense type for a given apartment
        Input: building - list of expense, apartment_id - integer
        Output: a list of total costs of each expense
    '''
    l = [0, 0, 0, 0, 0]
    for ap in building:
        if get_apartment_id(ap) == apartment_id:
            if get_expense_type(ap) == "gas":
                l[0] += get_ammount(ap)
            if get_expense_type(ap) == "water":
                l[1] += get_ammount(ap)
            if get_expense_type(ap) == "heating":
                l[2] += get_ammount(ap)
            if get_expense_type(ap) == "electricity":
                l[3] += get_ammount(ap)
            if get_expense_type(ap) == "other":
                l[4] = +get_ammount(ap)
    return l


def expense_type_total(building):
    '''
        Returns the total cost for each expense type
        Input: building - list of expenses
        Output: total costs for each expense
    '''
    exp_sum = {'gas': 0, 'water': 0, 'heating': 0, 'electricity': 0, 'other': 0}
    for ap in building:
        exp_sum[get_expense_type(ap)] += get_ammount(ap)
    return exp_sum


def filter_expense_type(building, expense_type):
    '''
        Keeps only the expenses having the specified type
        Input: building - list of expenses, expense_type - string
        Output: Creates a new list having only the specified expense type
    '''
    building[:] = [ap for ap in building if get_expense_type(ap) == expense_type]


def filter_value(building, ammount):
    '''
        Keeps only the expenses having the cost lower then a given ammount
        Input: building - list of expenses, ammount - integer
        Output: Creates a new list having only the expenses having costs lower than the given ammount
    '''
    building[:] = [ap for ap in building if get_ammount(ap) < ammount]


def record_undo(building, undo_steps):
    '''
        Adds a new current state of the building list to the undo list
        Input: building - List of expenses, undo_steps = list of each stage of the building lsit
        Output: adds the curent state of the building list to undo list
    '''
    current_building = deepcopy(building)
    undo_steps.append(current_building)
