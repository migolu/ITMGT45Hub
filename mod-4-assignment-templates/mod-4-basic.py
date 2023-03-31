#!/usr/bin/env python
# coding: utf-8

# In[4]:


def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #gross_pay = int
    gross_pay = int(gross_pay)

    #tax_rate = float
    tax_rate = float(tax_rate)

    #expenses = int
    expenses = int(expenses)
    
    tax_amount = int(tax_rate * gross_pay)
    after_tax = gross_pay - tax_amount
    remaining = int(after_tax - expenses)
    
    #account for invalid entries in tax rate
    if 0 < tax_rate <= 1:
        return remaining
    else:
        print("error")

savings(10000.99, 0.12, 2000.29)  


# In[6]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #set parameters
    total_material = int(total_material)
    material_units = str(material_units)
    num_jobs = int(num_jobs)
    job_consumption = int(job_consumption)

    job_waste = num_jobs * job_consumption
    waste_set = str(total_material - job_waste)
    material_left = waste_set + material_units

    return material_left
    

material_waste(5000, "kg", 10, 50)


# In[8]:


def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #set parameters
    principal = int(principal)
    rate = float(rate)
    periods = int(periods)
    
    inv = int(principal*(1+(rate*periods)))
    
    #making sure that rate is not invalid (set between 0 and 1)
    if 0 < rate <= 1:
        return inv
    else:
        print("error")
    
interest(1000, 0.12, 8)


# In[10]:


def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #set parameters
    weight = float(weight)
    weight_metric = float(weight*0.45359237)
    height = list(height)
    height_metric = (height[0]*12*0.0254) + (height[1]*0.0254)
    
    bmi = weight_metric / (height_metric * height_metric)
    
    return bmi
body_mass_index(40, [5, 10])


# In[ ]:




