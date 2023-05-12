# Lauren Spee
# 261008497

import math

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "bones"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    """ (float) -> float
    Returns the area of a circle with given diameter
    >>>round(get_pizza_area(7),2)
    38.48
    >>>round(get_pizza_area(2.5),4)
    4.9087
    >>>round(get_pizza_area(1.8),1)
    2.5
    """
    
    return math.pi*((diameter/2)**2)


def get_fair_quantity(diameter1, diameter2):
    """(float, float) -> int
    Returns an int of how many pizzas with the smaller diameter
    out of diameter1 and diameter2 it would take to equal the area
    of the bigger diameter
    >>>FAIR = True
    >>>get_fair_quantity(3.0,14.0)
    22
    >>>get_fair_quantity(20.0,6.0)
    12
    >>>FAIR = False
    >>>get_fair_quantity(7.0,8.0)
    1
    >>>get_fair_quantity(10.0,4.0)
    9
    """
    
    area1 = (math.pi*((diameter1/2)**2))
    area2 = (math.pi*((diameter2/2)**2))
    
    if area1 >= area2:
        if FAIR == True:
            return int(round((area1/area2)+0.49,0))
            #added 0.49 so it always rounds up 
        
        return int(1.5*(area1/area2)) #int always rounds down
        
    else:        
        if FAIR == True:
            return int(round((area2/area1)+0.49,0))
        
        return int(1.5*(area2/area1))

         
def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    """(num, num, num, num, int) -> float
    Returns the missing value of either d_large, d_small, c_large,
    c_small, or n_small using a formula
    >>>pizza_formula(14.0, 8.0, 9.55, -1, 4)
    12.47
    >>>pizza_formula(-1, 7.0, 12.35, 8.99,3)
    14.21
    >>>pizza_formula(16.0, -1, 11.50, 7.00, 2)
    8.83
    """
    
    a_large = (math.pi*((d_large/2)**2))
    a_small = (math.pi*((d_small/2)**2))
    
    #each if statement is the formula rearranged to equal the missing value
    if d_large == -1:
        return round((math.sqrt((4*n_small*a_small*c_large)/(math.pi*c_small))),2)
    
    elif d_small == -1:
        return round(math.sqrt((4*a_large*c_small)/(math.pi*c_large*n_small)),2)
        
    elif c_large == -1:
        return round(((a_large*c_small)/a_small),2)
    
    elif c_small == -1:
        return round(((n_small*a_small*c_large)/a_large),2)
    
    elif n_small == -1:
        return round(((a_large*c_small)/(c_large*a_small)),2)
    
    
def get_pizza_cake_cost(base_diameter, height_per_level):
    """(int, float) -> float
    Returns the cost of a stack of pizzas given the base_diameter and
    the height_per_level by finding the volume and multiplying that
    by the PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
    >>>FAIR = True
    >>>get_pizza_cake_cost(10, 2.0)
    2419.03
    >>>get_pizza_cake_cost(5,1.5)
    259.18
    >>>FAIR = False
    >>>get_pizza_cake_cost(20,1.0)
    13524.56
    >>>get_pizza_cake_cost(5,1.5)
    388.77
    """
    
    cost = 0
        
    while base_diameter >= 1:
        volume = height_per_level * (math.pi*((base_diameter/2)**2))
            
        level_price = volume * PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
            
        base_diameter -= 1
        cost += level_price
        
    if FAIR == True:
        return round(cost,2)
    
    else:
        return round(1.5*cost,2)
    
    
def get_pizza_poutine_cost(diameter, height):
    """ (int, float) -> float
    Returns the cost of a poutine cup based on its diameter and
    height which are used to find the volume then multiplied by
    PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    >>>FAIR = True
    >>>get_pizza_poutine_cost(2, 1.0)
    9.42
    >>>get_pizza_poutine_cost(8,2.0)
    301.59
    >>>FAIR = False
    >>>get_pizza_poutine_cost(5,3.0)
    265.07
    >>>get_pizza_poutine_cost(7, 1.5)
    259.77
    """
    
    volume = height*(math.pi*((diameter/2)**2))
    cost = volume * PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    
    if FAIR == True:
        return round(cost,2)
    
    else:
        return round(1.5*cost,2)


def display_welcome_menu():
    """ () -> NoneType
    Prints a welcome message
    >>>display_welcome_menu()
    Welcome to Boneless Pizza.
    Our pizzas are 100% boneless. We promise.
    Choose an option: 
    (a) Special Orders
    (b) Formula Mode
    (c) Quantity Mode
    """
    print("Welcome to Boneless Pizza Place.")
    print("Please choose an option: ")
    print("A. Special Orders")
    print("B. Formula Mode")
    print("C. Quantity Mode")
   
   
def special_orders():
    """ () -> NoneType
    Asks for a series of inputs asking for either cake or poutine
    then the height and diameter and if they want the special ingredient.
    Runs either the get_pizza_cake_cost or the get_pizza_poutine_cost
    functions and prints the result
    >>>FAIR = True
    >>>special_orders()
    Do you want cake or poutine? cake
    Enter diameter: 10
    Enter height: 1.0
    Do you want bones? no
    The cost is $1209.51
    >>>special_orders()
    Do you want cake or poutine? poutine
    Enter diameter: 8
    Enter height: 2.0
    Do you want bones? y
    The cost is $321.58
    >>> special_orders()
    Do you want cake or poutine? t
    Invalid input.
    >>>FAIR = False
    >>>special_orders()
    Do you want cake or poutine? cake
    Enter diameter: 20
    Enter height: 3
    Do you want bones? yes
    The cost is $40593.66
    >>>special_orders()
    Do you want cake or poutine? poutine
    Enter diameter: 4
    Enter height: 1
    Do you want bones? n
    The cost is $56.55
    """
    
    cake_or_poutine = input("Do you want cake or poutine? ")
    
    if cake_or_poutine != "cake" and cake_or_poutine != "poutine":
        print("Invalid input.")
        return None
    
    diameter = int(input("Enter diameter: "))
    height = float(input("Enter height: "))
    special = input("Do you want " + str(SPECIAL_INGREDIENT) + "? ")
    
    if cake_or_poutine == "cake":        
        cost = get_pizza_cake_cost(diameter, height)
                
        if special == "y" or special == "yes":
            cost = cost + SPECIAL_INGREDIENT_COST
        
        print("The cost is $" + str(round(cost,2)))
    
    else:
        cost = get_pizza_poutine_cost(diameter, height)
                
        if special == "y" or special == "yes":
            cost = (cost + SPECIAL_INGREDIENT_COST)

        print("The cost is $" + str(round(cost,2)))
        
   
def quantity_mode():
    """ () -> NoneType
    Asks for inputs of 2 diameters and runs the get_fair_quantity
    function and prints the minimum amount of small pizzas needed to
    equal the area of the large pizza
    >>>FAIR = True
    >>>quantity_mode()
    Enter diameter 1: 10
    Enter diameter 2: 5
    You should get 4 small pizzas
    >>>quantity_mode()
    Enter diameter 1: 7
    Enter diameter 2: 13
    You should get 4 small pizzas
    >>>FAIR = False
    >>>quantity_mode()
    Enter diameter 1: 14
    Enter diameter 2: 6
    You should get 8 small pizzas
    >>>quantity_mode()
    Enter diameter 1: 4
    Enter diameter 2: 12
    You should get 13 small pizzas
    """
    
    diameter1 = float(input("Enter diameter 1: "))
    diameter2 = float(input("Enter diameter 2: "))
    
    print("You should get", get_fair_quantity(diameter1, diameter2), "small pizzas")
    
    
def formula_mode():
    """ () -> NoneType
    Asks user for inputs and runs the function pizza_formula with the
    inputs of d_large, d_small, c_large, c_small, and n_small and prints
    the result
    >>>formula_mode()
    Enter large diameter: 10.0
    Enter small diameter: 5.0
    Enter large price: -1
    Enter small price: 5.0
    Enter number of small pizzas: 5
    The missing value is: 20.0
    >>>formula_mode()
    Enter large diameter: 18.0
    Enter small diameter: -1
    Enter large price: 15.0
    Enter small price: 10.0
    Enter number of small pizzas: 2
    The missing value is: 10.39
    >>>formula_mode()
    Enter large diameter: 15.0
    Enter small diameter: 4.0
    Enter large price: 10.0
    Enter small price: 1.0
    Enter number of small pizzas: -1
    The missing value is: 1.41
    """
    
    d_large = float(input("Enter large diameter: "))
    d_small = float(input("Enter small diameter: "))
    c_large = float(input("Enter large price: "))
    c_small = float(input("Enter small price: "))
    n_small = int(input("Enter number of small pizzas: "))
    
    result = pizza_formula(d_large, d_small, c_large, c_small, n_small)
    
    print("The missing value is:", result)
    
    
def run_pizza_calculator():
    """ () -> NoneType
    Runs all of the functions put together in a pizza-shop type manner,
    asking the user for inputs and calculating things depending on
    those inputs
    >>>FAIR = True
    >>>run_pizza_calculator()
    Welcome to Boneless Pizza Place.
    Please choose an option: 
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Do you want cake or poutine? cake
    Enter diameter: 14
    Enter height: 2.0
    Do you want bones? (yes/no) yes
    The cost is $6397.42
    >>>run_pizza_calculator()
    Welcome to Boneless Pizza Place.
    Please choose an option: 
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter: 16.0
    Enter small diameter: 7.0
    Enter large price: 10.0
    Enter small price: -1
    Enter number of small pizzas: 3
    The missing value is: 5.74
    >>>FAIR = False
    >>>run_pizza_calculator()
    Welcome to Boneless Pizza Place.
    Please choose an option: 
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: C
    Enter diameter 1: 18.0
    Enter diameter 2: 14.0
    You should get 2 small pizzas
    >>>run_pizza_calculator()
    Welcome to Boneless Pizza Place.
    Please choose an option: 
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: D
    Invalid mode.
    """
    
    display_welcome_menu()
    
    option = input("Your choice: ")
    
    if option == "A":
        special_orders()
        
    elif option == "B":
        formula_mode()
        
    elif option == "C":
        quantity_mode()
    
    else:
        print("Invalid mode.")

    
        