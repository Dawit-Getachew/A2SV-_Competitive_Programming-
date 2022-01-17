def swap_case(s):
    swapedS = ""
    for char in s:
        if char.isupper(): swapedS += char.lower()
        else: swapedS += char.upper()
    return swapedS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)