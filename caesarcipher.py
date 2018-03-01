# Eg: shift A 3 spaces, all As will be Ds

# NOTES:
# A-Z 65-90
# a-z 97-122
# char to unicode = ord(your_letter)
# unicode to char = chr(your_code)
# if it's a space leave it as a space, like any other different symbols


def char_alpha(unicode_number):
    if 65 <= unicode_number <= 90 or 97 <= unicode_number <= 122:
        return True
    else:
        return False


ori_str = input("Please enter string to encrypt: ")
shift_num = input("Please enter number to shift by: ")
shift_num = int(shift_num)

# Iterate through characters and change them to a new char
for c in ori_str:
    uni_num = ord(c)
    new_uni = uni_num + shift_num
    if char_alpha(uni_num):
        if char_alpha(new_uni):
            print(chr(new_uni), end="")
        else:
            print(chr(new_uni - 26), end="")
    else:
        print(c, end="")

