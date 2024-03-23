from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import accountdb
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch


Window.size = (240, 560)

class LoginDB():
    account = accountdb.AccountDB()
    ev_id = []
    ev2 = []
    name = ''
    password = 0

class MainLayout(ScreenManager):
    pass

class AccountL(BoxLayout, Screen):
    def Log(self):
        print('Вход')
        if self.nameAc.text != '' and self.nameAc.text != '':
            LoginDB.account.GetAc(self.nameAc.text, int(self.passAc.text))
        if LoginDB.account.ac != []:
            self.login.text = 'Вход выполнен'
            LoginDB.name = self.nameAc.text
            LoginDB.password = int(self.passAc.text)
        print(LoginDB.account.ac)

    def Reg(self):
        print('Регистрация')
        if self.nameAc.text != '' and self.nameAc.text != '':
            LoginDB.account.ApAc(self.nameAc.text, int(self.passAc.text))
        print(LoginDB.account.ac)

class Account(BoxLayout, Screen):
    def Reset(self):
        print(LoginDB.account.ac)
        if LoginDB.account.ac != []:
            self.nameL.text = LoginDB.account.ac[1]
            print(LoginDB.account.ac[1])
        if LoginDB.account.ac != []:
            self.memL.text = str(LoginDB.account.ac[3])
            print(LoginDB.account.ac[3])
        if LoginDB.account.ac != []:
            self.orgL.text = str(LoginDB.account.ac[5])
            print(LoginDB.account.ac[5])
    def eventsU(self):
        if LoginDB.name != '' and LoginDB.password != '':
            LoginDB.account.GetEvU(LoginDB.account.ac[0])
            for i in range(len(LoginDB.account.ev)):
                LoginDB.ev2.append(LoginDB.account.ev[i][0])
            LoginDB.account.ev = LoginDB.ev2
            print(LoginDB.account.ev)
            LoginDB.ev_id = []
            for i in range(len(LoginDB.account.ev)):
                LoginDB.ev_id.append(LoginDB.account.ev[i][0])
            print('cr  ', LoginDB.ev_id)

    def eventsC(self):
        if LoginDB.name != '' and LoginDB.password != '':
            LoginDB.account.GetEvC(LoginDB.account.ac[0])
            for i in range(len(LoginDB.account.ev)):
                LoginDB.ev2.append(LoginDB.account.ev[i][0])
            LoginDB.account.ev = LoginDB.ev2
            print(LoginDB.account.ev)
            LoginDB.ev_id = []
            for i in range(len(LoginDB.account.ev)):
                LoginDB.ev_id.append(LoginDB.account.ev[i][0])
            print('cr  ', LoginDB.ev_id)


class Events(GridLayout, Screen):
    page = 1
    nom = 1
    def back(self):
        if Events.page > 0:
            Events.page -= 1
            if len(LoginDB.ev_id) > 5 * Events.page:
                self.name1.text = LoginDB.account.ev[5 * Events.page][1]
            else:
                self.name1.text = ''
            if len(LoginDB.ev_id) > 1 + 5 * Events.page:
                self.name2.text = LoginDB.account.ev[1 + 5 * Events.page][1]
            else:
                self.name2.text = ''
            if len(LoginDB.ev_id) > 2 + 5 * Events.page:
                self.name3.text = LoginDB.account.ev[2 + 5 * Events.page][1]
            else:
                self.name3.text = ''
            if len(LoginDB.ev_id) > 3 + 5 * Events.page:
                self.name4.text = LoginDB.account.ev[3 + 5 * Events.page][1]
            else:
                self.name4.text = ''
            if len(LoginDB.ev_id) > 4 + 5 * Events.page:
                self.name5.text = LoginDB.account.ev[4 + 5 * Events.page][1]
            else:
                self.name5.text = ''

    def next(self):
        if len(LoginDB.ev_id) > 5 * (Events.page + 1):
            Events.page += 1
            if len(LoginDB.ev_id) > 5 * Events.page:
                self.name1.text = LoginDB.account.ev[5 * Events.page][1]
            else:
                self.name1.text = ''
            if len(LoginDB.ev_id) > 1 + 5 * Events.page:
                self.name2.text = LoginDB.account.ev[1 + 5 * Events.page][1]
            else:
                self.name2.text = ''
            if len(LoginDB.ev_id) > 2 + 5 * Events.page:
                self.name3.text = LoginDB.account.ev[2 + 5 * Events.page][1]
            else:
                self.name3.text = ''
            if len(LoginDB.ev_id) > 3 + 5 * Events.page:
                self.name4.text = LoginDB.account.ev[3 + 5 * Events.page][1]
            else:
                self.name4.text = ''
            if len(LoginDB.ev_id) > 4 + 5 * Events.page:
                self.name5.text = LoginDB.account.ev[4 + 5 * Events.page][1]
            else:
                self.name5.text = ''
    def Page0(self):
        Events.page = 0
        if len(LoginDB.ev_id) > 0 and LoginDB.ev_id[0] != None:
            self.name1.text = LoginDB.account.ev[0][1]
        else:
            self.name1.text = ''
        if len(LoginDB.ev_id) > 1:
            self.name2.text = LoginDB.account.ev[1][1]
        else:
            self.name2.text = ''
        if len(LoginDB.ev_id) > 2:
            self.name3.text = LoginDB.account.ev[2][1]
        else:
            self.name3.text = ''
        if len(LoginDB.ev_id) > 3:
            self.name4.text = LoginDB.account.ev[3][1]
        else:
            self.name4.text = ''
        if len(LoginDB.ev_id) > 4:
            self.name5.text = LoginDB.account.ev[4][1]
        else:
            self.name5.text = ''
    def nom1(self):
        Events.nom = 1
    def nom2(self):
        Events.nom = 2
        print(Events.nom)
    def nom3(self):
        Events.nom = 3
    def nom4(self):
        Events.nom = 4
    def nom5(self):
        Events.nom = 5

class Event(GridLayout, Screen):
    def Reset(self):
        print(Events.page)
        if len(LoginDB.ev_id) > Events.nom + 5 * Events.page:
            self.nameE.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][1])
            self.desc.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][2])
            self.town.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][3])
            self.link.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][4])
            self.typeE.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][5])
            self.con.text = str(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][6])
    def regEv(self):
        if LoginDB.name != '' and LoginDB.password != '' and (len(LoginDB.ev_id) > Events.nom + 5 * Events.page):
            LoginDB.account.RegEv(LoginDB.account.ev[Events.page * 5 + Events.nom - 1][0], LoginDB.account.ac[0])
            LoginDB.account.GetAc(LoginDB.name, LoginDB.password)
        print(LoginDB.account.ac)


class Search(GridLayout, Screen):
    def searchAl(self):
        LoginDB.account.GetAllEv()
        LoginDB.ev_id = []
        for i in range(len(LoginDB.account.ev)):
            LoginDB.ev_id.append(LoginDB.account.ev[i][0])
        print(LoginDB.ev_id)

class Append(GridLayout, Screen):
    def create(self):
        if LoginDB.name != '' and LoginDB.password != '':
            LoginDB.account.ApEv(self.nameE.text, self.desc.text, self.town.text, self.link.text, self.typeE.text, self.con.text, LoginDB.account.ac[0])
            LoginDB.account.GetAc(LoginDB.name, LoginDB.password)
            print(LoginDB.account.ac)

class MainKApp(App):
    pass

MainKApp().run()