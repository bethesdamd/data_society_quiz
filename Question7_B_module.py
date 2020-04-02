# Supporting code for Question7 B


import json
import re
from money import Money

# Writes total to simulated message queue (as plain string)
def write_total_to_simulated_queue(money):
    with open('total_queue.txt', 'w') as f:
        f.write(str(money.amount))

# Read total from queue
# returns as type Money
def read_total_from_simulated_queue():
    with open('total_queue.txt', 'r') as f:
        v = f.readline().strip()
        return Money(v, currency='USD')

# 
def process(rec):
    dollar_sign_regex = re.compile(r'^\$(.+)$')
    bal_string = rec['balance']
    bal_fixed = dollar_sign_regex.search(bal_string).group(1)
    bal_fixed = bal_fixed.replace(',', '')
    this_balance = Money(bal_fixed, currency='USD')

    total_money = this_balance + read_total_from_simulated_queue()
    print(f'total_money: {total_money}')
    write_total_to_simulated_queue(total_money)
    # total_as_string = str(total.format('en_US'))
    rec['balance'] = total_money.format('en_US')
    return rec

#with open('output_a.json', 'w') as f:
#    json.dump(out_list, f, indent=4)
