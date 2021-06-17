from kivy.app import App
from kivy.event import ObjectWithUid 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
class MyGridLayout(GridLayout):
    t=ObjectProperty(None)
    m= ObjectProperty(None) 
    h=ObjectProperty(None)    
    o=ObjectProperty(None)
    def press(self):
        t=self.t.text 
        m=self.m.text 
        h=self.h.text
        if t=='' or m=='' or h=='':
            temp='Enter data'
        elif t.isalpha() or m.isalpha() or h.isalpha():
            temp='Value cant be alphabet'
        elif int(t)>50 and int(m)<1000 and int(h)<50:
            temp='Defective Thermometer'
        elif int(t)<50 and int(m)>1000 and int(h)<50:
            temp='Defective Tensiometer'
        elif int(t)<50 and int(m)<1000 and int(h)>50:
            temp='Defective Hygrometer'
        elif (25<=int(t)<=50) or (500<=int(m)<=1000):
            
            temp='Water Needed \nTime Required : %d mins\nWater Quantity : %d liters'%(((int(t)*100)//60),(int(m)//10*2))
        else:
            temp='Abnormal condition'
        self.o.text=temp
        self.t.text=''
        self.m.text=''
        self.h.text=''
Builder.load_string("""<MyGridLayout>
    t: Temperature
    m: Moisture
    h: Humidity
    o: output
    cols: 1
    GridLayout:
        cols: 1 
        size: root.width,root.height
        GridLayout:
            cols: 2 

            Label:
                text: "Temperature" 
                font_size: 25
                background_color: (244/255.0,122/255.0,96/255.0,1)
                canvas.before:
                    Color:
                        rgba: self.background_color 
                    RoundedRectangle:
                        size: self.size 
                        pos: self.pos
            TextInput:
                id: Temperature
                multiline: False 
            Label:
                text: "Moisture" 
                font_size: 25
                background_color: (127/255.0,231/255.0,220/255.0,1)
                #background_color: (245/255.0,190/255.0,220/180.0,1)
                canvas.before:
                    Color:
                        rgba: self.background_color 
                    RoundedRectangle:
                        size: self.size 
                        pos: self.pos
            TextInput:
                id: Moisture
                multiline: False 
            Label:
                text: "Humidity"
                font_size: 25 
                background_color: (52/255.0,213/255.0,235/255.0,1)
                canvas.before:
                    Color:
                        rgba: self.background_color 
                    RoundedRectangle:
                        size: self.size 
                        pos: self.pos
            TextInput:
                id: Humidity
                multiline: False 
    GridLayout:
        cols : 2

        Button:
            text: "Submit"
            font_size:32
            on_press: root.press()
            background_color: (127/255.0,231/255.0,220/255.0,1)
            canvas.before:
                Color:
                    rgba: self.background_color 
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos
        Label:
            id: output
            text: " "
            font_size: 32
            background_color: (31/255.0,191/255.0,184/255.0,1)
            canvas.before:
                Color:
                    rgba: self.background_color 
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos""")
class program(App):
    def build(self):
        return MyGridLayout()

program().run()
