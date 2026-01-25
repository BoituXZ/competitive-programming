def swap_case(s):
    new_string =""
    for char in s:
        if char.islower():
            new_char = char.upper()
            new_string = new_string + new_char
        else:            
            new_char = char.lower()
            new_string = new_string + new_char
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
