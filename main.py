from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""
<Calculator>:
    orientation: 'vertical'

    FloatLayout:

        size: (20, 20)

        Label:
            id: expressionLabel
            size_hint: (.10, .10)
            pos: (300, 450)
            text: ''
            color: (143, 143, 143, 1)
            font_size: 20

        Label:
            id: resultLabel
            size_hint: (.10, .10)
            pos: (300, 400)
            text: ''
            font_size: 24

    GridLayout:

        cols: 4
        rows: 5

        Button:
            id: btnC
            text: 'C'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                resultLabel.text = ''
                expressionLabel.text = ''

        Button:
            id: btnDel
            text: 'DEL'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press: resultLabel.text = resultLabel.text[:-1]

        Button:
            id: btnPerc
            text: '%'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                if(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btnDiv
            text: '/'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                if(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btn7
            text: '7'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn8
            text: '8'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn9
            text: '9'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btnMul
            text: '*'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                if(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btn4
            text: '4'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn5
            text: '5'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn6
            text: '6'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btnMinus
            text: '—'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                if(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btn1
            text: '1'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn2
            text: '2'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btn3
            text: '3'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press: resultLabel.text += self.text

        Button:
            id: btnPlus
            text: '+'
            background_color: (0.2,0.2,0.2,0.7)
            font_size: 20
            on_press:
                if(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btn00
            text: '00'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press:
                if(len(resultLabel.text) != 0): resultLabel.text += self.text

        Button:
            id: btn0
            text: '0'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press:
                resultLabel.text += self.text

        Button:
            id: btnCom
            text: '.'
            background_color: (0.1,0.1,0.1,0.7)
            font_size: 20
            on_press:
                if(len(resultLabel.text) == 0): resultLabel.text += '0.'
                elif(root.CheckingSigns(resultLabel.text)): resultLabel.text += self.text

        Button:
            id: btnEqual
            text: '='
            background_color: (1,0.3,0.1,1)
            background_normal: ''
            font_size: 20
            on_press:
                root.Calculation(resultLabel.text)
""")

class Calculator(BoxLayout):

    def CheckingSigns(self, string):
        # Проверяет знаки в выражении
        if len(string) == 0: return False
        else:
            signs = ['+','—','/','*','%']
            for s in signs:
                if s in string: return False
        return True

    def StringToNumbers(self, string, operation):
        # Преобразует строки в числа
        num1, num2 = string.split(operation)
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                num1 = str(num1)
                num2 = str(num2)
        return num1, num2

    def Calculation(self, str_input):
        # Производит расчет
        if "+" in str_input:
            num1, num2 = self.StringToNumbers(str_input, "+")
            if num1 == "" or num2 == "":
                if num1 == "": res = num2
                elif num2 == "": res = num1
                str_input = str_input[:-1]
            else: res = num1 + num2
        elif "—" in str_input:
            num1, num2 = self.StringToNumbers(str_input, "—")
            if num1 == "" or num2 == "":
                if num1 == "": res = num2
                elif num2 == "": res = num1
                str_input = str_input[:-1]
            else: res = num1 - num2
        elif "/" in str_input:
            num1, num2 = self.StringToNumbers(str_input, "/")
            if num1 == "" or num2 == "":
                if num1 == "": res = num2
                elif num2 == "": res = num1
                str_input = str_input[:-1]
            else:
                try:
                    res = num1 / num2
                except ZeroDivisionError:
                    res = "Error"
        elif "*" in str_input:
            num1, num2 = self.StringToNumbers(str_input, "*")
            if num1 == "" or num2 == "":
                if num1 == "": res = num2
                elif num2 == "": res = num1
                str_input = str_input[:-1]
            else: res = num1 * num2
        elif "%" in str_input:
            str_input = str_input.replace("%", "")
            num1: float = float(str_input)
            res = num1 * 0.01
        else:
            res = str_input

        # Вывод результата
        self.ids.resultLabel.text = str(res)
        self.ids.expressionLabel.text = str_input + "="




class myApp(App):
    def build(self):
        Window.size = (360, 600)
        return Calculator()


if __name__ == "__main__":
    myApp().run()