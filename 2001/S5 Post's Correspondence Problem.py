# https://dmoj.ca/problem/ccc01s5
# Currently still fails last test case
maximum_length = int(input())
number_of_strings = int(input())

a = []
b = []
sequence_array = [0 for i in range(40)]  # 40 maximum array size
sequence_length = 0

for _ in range(number_of_strings):
    a.append(input())

for _ in range(number_of_strings):
    b.append(input())


def post(a_string, b_string, strings_added):
    global sequence_length

    if strings_added > maximum_length:
        return False
    elif (a_string == b_string) and strings_added > 0:  # empty strings would equal each other
        return True
    elif not equal_start(a_string, b_string):
        return False
    else:
        index = 0
        found_solution = False
        while (index < number_of_strings) and (not found_solution):
            sequence_length = strings_added
            sequence_array[sequence_length] = index
            found_solution = post(a_string + a[index], b_string + b[index], strings_added + 1)
            index += 1
        return found_solution


def equal_start(a_string, b_string):
    # If the two strings are different length, then the shorter string matches the beginning of the other
    if a_string == b_string:
        return True
    elif len(a_string) < len(b_string):
        return b_string.startswith(a_string)
    elif len(b_string) < len(a_string):
        return a_string.startswith(b_string)
    else:
        return False


if post("", "", 0):
    # everything plus one since the problem statement isn't 0-indexed
    print(sequence_length + 1)
    for i in range(sequence_length + 1):
        print(sequence_array[i] + 1)
else:
    print("No Solution")
