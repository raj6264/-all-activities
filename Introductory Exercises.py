#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# Complete the Exercises - Representing Abstraction Through Code 
# In programming, we deal with two kinds of elements: functions and data. 
# 
# Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 
# 
# By the concept of abstraction create functions representing abstracting principles through function 
# 
# Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
# Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
# Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
# Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
# Factor:  Calculate temperature that a person feels because of the wind (Python3)


# In[ ]:






def arithmetic(num1, num2, operator):
    """
    This function takes two numbers and an operator and returns the result of applying the operator to the numbers.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"





def conversion(num, unit):
    """
    This function takes a number and a unit (either 'miles' or 'kilometers') and converts the number to the other unit.
    """
    if unit == "miles":
        return num * 1.60934
    elif unit == "kilometers":
        return num / 1.60934
    else:
        return "Invalid unit"





def earthquake_impact(magnitude):
    """
    This function takes the magnitude of an earthquake and returns a description of the impact.
    """
    if magnitude < 2.0:
        return "Generally not felt by people"
    elif magnitude < 3.0:
        return "Often felt, but rarely causes damage"
    elif magnitude < 4.0:
        return "Light shaking, noticeable indoors, but no damage"
    elif magnitude < 5.0:
        return "Moderate shaking, no damage to well-built structures"
    elif magnitude < 6.0:
        return "Strong shaking, damage to poorly constructed buildings"
    elif magnitude < 7.0:
        return "Major earthquake, widespread damage"
    elif magnitude < 8.0:
        return "Great earthquake, serious damage"
    else:
        return "Can totally destroy communities near the epicenter"




def factor(temp, wind_speed):
    """
    This function takes the temperature in Celsius and the wind speed in kilometers per hour and returns the wind chill factor.
    """
    if wind_speed < 5.0:
        return temp
    else:
        wind_chill = 13.12 + 0.6215 * temp - 11.37 * wind_speed ** 0.16 + 0.3965 * temp * wind_speed ** 0.16
        return wind_chill

