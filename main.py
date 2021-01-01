import kivy
#App
from kivy.app import App
#UIX
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
#Misc
from kivy.properties import ObjectProperty
from plyer import vibrator
from plyer import notification

class MainInput(ScrollView):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols = 1, size_hint_y = None)
        self.add_widget(self.layout)

        self.calculation_history = Label(size_hint_y = None, markup = True)
        self.scroll_point = Label()
    
    def update_history(self,expression):

        self.calculation_history.text += '\n' + expression
        self.layout.height = self.calculation_history.texture_size[1] + 15
        #self.calculation_history.height = self.calculation_history.text_size[1]
        self.calculation_history.text_size = (self.calculation_history.width * 0.97,None)
        self.scroll_to(self.scroll_point)

    def changeToYellow(self):
        if self.text != "SyntaxERROR":
            self.background_color = (0.09,0.09,0.13,1)
            self.foreground_color = (0.52,0.63,0.78,1)
        else:
            self.foreground_color = (0.98,0.58,0.59,1)
            #self.foreground_color = (1,1,1,1)

class MainCal(FloatLayout):
    display = ObjectProperty(None)
    EvalText = ''
    last_out = 0

    def evaluate(self): 

        self.display.update_history('hello')
        '''
        self.volatile = self.display.text
        try:
            self.last_out = eval(self.display.text)
            self.display.text +='\n='+str(self.last_out) + '\n'
        except Exception as e:
            print(e)
            self.display.text = 'SyntaxERROR'
        '''

    def back_space(self):
        print('backspace pressed')
        '''if self.stooks == 0:
            self.display.text = self.volatile
            self.stooks = 1
        else:
            self.display.text = self.display.text[:-1]
            '''

    def copy_to_clipboard_and_notify(self):
        print('notified')
        #notification.notify('Calculator',' says hello')

class Keys(Button):
    def button_pressed(self):
        print('vibrated')
        #vibrator.vibrate(0.03)
class CalculatorApp(App):
    def build(self):    
        return MainCal()

    

if __name__ == "__main__":
    from kivy.config import Config
    Config.set('graphics', 'width', str(int(720)))
    Config.set('graphics', 'height', str(int(1280)))
    CalculatorApp().run()
    
