from CustomModule import GetFromSheets, Telegram, URLShortner
from datetime import date, datetime


def open_sheets():

    key = "11KHLVts1FfKidqPUlInAHpAeFUdTu3lIZXlj1udv-wM"
    sheet = GetFromSheets(key)

    return sheet

def get_reminders():

    sheet = open_sheets()
    data = sheet.get_all_values_as_lists(0)

    print(data)
    return data


def get_today(data):

    reminders = []
    current_time = datetime.now()
    counter = 0
    date_range = 10

    while counter <= len(data):
        data_row = data(counter)
        remind_datetime = datetime.strptime(data_row[5], '%y/%m/%d %H:%M:%S')
        if remind_datetime >= current_time:
            reminders.append(data_row)
        count += 1
    print(reminders)
    return reminders


def get_id():

    sheet = open_sheets()
    telegram_id = sheet.get_all_values_as_list(1)

    telegram_id_dict = {}
    i = 0
    for i in range(len(telegram_id)):
        data_row = telgram_id[i]
        name = data_row[0]
        value = data_row[1]
        telegram_id_dict[name] = value

    print(telegram_id)
    return telegram_id


def send_reminders(telegram_id, reminders):

    pass


def main():

    data = get_reminders()
    reminders = get_today(data)
    #tel_id = get_id()


if __name__ == '__main__':
    main()
