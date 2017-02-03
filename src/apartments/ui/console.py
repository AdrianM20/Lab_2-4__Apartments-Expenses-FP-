'''
Created on 19 oct. 2016
@author: adiM
'''

# import traceback
from apartments.util.common import check_digits, check_expense, apartment_exists
from apartments.domain.apartment import create_apartment, get_apartment_id
from apartments.domain.operations import add_apartment, remove_apartment, remove_apartments_inrange, \
    remove_expense_all, validate_apartment, replace_expense, apartment_total_expense, sum_of_expense, \
    total_apartment_expense_list, expense_type_total, filter_expense_type, \
    filter_value, record_undo


def read_command():
    '''
        Reads user command
        Input: -
        Output: (cmd,args) tuple where:
                cmd = user command
                args = command parameters
    '''
    command = input("Enter command: ")
    pos = command.find(' ')
    if pos == -1:
        '''
            No parameters command: exit, list, help
        '''
        return command, ''
    else:
        '''
            Parameters exist
        '''
        cmd = command[:pos]
        args = command[pos + 1:]
        args = args.split(' ')
        args = [e.strip() for e in args]
        return cmd, args


def UI_help(building, undo_steps, ):
    '''
        Print the available commands of the program
    '''
    print("Valid commands:")
    print("\tadd <apartment_id> <expense_type> <ammount>")
    print("\tremove <apartment_id>")
    print("\tremove <start_apartment> to <end_apartment>")
    print("\tremove <expense_type>")
    print("\treplace <apartment_id> <expense_type> <ammount>")
    print("\tlist")
    print("\tlist <apartment_id>")
    print("\tlist [<|=|>] <ammount>")
    print("\tsum <expense_type>")
    print("\tmax <apartment_id>")
    print("\tsort apartment")
    print("\tsort type")
    print("\tfilter <type>")
    print("\tfilter <value>")
    print("\tundo")
    print("\thelp")
    print("\texit")


def UI_add_apartment(building, undo_steps, apartment_id, expense_type, ammount):
    '''
        Validates if the set of data is correct and creates a new entry in the list
    '''
    try:

        apartment = create_apartment(int(apartment_id), expense_type, int(ammount))
        validate_apartment(apartment)
        record_undo(building, undo_steps)
        add_apartment(building, apartment)
    except ValueError as ve:
        print("Invalid input", ve)
        raise ve


def UI_print_apartment(apartment):
    '''
        Prints one specified apartment expense
    '''
    print("\t [Apartment Number: {0} || Expense: {1} || Ammount: {2}]".format(
        apartment["apartment_id"], apartment["expense_type"], apartment["ammount"], end="\t"))


def UI_print_all(building):
    '''
        Prints the whole list of apartment expenses
    '''
    if len(building) == 0:
        print("No apartment expenses recorded")
    else:
        print("The current expenses are:")
        for ap in building:
            UI_print_apartment(ap)
    print()


def UI_remove(building, undo_steps, command_args):
    '''
        Removes apartment expenses from list based on the given command
    '''
    try:
        if len(command_args) == 3 and command_args[1] == "to":
            record_undo(building, undo_steps)
            remove_apartments_inrange(building, int(command_args[0]), int(command_args[2]))
        elif len(command_args) == 1 and check_digits(command_args[0]):
            record_undo(building, undo_steps)
            ap_id = int(command_args[0])
            remove_apartment(building, ap_id)
        elif len(command_args) == 1 and check_expense(command_args[0]):
            record_undo(building, undo_steps)
            remove_expense_all(building, command_args[0])
        else:
            raise Exception("Invalid command format")
    except ValueError as ve:
        s = undo_steps.pop()
        print("Invalid input", ve)
        raise ve


def UI_replace_expense(building, undo_steps, apartment_id, expense_type, ammount):
    '''
        Validates if the set of data is correct and replaces the specified expense cost
    '''
    try:
        apartment = create_apartment(int(apartment_id), expense_type, int(ammount))
        validate_apartment(apartment)
        record_undo(building, undo_steps)
        replace_expense(building, apartment)
    except ValueError as ve:
        print("Invalid input", ve)
        raise ve


def UI_list_apartment_all(building, apartment_id):
    '''
        Lists all the expenses for a specified apartment
    '''
    id_not_found = True
    for ap in building:
        if get_apartment_id(ap) == apartment_id:
            UI_print_apartment(ap)
            id_not_found = False
    if id_not_found:
        print("There are no expenses for this apartment")


def UI_list_total_expense(building, condition, ammount):
    '''
        Lists all the apartments which obey the specified condition
    '''
    ap_ids = []
    if condition == "=":
        for ap in building:
            if apartment_total_expense(building, get_apartment_id(ap)) == ammount:
                if not get_apartment_id(ap) in ap_ids:
                    ap_ids.append(get_apartment_id(ap))
    elif condition == "<":
        for ap in building:
            if apartment_total_expense(building, get_apartment_id(ap)) < ammount:
                if not get_apartment_id(ap) in ap_ids:
                    ap_ids.append(get_apartment_id(ap))
    else:
        for ap in building:
            if apartment_total_expense(building, get_apartment_id(ap)) > ammount:
                if not get_apartment_id(ap) in ap_ids:
                    ap_ids.append(get_apartment_id(ap))
    if len(ap_ids) == 0:
        print("There are no apartments coresponding to this condition.")
    else:
        print("The apartments that are coresponding to the given condition:")
        print(ap_ids)


def UI_list(building, undo_steps, command_args):
    '''
        Decides which type of listing should be done
    '''
    operator = ["<", "=", ">"]
    if len(command_args) == 0:
        UI_print_all(building)
    elif len(command_args) == 1:
        if check_digits(command_args[0]):
            UI_list_apartment_all(building, int(command_args[0]))
        else:
            raise Exception("Invalid command format")
    elif len(command_args) == 2 and command_args[0] in operator and check_digits(command_args[1]):
        UI_list_total_expense(building, command_args[0], int(command_args[1]))
    else:
        raise Exception("Invalid command format")


def UI_sum_of_expense(building, undo_steps, expense_type):
    '''
        Prints the total costs of one specified expense type
    '''
    if check_expense(expense_type):
        if sum_of_expense(building, expense_type) == 0:
            print("There are no costs for this expense yet.")
        else:
            print("The total ammount for", expense_type, "expenses is", sum_of_expense(building, expense_type))
    else:
        print("This expense type does not exist.")


def UI_apartment_expenses(building, undo_steps, apartment_id):
    '''
        Prints the total of each expense type for a given apartment
    '''
    if apartment_exists(building, int(apartment_id)) == True:
        exp_list = total_apartment_expense_list(building, int(apartment_id))
        exp_type = ["gas", "water", "heating", "electricity", "other"]
        print("The expenses for apartment", apartment_id, "are:")
        for i in range(5):
            print("\t{0}: {1}".format(exp_type[i], exp_list[i], end="\t"))
    else:
        print("This apartment has no expenses.")


def UI_sort(building, undo_steps, arg):
    '''
        Prints a list of expenses sorted ascending as specified by user input
    '''
    if arg == "apartment":
        ap_list = sorted(building, key=lambda k: k['ammount'])
        UI_print_all(ap_list)
    elif arg == "type":
        exp_list = sorted(expense_type_total(building).items(), key=lambda x: x[1])
        print("The total ammount for each expense type:")
        for e in exp_list:
            print("\t{0}: {1}".format(e[0], e[1], end="\t"))
    else:
        raise Exception("Invalid command!")


def UI_filter(building, undo_steps, arg):
    '''
        Filters the expenses in the list based on the user input
    '''
    if check_expense(arg):
        record_undo(building, undo_steps)
        filter_expense_type(building, arg)
    elif check_digits(arg):
        record_undo(building, undo_steps)
        filter_value(building, int(arg))
    else:
        raise Exception("Invalid command!")


def UI_undo(building, undo_steps):
    '''
        Undo the last operation that modified the list
    '''
    if len(undo_steps) != 0:
        return undo_steps.pop()
    else:
        print("No actions have been taken yet.")


def run_app():
    '''
        Entry point in program
    '''
    building = [{"apartment_id": 1, "expense_type": "gas", "ammount": 100},
                {"apartment_id": 1, "expense_type": "water", "ammount": 50},
                {"apartment_id": 5, "expense_type": "water", "ammount": 250},
                {"apartment_id": 7, "expense_type": "heating", "ammount": 150},
                {"apartment_id": 4, "expense_type": "electricity", "ammount": 200},
                {"apartment_id": 12, "expense_type": "water", "ammount": 120},
                {"apartment_id": 8, "expense_type": "heating", "ammount": 315},
                {"apartment_id": 14, "expense_type": "gas", "ammount": 190},
                {"apartment_id": 5, "expense_type": "heating", "ammount": 135},
                {"apartment_id": 10, "expense_type": "other", "ammount": 45},
                {"apartment_id": 10, "expense_type": "electricity", "ammount": 220}, ]
    '''
        We add some apartments to the list so we have elements to work with
    '''
    undo_steps = []
    commands = {'add': UI_add_apartment, 'list': UI_list, 'remove': UI_remove,
                'replace': UI_replace_expense, 'sum': UI_sum_of_expense, 'max': UI_apartment_expenses,
                'help': UI_help, 'sort': UI_sort, 'filter': UI_filter}
    while True:
        (cmd, args) = read_command()
        if cmd == "exit":
            break
        try:
            if cmd == 'remove' or cmd == 'list':
                commands[cmd](building, undo_steps, args)
            elif cmd == 'undo':
                building = UI_undo(building, undo_steps)
            else:
                commands[cmd](building, undo_steps, *args)
        except KeyError:
            print("This option was not implemented. Please refer to the 'help' command")
        except ValueError:
            print("The given values are not coresponding. Please refer to the 'help' command")
        except TypeError:
            print("Wrong type of values. Please refer to the 'help' command")
        except Exception as ex:
            print("An error occurred:", ex)
            print("Try again!")
