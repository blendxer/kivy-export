from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from jnius import autoclass

class ali(BoxLayout):
    s = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bt = Button(text='open the link',on_release= self._press)
        tt = BoxLayout(orientation='vertical')
        self.tb = TextInput(text='meet.google.com/yja-ohqh-ehx')
        box_2 = BoxLayout()
        tt.add_widget(bt)
        tt.add_widget(self.tb)
        tt.add_widget(box_2)
        self.add_widget(tt)


    def _press(self, *args):
        if self.s == 7:
            self.currentActivity.startActivity(self.browserIntent)
            self.s = 0
        if self.s == 6:
            self.currentActivity = cast('android.app.Activity', mActivity)
            self.s = 7
        if self.s == 5:
            self.browserIntent.setData(self.Uri.parse(self.url))
            self.s = 6
        if self.s == 4:
            self.browserIntent.setAction(self.Intent.ACTION_VIEW)
            self.s = 5
        if self.s == 3:
            self.browserIntent = self.Intent()
            self.s = 4
        if self.s == 2:
            self.Uri = autoclass('android.net.Uri')
            self.s = 3
        if self.s == 1:
            self.Intent = autoclass('android.content.Intent')
            self.s =2
        if self.s == 0:
            self.url = 'https://{}'.format(self.tb.text)
            self.s = 1

class theApp(App):
    def build(self):
        return ali()

 
theApp().run()