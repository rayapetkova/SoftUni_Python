v_in_L = int(input())
p1_for_one_hour = int(input())
p2_for_one_hour = int(input())
hours = float(input())

first_pipe = hours * p1_for_one_hour
second_pipe = hours * p2_for_one_hour
both_pipes = first_pipe + second_pipe

if both_pipes <= v_in_L:
    print(f"The pool is {((both_pipes * 100) / v_in_L):.2f}% full. Pipe 1: {((first_pipe * 100) / both_pipes):.2f}%. \
    Pipe 2: {((second_pipe * 100) / both_pipes):.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {(both_pipes - v_in_L):.2f} liters.")