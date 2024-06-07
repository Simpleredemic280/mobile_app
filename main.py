from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from data import Data


global name
name = None
global age
age = None


class MainScreen(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        instr = Label(text="Тест Руф'є - це тест який перевірить працездатність серцево-судинної системи. Впиши ім'я та вік.")
        self.name_input = TextInput(text='name', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        self.age_input = TextInput(text='age', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.next_button.on_press = self.next

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.3))
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)
        line2.add_widget(self.name_input)
        line2.add_widget(self.age_input)
        line2.add_widget(self.next_button)
        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def next(self):
        name = self.name_input.text
        age = self.age_input.text
        self.manager.current = 'heart_beat_check'


class HeartBeatCheckScreen(Screen):
    def __init__(self, name='heart_beat_check'):
        super().__init__(name="heart_beat_check")
        instr = Label(text="Поміряти пульс, протягом 15 секунд. Запиши результат.")
        self.results_input = TextInput(text='Results', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.start_btn = Button(text="Почати вимірювання", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.timer_value = 15
        self.timer = Label(text=str(self.timer_value), size_hint=(0.1, 1))
        self.timer_event = None

        self.next_button.on_press = self.next
        self.start_btn.on_press = self.start_timer

        self.next_button.set_disabled(True)
        self.results_input.set_disabled(True)

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.4))
        line2_1 = BoxLayout(orientation="horizontal", size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5})
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)

        line2_1.add_widget(self.start_btn)
        line2_1.add_widget(self.timer)

        line2.add_widget(line2_1)
        line2.add_widget(self.results_input)
        line2.add_widget(self.next_button)

        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def timerTick(self, dt):
        if self.timer_value >= 0:
            self.timer_value -= 0.1
            self.timer.text = str(round(self.timer_value, 1))
        else:
            self.next_button.set_disabled(False)
            self.results_input.set_disabled(False)
            return False

    def start_timer(self):
        self.start_btn.set_disabled(True)
        self.timer_event = Clock.schedule_interval(self.timerTick, 0.1)

    def next(self):
        self.manager.current = 'set'

class SetCheckScreen(Screen):
    def __init__(self, name="set"):
        super().__init__(name="set")
        instr = Label(text="Зробити 30 присідань за 45 сек.")
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.start_btn = Button(text="Почати вимірювання", size_hint=(0.4, None), height='60sp',pos_hint={'center_x': 0.5})
        self.timer_value = 45
        self.timer = Label(text=str(self.timer_value), size_hint=(0.1, 1))
        self.timer_event = None

        self.next_button.on_press = self.next
        self.start_btn.on_press = self.start_timer

        self.next_button.set_disabled(True)

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.4))
        line2_1 = BoxLayout(orientation="horizontal", size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5})
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)

        line2_1.add_widget(self.start_btn)
        line2_1.add_widget(self.timer)

        line2.add_widget(line2_1)
        line2.add_widget(self.next_button)

        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def timerTick(self, dt):
        if self.timer_value >= 0:
            self.timer_value -= 0.1
            self.timer.text = str(round(self.timer_value, 1))
        else:
            self.next_button.set_disabled(False)
            self.results_input.set_disabled(False)
            return False

    def start_timer(self):
        self.start_btn.set_disabled(True)
        self.timer_event = Clock.schedule_interval(self.timerTick, 0.1)

    def next(self):
        self.manager.current = 'seat_set'

class SeatSetScreen(Screen):
    def __init__(self, name="seat_set"):
        super().__init__(name="seat_set")
        instr = Label(text="Виміряти пульс за 15 секунд. Запиши результат. ")
        self.results_input = TextInput(text='Results', multiline=False, size_hint=(0.4, 0.1),pos_hint={'center_x': 0.5})
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.start_btn = Button(text="Почати вимірювання", size_hint=(0.4, None), height='60sp',pos_hint={'center_x': 0.5})
        self.timer_value = 15
        self.timer = Label(text=str(self.timer_value), size_hint=(0.1, 1))
        self.timer_event = None

        self.next_button.on_press = self.next
        self.start_btn.on_press = self.start_timer

        self.next_button.set_disabled(True)
        self.results_input.set_disabled(True)

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.4))
        line2_1 = BoxLayout(orientation="horizontal", size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5})
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)

        line2_1.add_widget(self.start_btn)
        line2_1.add_widget(self.timer)

        line2.add_widget(line2_1)
        line2.add_widget(self.results_input)
        line2.add_widget(self.next_button)

        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def timerTick(self, dt):
        if self.timer_value >= 0:
            self.timer_value -= 0.1
            self.timer.text = str(round(self.timer_value, 1))
        else:
            self.next_button.set_disabled(False)
            self.results_input.set_disabled(False)
            return False

    def start_timer(self):
        self.start_btn.set_disabled(True)
        self.timer_event = Clock.schedule_interval(self.timerTick, 0.1)

    def next(self):
        self.manager.current = 'rest'

class RestScreen(Screen):
    def __init__(self, name="rest"):
        super().__init__(name="rest")
        instr = Label(text="Виміряти пульс протягом 15 секунд. Запиши результат.")
        self.results_input = TextInput(text='Results', multiline=False, size_hint=(0.4, 0.1), pos_hint={'center_x': 0.5})
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.start_btn = Button(text="Почати вимірювання", size_hint=(0.4, None), height='60sp',pos_hint={'center_x': 0.5})
        self.timer_value = 15
        self.timer = Label(text=str(self.timer_value), size_hint=(0.1, 1))
        self.timer_event = None

        self.next_button.on_press = self.next
        self.start_btn.on_press = self.start_timer

        self.next_button.set_disabled(True)
        self.results_input.set_disabled(True)

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.4))
        line2_1 = BoxLayout(orientation="horizontal", size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5})
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)

        line2_1.add_widget(self.start_btn)
        line2_1.add_widget(self.timer)

        line2.add_widget(line2_1)
        line2.add_widget(self.results_input)
        line2.add_widget(self.next_button)

        layout.add_widget(line1)
        layout.add_widget(line2)

        self.add_widget(layout)

    def timerTick(self, dt):
        if self.timer_value >= 0:
            self.timer_value -= 0.1
            self.timer.text = str(round(self.timer_value, 1))
        else:
            self.next_button.set_disabled(False)
            self.results_input.set_disabled(False)
            return False

    def start_timer(self):
        self.start_btn.set_disabled(True)
        self.timer_event = Clock.schedule_interval(self.timerTick, 0.1)


    def next(self):
        self.manager.current = 'results'


class ResultsScreen(Screen):
    def __init__(self, name="results"):
        super().__init__(name="results")
        instr = Label(text="Results")
        self.next_button = Button(text="Next", size_hint=(0.4, None), height='60sp', pos_hint={'center_x': 0.5})
        self.next_button.on_press = self.next

        line1 = BoxLayout()
        line2 = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.3))
        layout = BoxLayout(orientation="vertical", padding=5)

        line1.add_widget(instr)
        line2.add_widget(self.next_button)
        layout.add_widget(line1)
        layout.add_widget(line2)
        self.add_widget(layout)

    def next(self):
        self.manager.current = 'main'


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.data = Data()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        sm.add_widget(HeartBeatCheckScreen())
        sm.add_widget(SeatSetScreen())
        sm.add_widget(RestScreen())
        sm.add_widget(ResultsScreen())
        return sm


app = MyApp()
app.run()