#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

__author__ = 'Anton Vodopyanov'


class MyForm(forms.Form):
    set_date = forms.DateField(label='Set data')


