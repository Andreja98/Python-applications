from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        # Self referencira na instancu tekuce klase LoginScreen. Self je objekat koji je instanciran od klase LoginScreen
        # Manager je property od Screen posto je nasledjen od Screen pa nam daje pristup manager-u
        # Manager ima svoj atribut current kome pristupamo kako bi promenili screen
        self.manager.current = "sign_up_screen"

    def login(self, input_username, input_password):
        with open("users.json", "r") as file:
            users = json.load(file)
            if input_username in users and users[input_username]['password'] == input_password:
                self.manager.current = "login_screen_success"
            else:
                self.ids.login_wrong.text = "Wrong username or password!"


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, input_username, input_password):
        with open("users.json") as file:
            users = json.load(file)
        users[input_username] = {'username': input_username, 'password': input_password,
                                   'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feeling):
        feel = feeling.lower()
        available_feelings = glob.glob("quotes/*txt")
        # Stem nam daje samo naziv fajlova, bez ekstenzije txt, iz quotes foldera (happy, sad, unloved)
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feeling in available_feelings:
            with open(f"quotes/{feeling}.txt", encoding="utf8") as file:
                # Daje nam listu svih quotes
                quotes = file.readlines()
            self.ids.qoute.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        # Vraca objekat RootWidget a ne klasu zbog ()
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()