import json
import re
from money import Money

# Writes total to simulated message queue (as string)
def write_total_to_simulated_queue(money):
    with open('total_queue.txt', 'w') as f:
        f.write(str(money.amount))

# Read total from queue
# returns as formatted string e.g. '$44.15'
def read_total_from_simulated_queue():
    with open('total_queue.txt', 'r') as f:
        v = f.readline().strip()
        return Money(v, currency='USD').format('en_US')


x = Money('1234144.12', currency='USD')
write_total_to_simulated_queue(x)
print(read_total_from_simulated_queue())

def process(rec):
    dollar_sign_regex = re.compile(r'^\$(.+)$')
    bal_string = rec['balance']
    bal_fixed = dollar_sign_regex.search(bal_string).group(1)
    bal_fixed = bal_fixed.replace(',', '')
    this_balance = Money(bal_fixed, currency='USD')

    total += this_balance
    total_as_string = str(total.format('en_US'))
    rec['balance'] = total_as_string

    out_list.append(rec)

#with open('output_a.json', 'w') as f:
#    json.dump(out_list, f, indent=4)
