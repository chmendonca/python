# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:39:03 2020

@author: Cassio
"""

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()