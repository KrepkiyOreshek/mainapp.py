# pip install kivy
# pip install kivymd
# pip install https://github.com/kivymd/KivyMD/archive/3274d62/.zip
import math

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivymd.uix.pickers import MDDatePicker
import datetime

import pandas as pd
import numpy as np

KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.

<TooltipMDIconButton@MDIconButton+MDTooltip>

<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    MDNavigationDrawerHeader:
        title: "Калькулятор"
        text: "дополнительного отпуска"
        spacing: "4dp"
        padding: "12dp", 0, 0, "56dp"

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/Calculator_30001.png"
        
    MDRectangleFlatIconButton:
        icon: 'check-network'
        text: "Изменить фон - {}".format(app.theme_cls.theme_style)
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        line_color: 0.18431, 0.3098, 0.3098
        icon_color: 1, 1, 1, 1
        md_bg_color: 0.18431, 0.3098, 0.3098
        on_release: app.switch_theme_style()
        pos_hint: {"center_x": .5}

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0.18431, 0.3098, 0.3098

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        text_color_active: "orange"
                        background_color: 0.18431, 0.3098, 0.3098
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator']}[/size][/font] 1. Калькулятор"

                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-alert"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098
                                        # icon_size: root.height/25
                                        
                                    MDTextField:
                                        id: star
                                        hint_text: "Макс. кол-во дней допотпуска в вашей организации"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число"
                                        # font_size: root.height/35


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-clock"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDTextField:
                                        id: loan
                                        hint_text: "Кол-во рабочих дней в году по производственному календарю"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-check"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDTextField:
                                        id: months
                                        hint_text: "Кол-во дней, фактически отработанных во вредных условиях"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число"
                                        helper_text: "Расчитать этот параметр можно в расчетном календаре"
                                        helper_text_mode: "persistent"
                                        helper_text_color_normal: "green"
                                        helper_text_color_focus: "green"
                                        
                                    # TooltipMDIconButton:
                                        # icon: "account-question"
                                        # tooltip_text: "Расчитать этот параметр можно в расчетном календаре"
                                        
                                # BoxLayout:
                                    # orientation: 'vertical'                                    
                                        
                                    # MDRectangleFlatIconButton:
                                        # icon: 'arrow-left-circle'
                                        # text: "Расчитать этот папаметр"
                                        # theme_text_color: "Custom"
                                        # text_color: 1, 1, 1, 1
                                        # line_color: 0, 0, 0, 1
                                        # icon_color: 0.0, 0.50196, 0.0, 1
                                        # md_bg_color: 0.1, 0.1, 0.1, 1
                                        # pos_hint: {"center_x": .5, "center_y": .6}
                                        # on_release: app.switch_tab_by_name()
                                        # font_size: root.height/50

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-remove"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDTextField:
                                        id: interest
                                        hint_text: "Кол-во дней допотпуска, использованных в этом году"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число ( По умолчанию '0' )"

                                    # MDTextField:
                                    #    id: payment_type
                                    #    hint_text: "Payment type"
                                    #    on_focus: if self.focus: app.menu.open()
                                    
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "check-circle"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDRoundFlatButton:
                                        id: inters
                                        text: "Результат"
                                        theme_text_color: "Custom"
                                        text_color: "green"
                                        line_color: 0.18431, 0.3098, 0.3098
                                        adaptive_width: True
                                        # font_size: root.height/40
                                        
                                        
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: "center"
                                        
                                        MDRectangleFlatIconButton:
                                            icon: 'check-circle'
                                            text: "РАСЧИТАТЬ"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0.18431, 0.3098, 0.3098
                                            icon_color: 1, 1, 1, 1
                                            md_bg_color: 0.64706, 0.16471, 0.16471
                                            theme_text_color: "Custom"
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)
                                            # font_size: root.height/40
                                        
                                MDSeparator:
                                    height: "1dp"
                                                            
                        Tab:
                            id: tab2
                            name: 'tab2'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calendar']}[/size][/font] 2. Расчетный календарь"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-arrow-left"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "Дата выхода на работу"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число"
                                        on_focus: if self.focus: app.date_dialog.open()
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-arrow-right"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDTextField:
                                        id: start
                                        hint_text: "Дата последнего рабочего дня перед уходом в отпуск"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число"
                                        on_focus: if self.focus: app.date_dialog2.open()
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-remove"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDTextField:
                                        id: dat
                                        hint_text: "Количество дней отсутствия на работе (отпуск, больничный)"
                                        line_color_normal: 0.18431, 0.3098, 0.3098
                                        text_color_normal: 0.18431, 0.3098, 0.3098
                                        hint_text_color_normal: 0.18431, 0.3098, 0.3098
                                        required: True
                                        helper_text_mode: "on_error"
                                        helper_text: "Введите число ( По умолчанию '0' )"
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-check"
                                        theme_icon_color: "Custom"
                                        icon_color: 0.18431, 0.3098, 0.3098

                                    MDRoundFlatButton:
                                        id: date
                                        text: "Результат"
                                        theme_text_color: "Custom"
                                        text_color: "green"
                                        line_color: 0.18431, 0.3098, 0.3098
                                        adaptive_width: True
                                        # font_size: root.height/40
                                        
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    AnchorLayout:
                                        anchor_x: "center"
                                        
                                        MDRectangleFlatIconButton:
                                            icon: 'check-circle'
                                            text: "РАСЧИТАТЬ"
                                            theme_text_color: "Custom"
                                            text_color: 1, 1, 1, 1
                                            line_color: 0.18431, 0.3098, 0.3098
                                            icon_color: 1, 1, 1, 1
                                            md_bg_color: 0.64706, 0.16471, 0.16471
                                            theme_text_color: "Custom"
                                            adaptive_width: True
                                            on_release: app.calc_table(*args)
                                            # font_size: root.height/40

                            
                        # Tab:
                        #    id: tab3
                        #    name: 'tab3'
                        #    title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                            
                        # Tab:
                        #    id: tab4
                        #    name: 'tab4'
                        #    title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                            
                        # Tab:
                        #    id: tab5
                        #    name: 'tab5'
                        #    title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class DopOtpuskCalculatorApp(MDApp):
    title = "Калькулятор дополнительного отпуска"
    by_who = "by E.N."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icons = None
        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        # menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        # menu_items = [{"icon": "format-text-rotation-angle-up", "text": 'annuity'},
        #              {"icon": "format-text-rotation-angle-down", "text": 'differentiated'}]
        # self.menu = MDDropdownMenu(
        #    caller=self.screen.ids.payment_type,
        #    items=menu_items,
        #    position="auto",
        #    width_mult=4,
        # )
        # self.menu.bind(on_release=self.set_item)

        # https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog = MDDatePicker(primary_color=(0.18431, 0.3098, 0.3098),
                                        selector_color=(0.18431, 0.3098, 0.3098)
                                        )
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)

        # https://kivymd.readthedocs.io/en/latest/components/pickers/?highlight=date%20picker#
        self.date_dialog2 = MDDatePicker(primary_color=(0.18431, 0.3098, 0.3098),
                                         selector_color=(0.18431, 0.3098, 0.3098)
                                         )
        self.date_dialog2.bind(on_save=self.on_save2, on_cancel=self.on_cancel2)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)
        self.screen.ids.start_date.text = value.strftime("%d-%m-%Y")  # str(date)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def on_save2(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        print(instance, value, date_range)
        self.screen.ids.start.text = value.strftime("%d-%m-%Y")  # str(date)

    def on_cancel2(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        # self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        # return Builder.load_string(KV)
        return self.screen

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.start.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.star.text = "7"
        self.screen.ids.loan.text = "247"
        self.screen.ids.months.text = "142"
        self.screen.ids.interest.text = "0"
        self.screen.ids.dat.text = "0"
        self.screen.ids.date.text = "Результат (дни): ""0"
        self.screen.ids.inters.text = "Результат (дни): ""0"
        # self.screen.ids.payment_type.text = "annuity"

        icons_item_menu_lines = {
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #    self.root.ids.tabs.add_widget(
        #        Tab(
        #            title=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #        )
        #    )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked!" + tab_text)

    def switch_tab_by_name(self):
        '''Switching the tab by name.'''

        try:
            x = f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calendar']}[/size][/font] 2. Расчетный календарь"
            print(f"Switch slide by name, next element to show: [{x}]")
            self.root.ids.tabs.switch_tab(x)
        except StopIteration:
            # Reset the iterator an begin again.
            self.iter_list_names = iter(list(self.icons))
            self.switch_tab_by_name()

    def on_star_click(self):
        print("tab clicked!")

    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text
        start = self.screen.ids.start.text
        dat = self.screen.ids.dat.text
        print(start_date + " " + start)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        start = datetime.datetime.strptime(self.screen.ids.start.text, "%d-%m-%Y").date()
        # holidays = pd.to_datetime("04/10/2022", format="%d/%m/%Y").date()
        delta = np.busday_count(start_date, start, weekmask="1111111",
                                holidays=["2016-01-01", "2016-01-02", "2016-01-03", "2016-01-04", "2016-01-05",
                                          "2016-01-06", "2016-01-07", "2016-01-08", "2016-01-09", "2016-01-10",
                                          "2016-01-16", "2016-01-17", "2016-01-23", "2016-01-24", "2016-01-30",
                                          "2016-01-31", "2016-02-06", "2016-02-07", "2016-02-13", "2016-02-14",
                                          "2016-02-21", "2016-02-22", "2016-02-23", "2016-02-27", "2016-02-28",
                                          "2016-03-05", "2016-03-06", "2016-03-07", "2016-03-08", "2016-03-12",
                                          "2016-03-13", "2016-03-19", "2016-03-20", "2016-03-26", "2016-03-27",
                                          "2016-04-02", "2016-04-03", "2016-04-09", "2016-04-10", "2016-04-16",
                                          "2016-04-17", "2014-04-23", "2016-04-24", "2016-04-30", "2016-05-01",
                                          "2016-05-02", "2016-05-03", "2016-05-07", "2016-05-08", "2016-05-09",
                                          "2016-05-14", "2016-05-15", "2016-05-21", "2016-05-22", "2016-05-28",
                                          "2016-05-29", "2016-06-04", "2016-06-05", "2016-06-11", "2016-06-12",
                                          "2016-06-13", "2016-06-18", "2016-06-19", "2016-06-25", "2016-06-26",
                                          "2016-07-02", "2016-07-03", "2016-07-09", "2016-07-10", "2016-07-16",
                                          "2016-07-17", "2016-07-23", "2016-07-24", "2016-07-30", "2016-07-31",
                                          "2016-08-06", "2016-08-07", "2016-08-13", "2016-08-14", "2016-08-20",
                                          "2016-08-21", "2016-08-27", "2016-08-28", "2016-09-03", "2016-09-04",
                                          "2016-09-10", "2016-09-11", "2016-09-17", "2016-09-18", "2016-09-24",
                                          "2016-09-25", "2016-10-01", "2016-10-02", "2016-10-08", "2016-10-09",
                                          "2016-10-15", "2016-10-16", "2016-10-22", "2016-10-23", "2016-10-29",
                                          "2016-10-30", "2016-11-04", "2016-11-05", "2016-11-06", "2016-11-12",
                                          "2016-11-13", "2016-11-19", "2016-11-20", "2016-11-26", "2016-11-27",
                                          "2016-12-03", "2016-12-04", "2016-12-10", "2016-12-11", "2016-12-17",
                                          "2016-12-18", "2016-12-24", "2016-12-25", "2016-12-31", "2017-01-01",
                                          "2017-01-02", "2017-01-03", "2017-01-04", "2017-01-05", "2017-01-06",
                                          "2017-01-07", "2017-01-08", "2017-01-14", "2017-01-15", "2017-01-21",
                                          "2017-01-22", "2017-01-28", "2017-01-29", "2017-02-04", "2017-02-05",
                                          "2017-02-11", "2017-02-12", "2017-02-18", "2017-02-19", "2017-02-23",
                                          "2017-02-24", "2017-02-25", "2017-02-26", "2017-03-04", "2017-03-05",
                                          "2017-03-08", "2017-03-11", "2017-03-12", "2017-03-18", "2017-03-19",
                                          "2017-03-25", "2017-03-26", "2017-04-01", "2017-04-02", "2017-04-08",
                                          "2017-04-09", "2017-04-15", "2017-04-16", "2017-04-22", "2017-04-23",
                                          "2017-04-29", "2017-04-30", "2017-05-01", "2017-05-06", "2017-05-07",
                                          "2017-05-08", "2017-05-09", "2017-05-13", "2017-05-14", "2017-05-20",
                                          "2017-05-21", "2017-05-27", "2017-05-28", "2017-06-03", "2017-06-04",
                                          "2017-06-10", "2017-06-11", "2017-06-12", "2017-06-17", "2017-06-18",
                                          "2017-06-24", "2017-06-25", "2017-07-01", "2017-07-02", "2017-07-08",
                                          "2017-07-09", "2017-07-15", "2017-07-16", "2017-07-22", "2017-07-23",
                                          "2017-07-29", "2017-07-30", "2017-08-05", "2017-08-06", "2017-08-12",
                                          "2017-08-13", "2017-08-19", "2017-08-20", "2017-08-26", "2017-08-27",
                                          "2017-09-02", "2017-09-03", "2017-09-09", "2017-09-10", "2017-09-16",
                                          "2017-09-17", "2017-09-23", "2017-09-24", "2017-09-30", "2017-10-01",
                                          "2017-10-07", "2017-10-08", "2017-10-14", "2017-10-15", "2017-10-21",
                                          "2017-10-22", "2017-10-28", "2017-10-29", "2017-11-04", "2017-11-05",
                                          "2017-11-06", "2017-11-11", "2017-11-12", "2017-11-18", "2017-11-19",
                                          "2017-11-25", "2017-11-26", "2017-12-02", "2017-12-03", "2017-12-09",
                                          "2017-12-10", "2017-12-16", "2017-12-17", "2017-12-23", "2017-12-24",
                                          "2017-12-30", "2017-12-31", "2018-01-01", "2018-01-02", "2018-01-03",
                                          "2018-01-04", "2018-01-05", "2018-01-06", "2018-01-07", "2018-01-08",
                                          "2018-01-13", "2018-01-14", "2018-01-20", "2018-01-21", "2018-01-27",
                                          "2018-01-28", "2018-02-03", "2018-02-04", "2018-02-10", "2018-02-11",
                                          "2018-02-17", "2018-02-18", "2018-02-23", "2018-02-24", "2018-02-25",
                                          "2018-03-03", "2018-03-04", "2018-03-08", "2018-03-09", "2018-03-10",
                                          "2018-03-11", "2018-03-17", "2018-03-18", "2018-03-24", "2018-03-25",
                                          "2018-03-31", "2018-04-01", "2018-04-07", "2018-04-08", "2018-04-14",
                                          "2018-04-15", "2018-04-21", "2018-04-22", "2018-04-29", "2018-04-30",
                                          "2018-05-01", "2018-05-02", "2018-05-05", "2018-05-06", "2018-05-09",
                                          "2018-05-12", "2018-05-13", "2018-05-19", "2018-05-20", "2018-05-26",
                                          "2018-05-27", "2018-06-02", "2018-06-03", "2018-06-10", "2018-06-11",
                                          "2018-06-12", "2018-06-16", "2018-06-17", "2018-06-23", "2018-06-24",
                                          "2018-06-30", "2018-07-01", "2018-07-07", "2018-07-08", "2018-07-14",
                                          "2018-07-15", "2018-07-21", "2018-07-22", "2018-07-28", "2018-07-29",
                                          "2018-08-04", "2018-08-05", "2018-08-11", "2018-08-12", "2018-08-18",
                                          "2018-08-19", "2018-08-25", "2018-08-26", "2018-09-01", "2018-09-02",
                                          "2018-09-08", "2018-09-09", "2018-09-15", "2018-09-16", "2018-09-22",
                                          "2018-09-23", "2018-09-29", "2018-09-30", "2018-10-06", "2018-10-07",
                                          "2018-10-13", "2018-10-14", "2018-10-20", "2018-10-21", "2018-10-27",
                                          "2018-10-28", "2018-11-03", "2018-11-04", "2018-11-05", "2018-11-10",
                                          "2018-11-11", "2018-11-17", "2018-11-18", "2018-11-24", "2018-11-25",
                                          "2018-12-01", "2018-12-02", "2018-12-08", "2018-12-09", "2018-12-15",
                                          "2018-12-16", "2018-12-22", "2018-12-23", "2018-12-30", "2018-12-31",
                                          "2019-01-01", "2019-01-02", "2019-01-03", "2019-01-04", "2019-01-05",
                                          "2019-01-06", "2019-01-07", "2019-01-08", "2019-01-12", "2019-01-13",
                                          "2019-01-19", "2019-01-20", "2019-01-26", "2019-01-27", "2019-02-02",
                                          "2019-02-03", "2019-02-09", "2019-02-10", "2019-02-16", "2019-02-17",
                                          "2019-02-23", "2019-02-24", "2019-03-02", "2019-03-03", "2019-03-08",
                                          "2019-03-09", "2019-03-10", "2019-03-16", "2019-03-17", "2019-03-23",
                                          "2019-03-24", "2019-03-30", "2019-03-31", "2019-04-06", "2019-04-07",
                                          "2019-04-13", "2019-04-14", "2019-04-20", "2019-04-21", "2019-04-27",
                                          "2019-04-28", "2019-05-01", "2019-05-02", "2019-05-03", "2019-05-04",
                                          "2019-05-05", "2019-05-09", "2019-05-10", "2019-05-11", "2019-05-12",
                                          "2019-05-18", "2019-05-19", "2019-05-25", "2019-05-26", "2019-06-01",
                                          "2019-06-02", "2019-06-08", "2019-06-09", "2019-06-12", "2019-06-15",
                                          "2019-06-16", "2019-06-22", "2019-06-23", "2019-06-29", "2019-06-30",
                                          "2019-07-06", "2019-07-07", "2019-07-13", "2019-07-14", "2019-07-20",
                                          "2019-07-21", "2019-07-27", "2019-07-28", "2019-08-03", "2019-08-04",
                                          "2019-08-10", "2019-08-11", "2019-08-17", "2019-08-18", "2019-08-24",
                                          "2019-08-25", "2019-08-31", "2019-09-01", "2019-09-07", "2019-09-08",
                                          "2019-09-14", "2019-09-15", "2019-09-21", "2019-09-22", "2019-09-28",
                                          "2019-09-29", "2019-10-05", "2019-10-06", "2019-10-12", "2019-10-13",
                                          "2019-10-19", "2019-10-20", "2019-10-26", "2019-10-27", "2019-11-02",
                                          "2019-11-03", "2019-11-04", "2019-11-09", "2019-11-10", "2019-11-16",
                                          "2019-11-17", "2019-11-23", "2019-11-24", "2019-11-30", "2019-12-01",
                                          "2019-12-07", "2019-12-08", "2019-12-14", "2019-12-15", "2019-12-21",
                                          "2019-12-22", "2019-12-28", "2019-12-29", "2020-01-01", "2020-01-02",
                                          "2020-01-03", "2020-01-04", "2020-01-05", "2020-01-06", "2020-01-07",
                                          "2020-01-08", "2020-01-11", "2020-01-12", "2020-01-18", "2020-01-19",
                                          "2020-01-25", "2020-01-26", "2020-02-01", "2020-02-02", "2020-02-08",
                                          "2020-02-09", "2020-02-15", "2020-02-16", "2020-02-22", "2020-02-23",
                                          "2020-02-24", "2020-02-29", "2020-03-01", "2020-03-07", "2020-03-08",
                                          "2020-03-09", "2020-03-14", "2020-03-15", "2020-03-21", "2020-03-22",
                                          "2020-03-28", "2020-03-29", "2020-04-04", "2020-04-05", "2020-04-11",
                                          "2020-04-12", "2020-04-18", "2020-04-19", "2020-04-25", "2020-04-26",
                                          "2020-05-01", "2020-05-02", "2020-05-03", "2020-05-04", "2020-05-05",
                                          "2020-05-09", "2020-05-10", "2020-05-11", "2020-05-16", "2020-05-17",
                                          "2020-05-23", "2020-05-24", "2020-05-30", "2020-05-31", "2020-06-06",
                                          "2020-06-07", "2020-06-12", "2020-06-13", "2020-06-14", "2020-06-20",
                                          "2020-06-21", "2020-06-27", "2020-06-28", "2020-07-04", "2020-07-05",
                                          "2020-07-11", "2020-07-12", "2020-07-18", "2020-07-19", "2020-07-25",
                                          "2020-07-26", "2020-08-01", "2020-08-02", "2020-08-08", "2020-08-09",
                                          "2020-08-15", "2020-08-16", "2020-08-22", "2020-08-23", "2020-08-29",
                                          "2020-08-30", "2020-09-05", "2020-09-06", "2020-09-12", "2020-09-13",
                                          "2020-09-19", "2020-09-20", "2020-09-26", "2020-09-27", "2020-10-03",
                                          "2020-10-04", "2020-10-10", "2020-10-11", "2020-10-17", "2020-10-18",
                                          "2020-10-24", "2020-10-25", "2020-10-31", "2020-11-01", "2020-11-04",
                                          "2020-11-07", "2020-11-08", "2020-11-14", "2020-11-15", "2020-11-21",
                                          "2020-11-22", "2020-11-28", "2020-11-29", "2020-12-05", "2020-12-06",
                                          "2020-12-12", "2020-12-13", "2020-12-19", "2020-12-20", "2020-12-26",
                                          "2020-12-27", "2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04",
                                          "2021-01-05", "2021-01-06", "2021-01-07", "2021-01-08", "2021-01-09",
                                          "2021-01-10", "2021-01-16", "2021-01-17", "2021-01-23", "2021-01-24",
                                          "2021-01-30", "2021-01-31", "2021-02-06", "2021-02-07", "2021-02-13",
                                          "2021-02-14", "2021-02-21", "2021-02-22", "2021-02-23", "2021-02-27",
                                          "2021-02-28", "2021-03-06", "2021-03-07", "2021-03-08", "2021-03-13",
                                          "2021-03-14", "2021-03-20", "2021-03-21", "2021-03-27", "2021-03-28",
                                          "2021-04-03", "2021-04-04", "2021-04-10", "2021-04-11", "2021-04-17",
                                          "2021-04-18", "2021-04-24", "2021-04-25", "2021-05-01", "2021-05-02",
                                          "2021-05-03", "2021-05-08", "2021-05-09", "2021-05-10", "2021-05-15",
                                          "2021-05-16", "2021-05-22", "2021-05-23", "2021-05-29", "2021-05-30",
                                          "2021-06-05", "2021-06-06", "2021-06-12", "2021-06-13", "2021-06-14",
                                          "2021-06-19", "2021-06-20", "2021-06-26", "2021-06-27", "2021-07-03",
                                          "2021-07-04", "2021-07-10", "2021-07-11", "2021-07-17", "2021-07-18",
                                          "2021-07-24", "2021-07-25", "2021-07-31", "2021-08-01", "2021-08-07",
                                          "2021-08-08", "2021-08-14", "2021-08-15", "2021-08-21", "2021-08-22",
                                          "2021-08-28", "2021-08-29", "2021-09-04", "2021-09-05", "2021-09-11",
                                          "2021-09-12", "2021-09-18", "2021-09-19", "2021-09-25", "2021-09-26",
                                          "2021-10-02", "2021-10-03", "2021-10-09", "2021-10-10", "2021-10-16",
                                          "2021-10-17", "2021-10-23", "2021-10-24", "2021-10-30", "2021-10-31",
                                          "2021-11-04", "2021-11-05", "2021-11-06", "2021-11-07", "2021-11-13",
                                          "2021-11-14", "2021-11-20", "2021-11-21", "2021-11-27", "2021-11-28",
                                          "2021-12-04", "2021-12-05", "2021-12-11", "2021-12-12", "2021-12-18",
                                          "2021-12-19", "2021-12-25", "2021-12-26", "2021-12-31", "2022-01-01",
                                          "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05", "2022-01-06",
                                          "2022-01-07", "2022-01-08", "2022-01-09", "2022-01-15", "2022-01-16",
                                          "2022-01-22", "2022-01-23", "2022-01-29", "2022-01-30", "2022-02-05",
                                          "2022-02-06", "2022-02-12", "2022-02-13", "2022-02-19", "2022-02-20",
                                          "2022-02-23", "2022-02-26", "2022-02-27", "2022-03-06", "2022-03-07",
                                          "2022-03-08", "2022-03-12", "2022-03-13", "2022-03-19", "2022-03-20",
                                          "2022-03-26", "2022-03-27", "2022-04-02", "2022-04-03", "2022-04-09",
                                          "2022-04-10", "2022-04-16", "2022-04-17", "2022-04-23", "2022-04-24",
                                          "2022-04-30", "2022-05-01", "2022-05-02", "2022-05-03", "2022-05-07",
                                          "2022-05-08", "2022-05-09", "2022-05-10", "2022-05-14", "2022-05-15",
                                          "2022-05-21", "2022-05-22", "2022-05-28", "2022-05-29", "2022-06-04",
                                          "2022-06-05", "2022-06-11", "2022-06-12", "2022-06-13", "2022-06-18",
                                          "2022-06-19", "2022-06-25", "2022-06-26", "2022-07-02", "2022-07-03",
                                          "2022-07-09", "2022-07-10", "2022-07-16", "2022-07-17", "2022-07-23",
                                          "2022-07-24", "2022-07-30", "2022-07-31", "2022-08-06", "2022-08-07",
                                          "2022-08-13", "2022-08-14", "2022-08-20", "2022-08-21", "2022-08-27",
                                          "2022-08-28", "2022-09-03", "2022-09-04", "2022-09-10", "2022-09-11",
                                          "2022-09-17", "2022-09-18", "2022-09-24", "2022-09-25", "2022-10-01",
                                          "2022-10-02", "2022-10-08", "2022-10-09", "2022-10-15", "2022-10-16",
                                          "2022-10-22", "2022-10-23", "2022-10-29", "2022-10-30", "2022-11-04",
                                          "2022-11-05", "2022-11-06", "2022-11-12", "2022-11-13", "2022-11-19",
                                          "2022-11-20", "2022-11-26", "2022-11-27", "2022-12-03", "2022-12-04",
                                          "2022-12-10", "2022-12-11", "2022-12-17", "2022-12-18", "2022-12-24",
                                          "2022-12-25", "2022-12-31", "2023-01-01", "2023-01-02", "2023-01-03",
                                          "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08",
                                          "2023-01-14", "2023-01-15", "2023-01-21", "2023-01-22", "2023-01-28",
                                          "2023-01-29", "2023-02-04", "2023-02-05", "2023-02-11", "2023-02-12",
                                          "2023-02-18", "2023-02-19", "2023-02-23", "2023-02-24", "2023-02-25",
                                          "2023-02-26", "2023-03-04", "2023-03-05", "2023-03-08", "2023-03-11",
                                          "2023-03-12", "2023-03-18", "2023-03-19", "2023-03-25", "2023-03-26",
                                          "2023-04-01", "2023-04-02", "2023-04-08", "2023-04-09", "2023-04-15",
                                          "2023-04-16", "2023-04-22", "2023-04-23", "2023-04-29", "2023-04-30",
                                          "2023-05-01", "2023-05-06", "2023-05-07", "2023-05-08", "2023-05-09",
                                          "2023-05-13", "2023-05-14", "2023-05-20", "2023-05-21", "2023-05-27",
                                          "2023-05-28", "2023-06-03", "2023-06-04", "2023-06-10", "2023-06-11",
                                          "2023-06-12", "2023-06-17", "2023-06-18", "2023-06-24", "2023-06-25",
                                          "2023-07-01", "2023-07-02", "2023-07-08", "2023-07-09", "2023-07-15",
                                          "2023-07-16", "2023-07-22", "2023-07-23", "2023-07-29", "2023-07-30",
                                          "2023-08-05", "2023-08-06", "2023-08-12", "2023-08-13", "2023-08-19",
                                          "2023-08-20", "2023-08-26", "2023-08-27", "2023-09-02", "2023-09-03",
                                          "2023-09-09", "2023-09-10", "2023-09-16", "2023-09-17", "2023-09-23",
                                          "2023-09-24", "2023-09-30", "2023-10-01", "2023-10-07", "2023-10-08",
                                          "2023-10-14", "2023-10-15", "2023-10-21", "2023-10-22", "2023-10-28",
                                          "2023-10-29", "2023-11-04", "2023-11-05", "2023-11-06", "2023-11-11",
                                          "2023-11-12", "2023-11-18", "2023-11-19", "2023-11-25", "2023-11-26",
                                          "2023-12-02", "2023-12-03", "2023-12-09", "2023-12-10", "2023-12-16",
                                          "2023-12-17", "2023-12-23", "2023-12-24", "2023-12-30", "2023-12-31"])
        print(delta - int(dat))
        self.screen.ids.date.text = "Результат (дни): " + str(delta - int(dat))
        self.screen.ids.months.text = str(delta - int(dat))

        print("button2 pressed")
        star = self.screen.ids.star.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        inters = self.screen.ids.inters.text
        print(star + " " + loan + " " + months + " " + interest + " " + inters)
        # convert to date object, float, and so on
        star = float(star)
        loan = float(loan)
        months = float(months)
        interest = float(interest)
        percent = loan / 12
        print(percent)
        b = months / percent
        print(b)
        r = round(b)
        print(r)
        if r >= 11:
            z = star - interest
            x = math.ceil(z)
            print(x)
            self.screen.ids.inters.text = "Результат (дни): " + str(x)
        elif r < 11:
            e = star / 12 * r - interest
            q = math.ceil(e)
            print(q)
            self.screen.ids.inters.text = "Результат (дни): " + str(q)

        pass


DopOtpuskCalculatorApp().run()
