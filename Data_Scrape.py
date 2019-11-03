from bs4 import BeautifulSoup
import requests
# importing the module
import tweepy
import time

url = "https://money.cnn.com/data/commodities/"

# personal details
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    # content = urllib3.urlopen(url).read()
    content = requests.get(url)
    print(content.text)
    soup = BeautifulSoup(content.text)
    # print(soup.prettify())

    print(soup.title.string)

    # print(soup.find_all('a'))
    links = soup.find_all(class_='cnncol3')  # list of scraped prices
    # print(links)
    # for link in links:
    #     print(link.text)
    comm_one = " - Light Crude"
    a = (links[1].text + comm_one)
    print(a)
    links = soup.find_all(class_='cnncol3')
    comm_two = " - Natural Gas"
    b = (links[3].text + comm_two)
    print(b)
    links = soup.find_all(class_='cnncol3')
    comm_three = " - Brent Crude"
    c = (links[5].text + comm_three)
    print(c)
    links = soup.find_all(class_='cnncol3')
    comm_four = " - Gold"
    d = links[7].text + comm_four
    print(d)
    api.update_status(status=(a, b, c, d))
    print('tweeted')
    time.sleep(180)
