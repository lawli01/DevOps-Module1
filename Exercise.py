import operator

operators = {
    'x': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv
}

def calculate(operator: str, first_operand: int, second_operand: int):
    return operators[operator](first_operand, second_operand)

def step_1():
    input_operator = input("Enter operator: ")
    first_operand = int(input("Enter first number: "))
    second_operand = int(input("Enter second number: "))
    print(f'Result: {calculate(input_operator, first_operand, second_operand)}')

def step_2():
    with (open('first_input_file.txt', mode='r')) as f:
        lines = f.readlines()
        total = 0

        for line in lines:
            split = line.split(sep=' ')
            total += calculate(split[1], int(split[2]), int(split[3]))
        
        print(total) # 756216.3057730488

def step_3():
    with (open('second_input_file.txt', mode='r')) as f:
        lines = f.readlines()
        lines_encountered = set()
        current_line_index = 0

        while True:
            line = lines[current_line_index].rstrip()
            line_split = line.split(sep=' ')
            print(line)
            if line in lines_encountered:
                print(line) # goto 1236
                print(current_line_index + 1) # 1
                return
            elif len(line_split) == 2:
                current_line_index = int(line_split[1]) - 1
            else:
                current_line_index = round(calculate(line_split[2], int(line_split[3]), int(line_split[4])))
                
            lines_encountered.add(line)

def step_4():
    with (open('third_input_file.txt', mode='r')) as f:
        lines = f.readlines()
        current_line_index = 0
        lines_encountered = set()

        while True:
            lines_length = len(lines)
            line = lines[current_line_index]
            line_split = line.rstrip().split(sep=' ')

            if current_line_index > lines_length:
                print('Current line index greater than length of lines')
                print(current_line_index)
                print(len(lines))
                return
            if line_split[0] == 'remove':
                del lines[int(line_split[1]) - 1]
                current_line_index = int(line_split[1]) - 1
                continue
            if line_split[0] == 'replace':
                line_number_1_index = int(line_split[1]) - 1
                line_number_2_index = int(line_split[2]) - 1
                current_line_index += 1

                if (line_number_1_index > lines_length or line_number_2_index > lines_length):
                    continue
                else:
                    lines[line_number_1_index] = lines[line_number_2_index]
            if line_split[0] == 'goto':
                current_line_index = int(line_split[1]) - 1
                continue

if __name__ == '__main__':
    step_3()