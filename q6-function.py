
# Determine if input is a leap year
def is_leap(year):
    leap = False

    if (year % 4) == 0:
        # divisible by 4
        leap = True

        if (not(year%100)) and (not(year%400)):
            # divisible by 100 and 400
            leap = True
        elif not (year%100):
            leap = False

    return leap


def main():
    year = int(input())
    print(is_leap(year))


if __name__ == '__main__':
    main()
