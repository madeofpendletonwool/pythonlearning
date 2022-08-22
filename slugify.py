import sys


# print(sys.argv[1])
def slugify(phrase="HERES A DEFAULT"):
    sluggedphrase = phrase.lower().strip().replace(" ", "-")
    return sluggedphrase

slugger = slugify(sys.argv[1])
print(slugger)


