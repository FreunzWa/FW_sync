#!/usr/bin/python3
import requests
from datetime import datetime
import pyexcel_ods
import sys

import smtplib
import email



mailingList = []

urlDict = dict()
urlDict['ULD'] = ('itemprop="price">', "https://www.uniqlo.com/au/store/men-ultra-light-down-jacket-4193800003.html")
urlDict['Milk'] = ('"price":', "https://www.woolworths.com.au/shop/productdetails/405010/pauls-farmhouse-gold-milk")
urlDict['Tuna'] = ('"price":', "https://www.woolworths.com.au/shop/productdetails/19736/john-west-tuna-light-in-springwater")
urlDict['TwiningsEnglishBreakfast'] = ('"price":', "https://www.woolworths.com.au/shop/productdetails/829281/twinings-extra-strong-english-breakfast-tea-bags")
urlDict['BakerFlour'] = ('"price":', "https://www.woolworths.com.au/shop/productdetails/91304/defiance-white-baker-s-flour")


def send_notification(message_text):
    msg = email.message.EmailMessage()
    msg.set_content(message_text)
    msg['Subject'] = "FW Price update"
    msg['From'] = "chessmushi@gmail.com"
    msg['To'] = "joshaughness@student.unimelb.edu.au"


    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('chessmushi@gmail.com','trophies1')
    server.send_message(msg)
    server.quit()




def get_specific_price(item_name):
    """get the price of a specific article"""
    price=''
    """
    if item_name == "ULD":
        url = "https://www.uniqlo.com/au/store/men-ultra-light-down-jacket-4193800003.html"
        search_tag = 'itemprop="price">'
    elif item_name == "Milk":
        url = "https://www.woolworths.com.au/shop/productdetails/405010/pauls-farmhouse-gold-milk"
        search_tag = 
    elif item_name == "Tuna":
        url = "https://www.woolworths.com.au/shop/productdetails/19736/john-west-tuna-light-in-springwater"
        search_tag = '"price":'
    elif item_name == "TwiningsEnglishBreakfast":
        url = "https://www.woolworths.com.au/shop/productdetails/829281/twinings-extra-strong-english-breakfast-tea-bags"
        search_tag = '"price":'
    elif item_name == "BakerFlour":
        url = "https://www.woolworths.com.au/shop/productdetails/91304/defiance-white-baker-s-flour"
        search_tag = '"price":'
    elif item_name == "TwiningsPeppermint":
        url = "https://www.woolworths.com.au/shop/productdetails/888487/twinings-pure-peppermint-tea-bags"
        search_tag = '"price":'

    """
    search_tag, url = urlDict[item_name]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #create a response object from url
    r = requests.get(url, headers=headers)
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
    """return prices for each article"""
    price_row = []
    price_row.append(datetime.now().ctime()) 
    for article in book[0][1:]:
        price_row.append(get_specific_price(article))

    return price_row

def get_analytics(article):
    """run analytics on a specific article"""
    

if __name__ == "__main__":


    #set the path to the data file
    PATH = '/home/sarsfield/Documents/sync/code/'

    #log that this program was run
    f=open(PATH+"price_getter_log.txt", "a+")
    f.write("Program run at {d} with arguments: {a}".format(d=datetime.now().ctime(), a=sys.argv.__repr__()))

    #load the data file
    data_file = PATH+'uniqlo_prices.ods'
    articles = dict()
    book = pyexcel_ods.read_data(data_file)['prices']
    #creates a list of all article names to be updated.
    article_names = book[0][1:]
    print(article_names)

    #append all the history of pulled prices for each item

    date_list = []      
    if len(book[1:])>=1:
        for row in book[1:]:
            date_list.append(row[0])
            most_recent_date = datetime.strptime(row[0], '%a %b %d %H:%M:%S %Y')
    #if a price has not been recorded for today, the price is pulled and appended to the boook
        if most_recent_date.day != datetime.now().day:
            book.append(get_price_list())   
    else:
        book.append(get_price_list())   

    today_prices = book[-1:][0][1:]
    yesterday_prices = book[-2:][0][1:]

    for ind, price in enumerate(today_prices):
        try:
            if float(price) < float(yesterday_prices[ind]):
                msg = "The price of {item} has decreased from ${y} to ${t}! \nItem URL: {url}".format(item=book[0][ind+1], y=float(yesterday_prices[ind]), t=float(price), url=urlDict[book[0][ind+1]][1])
                print(msg)
                send_notification(msg)
        except ValueError:
            #some of teh cells are empty and only contain '' as the value, 
            #handle these values.
            pass
        except IndexError:
            #some of the price lists may be of different lengths, handle this
            pass


    #save the new price data to the data file.
    pyexcel_ods.save_data(data_file,dict(prices=book))
                          



