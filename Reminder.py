from CustomModule import GetFromSheets, Telegram, URLShortener, UpdateSheets
from datetime import date, datetime
from time import sleep


def open_sheets():

    key = "11KHLVts1FfKidqPUlInAHpAeFUdTu3lIZXlj1udv-wM"
    sheet = GetFromSheets(key)

    return sheet

def get_reminders():

    sheet = open_sheets()
    data = sheet.get_all_values_as_lists(0)

    return data


def get_today(data):

    reminders = []
    current_time = datetime.now()

    del data[0]
    for rem in data:
        remind_datetime = datetime.strptime(rem[4], '%m/%d/%Y %H:%M:%S')
        if remind_datetime <= current_time:
            if rem[7] != "SEND":
                reminders.append(rem)
    return reminders


def get_id():

    sheet = open_sheets()
    telegram_id = sheet.get_all_values_as_lists(1)

    telegram_id_dict = {}
    i = 0
    for i in range(len(telegram_id)):
        data_row = telegram_id[i]
        name = data_row[0]
        value = data_row[1]
        telegram_id_dict[name] = value

    return telegram_id_dict


def send_reminders(url, tele, telegram_id, reminders):


    reminders_send = []
    for rem in reminders:
        name = rem[1]
        remind_name = rem[2]
        users = remind_name.split(",")
        content = rem[3]
        if remind_name in telegram_id:
            for remindeer.strip() in users:
                message = f"Reminder from {name} Regarding \"{content}\".Use \"{url}\" link to reschedule your reminder."
                tele.send_message(int(telegram_id[remindeer]), message)
                reminders_send.append(rem)

    return reminders_send


def re_update(reminders_send):

    key = "11KHLVts1FfKidqPUlInAHpAeFUdTu3lIZXlj1udv-wM"
    A = GetFromSheets(key)
    B = UpdateSheets(key, 0)

    i = 0
    data_row = A.get_column(0, 7)
    for row in reminders_send:
        S_ID = row[6]
        for count in data_row:
            if count == S_ID:
                #B.update_cell(f"H{i+1}", "SEND")
                B.delete_rows(int(S_ID) + 1)
            i+=1

def main():

    data = get_reminders()
    reminders = get_today(data)
    if len(reminders) > 0:
        tel_id = get_id()
        long_url = reminders[0][5]
        url = URLShortener(long_url)
        tele = Telegram()
        rem_send = send_reminders(url=url, tele=tele, telegram_id=tel_id, reminders=reminders)
        re_update(rem_send)
