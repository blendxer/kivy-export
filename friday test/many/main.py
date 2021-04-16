import os
from kivy.app import App
from kivy.lang import Builder
import plyer
import io

kv = '''
BoxLayout:
	orientation: 'vertical'
	Button:
		text: 'download update'
		on_release: app.download()
	Label:
		text: 'not thing yet'
		id: internet
	Button:
		text: 'check path'
		on_release: app.checkpath()
	Label:
		text: 'no thing yet'
		id: path
		multiline: True
	Button:
		text: 'get name'
		on_release: app.get_name()
	Label
		id: device_name
		text: 'no thing yet'

'''


class theapp(App):
	def build(self):
		return Builder.load_string(kv)

	def download(self):
		import gspread 
		cd = gspread.service_account(filename='credit.json')
		sh = cd.open_by_key('1jjNzQyRd67E7r4Knbq_FjLH-SHz5SHsUG4Q7K5GWzok')
		worksheet = sh.sheet1
		result  = worksheet.get_all_records()
		text = 'the target is {}'.format(result[0]['target'])
		self.root.ids.internet.text= text

	def checkpath(self):
		from android.permissions import request_permissions, Permission
		request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
		path = plyer.storagepath.get_pictures_dir()
		files = os.scandir(path)
		_list = []
		for i in files:
			_list.append(i.path)
		text = str(_list)
		self.root.ids.path.text = text
		
	def get_name(self):
		from jnius import autoclass
		name = autoclass('android.os.Build.MODEL')
		self.root.ids.device_name.text = str(name)


theapp().run()