import sys


# print(sys.argv[1])
def is_even(div):
    if div % 2 == 0:
        return True
    return False

well = is_even(int(sys.argv[1]))
print(well)


