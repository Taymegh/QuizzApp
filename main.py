import kivy

a= 1

from kivy.app import App
from kivy.uix.label import Label


class MyQuizz(App):
    def build(self):
        return Label(text="Enfin")
    


if __name__ == '__main__':
    MyQuizz.run()

    