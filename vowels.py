import sys

count = 0 
# print(sys.argv[1])
def vowelcount(phrase):
    count = 0
    for chr in phrase:
        if chr in "aeiou":
            count += 1
    return count

slugger = vowelcount(sys.argv[1])
print(count)


