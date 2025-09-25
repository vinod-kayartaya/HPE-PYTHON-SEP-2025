from datetime import datetime, date, timedelta


def main():
    current_time = datetime.now()
    print(f'{current_time = }')
    today = date.today()
    print(f'{today.isoformat() = }')

    bday = datetime(1974, 1, 20, 4, 30, 0)
    print(bday)
    print(bday.strftime('%B %d, %Y, %H:%M %p'))

    user_dob = input('Enter your birth date in DD/MM/YYYY format: ')
    print(f'{type(user_dob) = }, {user_dob = }')
    user_dob = datetime.strptime(user_dob, '%d/%m/%Y')
    print(f'{type(user_dob) = }, {user_dob = }')
    print(f'You were born in the month of {user_dob.strftime('%B')}.')

    today = datetime.now()
    print("Today:", today)

    # Add 10 days
    future = today + timedelta(days=10)
    print("10 days later:", future)
    _200_days_back = today - timedelta(days=200)
    print('200 days back, it was', _200_days_back)

    d1 = date(2025, 9, 23)
    d2 = date(2025, 12, 25)

    diff = d1 - d2
    print(f'{type(diff) = }, {diff = }')


if __name__ == '__main__':
    main()
