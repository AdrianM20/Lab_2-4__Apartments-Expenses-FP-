'''
    --- 5. Apartment Building Administrator ---

Jane is the administrator of an apartment building and she wants to manage the monthly expenses for
each apartment. Jane needs an application to store, for a given month, the expenses for each
apartment. Each expense is stored in the application using the following elements: apartment
(number of apartment, positive integer), amount (positive integer), type (from one of the predefined
categories: water, heating, electricity, gas, other). Help Jane by creating an application that provides
the following functionalities (each functionality is exemplified):

    1. add <apartment> <type> <amount>
    
    2. remove <apartment>
       remove <start apartment> to <end apartment>
       remove <type>
       
    3. replace <apartment> <type> with <amount>
    
    4. list
       list <apartment>
       list [ < | = | > ] <amount>
       
    5. sum <type>
       max <apartment>
         
    6. sort apartment
       sort type
       
    7. filter <type>
       filter <value>
       
    8. undo

Created on 18 oct. 2016
@author: adiM
'''

from apartments.ui.console import run_app

if __name__ == '__main__':
    run_app()
    print("Program ended. Goodbye!")
