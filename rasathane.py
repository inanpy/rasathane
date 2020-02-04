from requests import request
from lxml import html
import time

def pull_data():
    res = request('GET', 'http://www.koeri.boun.edu.tr/scripts/lst4.asp')
    html_data = html.fromstring(res.content)
    stores = html_data.xpath('//pre/text()')
    data = stores[0].splitlines()
    for item in data:
        try:
            print clear_data(item)
        except:
            continue    

def clear_data(line):
    split_data = line.split()
    siddet = split_data[6] if split_data[7] == '-.-' else split_data[7]
    lokasyon = u'{}-{}'.format(split_data[-3], split_data[-2])
    data = {
          'tarih': split_data[0],
          'saat': split_data[1],
          'derinlik': split_data[4],
          'siddet':  siddet,
          'lokasyon': lokasyon,
          'tip': split_data[-1]
    }
    return data
