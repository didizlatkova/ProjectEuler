# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def under20(x):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }[x]

def tenths(x):
    return {        
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }[x]

def getWord(number):
    if (number < 20):
        return under20(number)
    elif (number < 100):
        if  (number % 10 == 0):
            return tenths(number/10)
        else:
            return tenths(number/10) + under20(number%10)
    elif (number % 100 == 0):
        return under20(number/100) + "hundred"
    else:
        return getWord(number/100*100) + "and" + getWord(number%100)

sum = 11 # one thousand
for i in range(1, 1000):
    sum += len(getWord(i))

print(sum)