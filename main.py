import kivy

from kivy.app import App
from kivy.uix.label import Label

class Myapp(App):
    
    def build(self):
        return Label(text='Hello 3atay')
    
if __name__ == '__main___':
    Myapp().run()