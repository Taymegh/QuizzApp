
from kivy.app import App
from kivy.uix.label import Label

class AppQuizz(App):
    
    def build(self):
        return Label(text='Hello 3atay')
    
if __name__ == '__main__':
    AppQuizz().run()