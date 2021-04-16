from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import gspread , oauth2client.service_account
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

Kv = '''
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'update text'
        on_release: app.download()
    Label:
        id : label
        text: 'not run yet'
'''


class theapp(App):
    def build(self):
        return Builder.load_string(Kv)

    def download(self):
        credit = ServiceAccountCredentials.from_json_keyfile_name('file\\credit.json', scope)
        client = gspread.authorize(credit)
        sheet = client.open('E').sheet1
        data = sheet.get_all_records()
        downlad = data[0]
        text = 'the wanted {} \n check time {} \n unwanted {} '.format(downlad["T"],downlad['te'], downlad['tn'])
        self.root.ids.label.text = text
theapp().run()
