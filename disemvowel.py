import re

def disemvowel(text):
    text = re.sub("[y][aeiou][y]|[aeiou][y]|[y][aeiou]|[aeiou]", '', text)
    # print(x)

    return text

    # look at characters, remove y- something - y, y-something, something-y, a e i o u any vowels

print(disemvowel('may the yellow mystery force be with you!'))
print(disemvowel('sydney, kay, and yvonne met boris yeltsin in guyana'))