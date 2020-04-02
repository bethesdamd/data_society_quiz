import json
import re
from money import Money
data = json.load(open('input.json', 'r'))

# Your code here

dollar_sign_regex = re.compile(r'^\$(.+)$')
out_list = []
total = 0
for rec in data:
    bal_string = rec['balance']
    # Remove dollar sign
    # Assumes USD currency
    bal_fixed = dollar_sign_regex.search(bal_string).group(1)

    # Remove commas
    bal_fixed = bal_fixed.replace(',', '')
    this_balance = Money(bal_fixed, currency='USD')

    total += this_balance
    total_as_string = str(total.format('en_US'))
    rec['balance'] = total_as_string

    out_list.append(rec)

with open('output_a.json', 'w') as f:
    json.dump(out_list, f, indent=4)
