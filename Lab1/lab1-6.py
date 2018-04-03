def factor_calculate(function_input):
    factor_count = 0
    print("Here are the factors of number", function_input, ": ")
    for x in range (1, function_input + 1):
        if function_input % x == 0:
            print(x)
            factor_count = factor_count + 1
    print("Altogether", factor_count, "factors")
    return

input_from_command_line = int(input("Give me a integer: "))

factor_calculate(input_from_command_line)

