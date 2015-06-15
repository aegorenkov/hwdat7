'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

from os import chdir
directory = r'/home/alex/Documents/DAT7/data'
chdir(directory)

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv
with open('chipotle.tsv', 'rU') as tsvfile:
    chipotlereader = csv.reader(tsvfile, delimiter='\t')
    data = [row for row in chipotlereader]

'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''

header = data[0]
data = data[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

def strip_dollar(dollar_string):
    '''
    Strip off dollar sign and whitespace at the end of string
    return as float for simplicity    
    '''
    return float(dollar_string[1:-1])
    
#Quick test for strip_dollar function
strip_dollar('$2.39 ') == 2.39   

#Take advantage of commutation to compute the average, total/quantity
total_price = sum([strip_dollar(row[4]) for row in data])
number_orders = len(set([row[0] for row in data]))
average_price = total_price/number_orders

#18 dollars looks a little high, let's check for unsual values in the data
max([strip_dollar(row[4]) for row in data])
#44.25 is in the data set and I can see how some orders would pull up the mean
min([strip_dollar(row[4]) for row in data])
#Also reasonable


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

def drink_in(item_string):
    '''
    Return True if given a drink row.
    item_string: String from item_name column, index 2
    '''
    string_fingerprint = item_string.lower()
    if 'canned soda' in string_fingerprint:
        hasdrink = True
    elif 'canned soft drink' in string_fingerprint:
        hasdrink = True
    else:
        hasdrink = False
    return hasdrink
    
#Good, only the expected soft drinks
matched_type = set([row[2] for row in data if drink_in(row[2])])

unique_drinks = set([row[3] for row in data if drink_in(row[2])])

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

def num_toppings(topping_string):
    '''
    count the number of toppings for a given burrito
    topping_string: Expects string from choice description column, index 3, in 
    a row associated with burritos
    '''
    return len(topping_string.split(','))

#Simple tests
num_toppings('[Fresh Tomato Salsa, [Rice, Pinto Beans, Sour Cream, Cheese]]') == 5
num_toppings('[Fresh Tomato Salsa, Rice]') == 2
num_toppings('[[Fresh Tomato Salsa (Mild), Tomatillo-Red Chili Salsa (Hot)],' \
                '[Rice, Cheese, Sour Cream, Guacamole]]') == 6

#Burrito matches look reasonable
matched_burrito = set([row[2] for row in data if 'Burrito' in row[2]])

#Find average number of toppings as total_toppings/num_burritos
burrito_rows = (row for row in data if 'Burrito' in row[2]) #use less memory
burrito_topping_counts = [num_toppings(row[3]) for row in burrito_rows]
total_toppings = sum(burrito_topping_counts)
num_burritos = len(burrito_topping_counts)
avg_topping_count = total_toppings/num_burritos
#5 toppings on average looks reasonable


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

#native python appraoch
chip_orders = {}
for row in data:
    order_type = row[2]
    quantity = int(row[1])
    if 'Chip' in order_type:
        chip_orders.setdefault(order_type, 0) 
        chip_orders[order_type] += quantity
            
#ollections aproach
from collections import defaultdict

def default_factory():
    return 0
    
chip_orders = collections.defaultdict(default_factory)
for row in data:
    order_type = row[2]
    quantity = int(row[1])
    if 'Chip' in order_type:
        chip_orders.setdefault(order_type, 0) 
        chip_orders[order_type] += quantity

#Is there any advantage to default dict/ a better way?
#We can set default values with more flexible functions, but it's no help in
#this case
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''