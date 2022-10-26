import sys
import datetime


def get_age(yyyy, mm, dd):

    dob = datetime.date(int(yyyy), int(mm), int(dd))
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age


def print_age(age):
    print(f'age is: {age}')


def main(yyyy, mm, dd):
    age = get_age(yyyy, mm, dd)
    print_age(age)


if __name__ == "__main__":
    print(f'entered: {sys.argv[1]},{sys.argv[2]},{sys.argv[3]}')
    main(sys.argv[1], sys.argv[2], sys.argv[3])
