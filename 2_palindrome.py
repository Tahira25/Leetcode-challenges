def is_palindrome(input):
    if str(input)[::] == str(input)[::-1]:
        return True
    return False

print(is_palindrome(213234435))



# x = "123456"
# print(x[::])
# print(x[::-1])
# print(len(x))