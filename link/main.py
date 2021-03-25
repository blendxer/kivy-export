from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pyjnius import autoclass, cast
import android

class ali(BoxLayout):
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
        url = 'https://{}'.format(self.tb.text)
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        browserIntent = Intent()
        browserIntent.setAction(Intent.ACTION_VIEW)
        browserIntent.setData(Uri.parse(url))
        currentActivity = cast('android.app.Activity', mActivity)
        currentActivity.startActivity(browserIntent)

class theApp(App):
    def build(self):
        return ali()

 
theApp().run()