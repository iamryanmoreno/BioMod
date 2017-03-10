from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
import datetime
import time
import os
import threading
import sys


import datetime
import os
import threading
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.clock import Clock
from base import Base
import serial
from kivy.uix.screenmanager import ScreenManager, Screen


pop1 = Popup(title='Settings Popup', content=Label(text='To customize'),size_hint=(None,None),size=(1280,800))

class AppScreen(Screen):
	app = ObjectProperty()
	
class FirstForm(AppScreen):
        app1 = ObjectProperty()
        user = StringProperty()
				
        def pop_up(self):
                pop1.open()

class MainWindow(AppScreen):
        def exit_app(self):
                sys.exit()

	
class main(App, Base):
        def build(self):
                config = self.config
                self.title = "BioMOD"
                self.root = Builder.load_file('main.kv')
                Base.__init__(self)
                Clock.schedule_interval(self.display_datetime,1)
                return self.root
                
        def display_datetime(self, *args):
		#time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                date_now = datetime.datetime.now().strftime('%a %d %b %y')
                time_now = datetime.datetime.now().strftime('%X')
                self.root.ids['lb_date'].text = date_now
                self.root.ids['lb_time'].text = time_now
				
        
		
if __name__=='__main__':
	main().run()
