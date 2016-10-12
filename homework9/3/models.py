# -*- coding: utf-8 -*-

from datetime import date

from app import db

__author__ = 'Anton Vodopyanov'


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.String(10), unique=True, nullable=False)
    sex = db.Column(db.String(6), default='male', nullable=False)
    name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, default=date.today(), nullable=False)
    age = db.Column(db.Integer, default=None)
    faculty = db.Column(db.String(30), nullable=False)

    def __init__(self, studentID=None, sex='', name='', last_name='', date_of_birth=None, age=None, faculty=''):
        self.studentID = studentID
        self.sex = sex
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = (date.today() - date_of_birth).days // 365
        self.faculty = faculty







