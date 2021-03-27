import gspread
import requests, urllib

class GetFromSheets:

    def __init__(self, key):

        self.key = key
        self.sheet = gspread.service_account().open_by_key(self.key)

    def get_worksheet(self, worksheet_no):

        sheet = self.sheet.get_worksheet(worksheet_no)

        return sheet

    def get_all_values_as_lists(self, worksheet_no):

        sheet = self.get_worksheet(worksheet_no)
        values_list = sheet.get_all_values()
        return values_list

    def get_all_values_as_dict(self, worksheet_no):

        sheet = self.get_worksheet(worksheet_no)
        values_dict = sheet.get_all_records()

        return values_dict

    def get_column(self, worksheet_no, column_no):

        sheet = self.get_worksheet(worksheet_no)
        column = sheet.col_values(column_no)

        return column

    def get_row(self, worksheet_no, row_no):

        sheet = self.get_worksheet(worksheet_no)
        row = sheet.row_values(row_no)

        return row

    def get_cell(self, worksheet_no, cell_co):

        sheet = self.open_sheets(self, worksheet_no)
        cell = sheet.acell(cell_no).value

        return cell


class UpdateSheets:

    def __init__(self, key, worksheet_no):

        self.key = key
        self.sheet = gspread.service_account().open_by_key(self.key)
        self.worksheet_no = worksheet_no
        self.worksheet = self.sheet.get_worksheet(self.worksheet_no)

    def update_cell(self, cell_no, cell_value):

        self.worksheet.update(cell_no, cell_value)


class Telegram:

    def __init__(self):

        self.url = "https://api.telegram.org/bot1347792998:AAGpgNdhA3-teAuTZSuoyMTv51OoPlHs5GQ"

    def send_message(self, chat_id, message):

        base_url = f"{self.url}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(base_url)
        return response


def URLShortener(long_url):

    api_key = "e8ddf38a2ef45074c54626588dda833065383"

    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={long_url}"
    data = requests.get(api_url).json()["url"]
    if data["status"] == 7:
        shortened_url = data["shortLink"]
    else:
        shortened_url = long_url

    return shortened_url
