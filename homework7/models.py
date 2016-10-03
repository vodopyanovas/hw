# -*- coding: utf-8 -*-

import datetime
import json

__author__ = 'sobolevn'
__author__ = 'Anton Vodopyanov'


class Storage(object):
    items = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
        return cls._obj


class BlogPostModel(object):
    def __init__(self, form_data):
        self.title = form_data['title']
        self.text = form_data['text']
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.author = form_data['author']
        self.load_list = []

    def save(self):
        with open('blog.json', 'w', encoding = 'utf-8') as file:
            forms_dict = {
               'title': self.title,
               'text': self.text,
               'time_stamp': self.time_stamp,
               'author': self.author
            }

            self.load_list.append(forms_dict)
            json.dump(self.load_list, file)

    def load_file(self):
        try:
            with open('blog.json', 'r') as file:
                load = json.load(file)
                self.load_list.extend(load)

                for index in self.load_list:
                    self.title = index.get('title')
                    self.text = index.get('text')
                    self.author = index.get('author')
                    self.time_stamp = index.get('time_stamp')
        except:
            with open('blog.json', 'w') as file:
                print('The new file has been created!\n')