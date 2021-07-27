import datetime
import os
import glob
import functools
import setting

chart_types = ['Open', 'Close', 'High', 'Low']


def validate_date(date_text, name):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        raise ValueError(f'Incorrect {name} data format, should be YYYY-MM-DD')


def validate_chart_type(type):
    if type not in chart_types:
        chart_types_str = functools.reduce(lambda a, b: str(a) + ', ' + str(b), chart_types)
        raise ValueError(f'Incorrect chart type format, should be {chart_types_str}')
    else:
        return type


def clean_static():
    files = glob.glob(setting.static + '/*')
    for f in files:
        os.remove(f)
