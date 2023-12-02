file = open('Day1\\secret_elf_doc.txt','r')

sum_of_callibaration = 0

callibaration_value_list = []

def get_calibration_values(line):
    for x in line:
        if x.isdigit():
            return x

def get_final_value(line):

    digit_1 = get_calibration_values(line)

    digit_2 = get_calibration_values(line[::-1])

    return "".join([digit_1,digit_2])

def final_secret_code():
    lines = file.readlines()
    for x in lines:
        callibaration_value_list.append(int(get_final_value(x)))


final_secret_code()
print(callibaration_value_list)
print(sum(callibaration_value_list))