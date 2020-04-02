# Question 7 B
# This is the main program which calls a simulated service,
# called process() in module Question7_B_module 

from money import Money
import Question7_B_module as q
import json

if __name__ == "__main__":

    # Zero out the queue value
    with open('total_queue.txt', 'w') as f:
        f.write("0.0")

    data = json.load(open('input.json', 'r'))

    final_arr = []
    with open('output_a.json', 'w') as f:
        for rec in data:
            final_arr.append(q.process(rec))
        json.dump(final_arr, f, indent=4)
