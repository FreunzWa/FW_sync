#!/usr/bin/python3
import requests
from datetime import datetime
import pyexcel_ods
import sys


def get_specific_price():
    price=''
    url = "https://www.uniqlo.com/au/store/men-ultra-light-down-jacket-4193800003.html"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #create a response object from url
    r = requests.get(url, headers=headers)
    search_tag = 'itemprop="price">'
    pos = (r.text.find(search_tag))+len(search_tag)
    query_char = '0'
    count = 0
    while query_char in '.0123456789':
        count+=1
        query_char = r.text[pos+(count-1)]
        price = price + query_char
    print("Pulled price: $",price[:-1])
    return price[:-1]

def get_price_list(date=0):
    price_row = []
    price_row.append(datetime.now().ctime())
    for article in book[0][1:]:
        price_row.append(get_specific_price())

    return price_row



if __name__ == "__main__":
    PATH = '/home/sarsfield/Documents/sync/code/'
    f=open(PATH+"price_getter_log.txt", "a+")
    f.write("Program run at {d} with arguments: {a}".format(d=datetime.now().ctime(), a=sys.argv.__repr__()))

    data_file = PATH+'uniqlo_prices.ods'
    article_names = ['ULD']
    articles = dict()
    book = pyexcel_ods.read_data(data_file)['prices']
    print(book)
    date_list = []


    if len(book[1:])>=1:
        for row in book[1:]:
            date_list.append(row[0])
            print(date_list)
            most_recent_date = datetime.strptime(row[0], '%a %b %d %H:%M:%S %Y')


        if most_recent_date.day != datetime.now().day:
            book.append(get_price_list())   
        else:
            raise Exception("Already updated today")
    else:
        book.append(get_price_list())   


    pyexcel_ods.save_data(data_file,dict(prices=book))
                          


