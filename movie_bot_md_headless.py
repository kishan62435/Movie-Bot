import time
import threading
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from selenium_f_headless import *
from selenium_f_headless import movie_bot
from  kivy.properties import ObjectProperty

 
class MovieBot(MDApp):
    mname = ObjectProperty(None)
    quality = ObjectProperty(None)
    Quality = ObjectProperty(None)
    link4 = ObjectProperty(None)
    link5 = ObjectProperty(None)


    checks = []
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Teal" 
        return Builder.load_file('kivy_bot_md.kv')
    
   
   
    def checkBox_click(self, instance, value, Q):
        global Quality
        if value==True:
            MovieBot.checks.append(Q)
            Quality=''
            for x in MovieBot.checks:
                Quality = f'{Quality}{x}'
           
        
        else:
            MovieBot.checks.remove(Q)
            Quality = ''
            for x in MovieBot.checks:
                Quality = f'{Quality} {x}'
        
    def complete(self, args):
            try:
                if(t1.is_alive() is False):
                    Clock.schedule_once(self.complete2, 5)
                    # self.root.ids.status.text = 'Searching completed, Now you can download or watch the movie!'
                    # global flag
                    # flag=0
            except:
                elf.root.ids.status.text = 'Searching for the movie  "' + mname + '" , please wait...'
    def complete2(self, args):
        try:
            self.root.ids.status.text = 'Searching completed.'
            global flag
            flag=0
        
        except:
            pass
            

    def status_sleep(self, *args):
            
            self.root.ids.status.text = 'Searching for the movie  "' + mname + '" , please wait...'
            Clock.schedule_interval(self.complete,1)    
    
    def search_button(self):
        
        try:
            global mname
            mname = self.root.ids.name.text 
            quality = Quality
    
                
            global link4,link5 
            
            global t1, flag
            flag=1
            t1 = threading.Thread(target = movie_bot, args= [mname, quality, self])
            t1.daemon = True
            t1.start()
            
            if(t1.is_alive()):
                
                flag=1
                self.status_sleep(self)
        except:
            pass
        
    def watcha(self):
        try:
            # print(flag)
            if(flag == 1):
                pass
            else:
                self.root.ids.status.text = ''
                t2 = threading.Thread(target=watch_nowa)
                t2.daemon = True
                t2.start()
        except:
            pass

    def watchb(self):
        try:
            # print(flag)
            if(flag == 1):
                pass
            else:
                self.root.ids.status.text = ''
                t4 = threading.Thread(target=watch_nowb)
                t4.daemon = True
                t4.start()
        except:
            pass
        
    def downloada(self):
        try:
            if(flag == 1):
                pass
            else:
                self.root.ids.status.text = ''
                t3 = threading.Thread(target=download_moviea)
                t3.daemon = True
                t3.start()
        except:
            pass
    
    def downloadb(self):
        try:
            if(flag == 1):
                pass
            else:
                self.root.ids.status.text = ''
                t5 = threading.Thread(target=download_movieb)
                t5.daemon = True
                t5.start()
        except:
            pass
        
    def close(self):
        exit(0)
    
MovieBot().run()