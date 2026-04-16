def sol(h, m):
    hs = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'one']
    ms = [" o' clock", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
          "quarter", "sixteen", "seventeen", "eighteen", "nineteen",
          "twenty", "twenty one", "twenty two", "twenty three",
          "twenty four", "twenty five", "twenty six", "twenty seven",
          "twenty eight", "twenty nine", "half"]
    if m == 0:
        return f'{hs[h]}{ms[m]}'
    elif 1 <= m <= 30:
        if m == 1:
            return f'{ms[m]} minute past {hs[h]}'
        if m != 15 and m != 30:
            return f'{ms[m]} minutes past {hs[h]}'
        else:
            return f'{ms[m]} past {hs[h]}'
    else:
        m = 60 - m
        if m == 1:
            return f'{ms[m]} minute to {hs[h + 1]}'
        if m != 15 and m != 30:
            return f'{ms[m]} minutes to {hs[h + 1]}'
        else:
            return f'{ms[m]} to {hs[h + 1]}'
 
 
if __name__ == '__main__':
    h = int(input())
    m = int(input())
 
    print(sol(h, m))
 