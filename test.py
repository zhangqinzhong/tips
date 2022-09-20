import datetime

if __name__ == '__main__':
    print(datetime.date.today())

    today = datetime.date.today().__str__()
    a = 'wo' + today + 'a'
    print(a)