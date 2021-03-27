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


class URLShortner:

    def __init__(self):


    def shorten_url(self, long_url):

        #api_url = f"https://cutt.ly/api/api.php?key={self.api_key}&short={long_url}"
        r = requests.get('http://cutt.ly/api/api.php?key={}&stats={}'.format(self.api_key, long_url))

        #data = requests.get(api_url).json()["url"]
        #shortened_url = data["shortLink"]
        #return shortened_url
        return r.text


class URLShortener:

    def __init__(self):

        self.api_key = "e8ddf38a2ef45074c54626588dda833065383"

    def shorten_url(self, long_url):
    
        api_url = f"https://cutt.ly/api/api.php?key={self.api_key}&short={long_url}"
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            shortened_url = data["shortLink"]
        
        return shorten_url

"""

class URLShortner:

    def __init__(self):

        self.username = "o_6muh2ef1h3"
        self.password = "n8eB0e^D9cC^8sa"

    def get_access(self):

        auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(self.username, self.password))
        if auth_res.status_code == 200:
        # if response is OK, get the access token
            access_token = auth_res.content.decode()
        else:
            print("[!] Cannot get access token, exiting...")
            exit()

        return access_token

    def shorten_url(self, long_url):

        access_token = self.get_access()

        # construct the request headers with authorization
        headers = {"Authorization": f"Bearer {access_token}"}

        # get the group UID associated with our account
        groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
        if groups_res.status_code == 200:
            # if response is OK, get the GUID
            groups_data = groups_res.json()['groups'][0]
            guid = groups_data['guid']

        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": long_url}, headers=headers)
        if shorten_res.status_code == 200:
            # if response is OK, get the shortened URL
            link = shorten_res.json().get("link")

        return link
    """
