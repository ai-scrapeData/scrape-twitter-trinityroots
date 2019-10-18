import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import datetime
from datetime import datetime

import requests

import pymongo
from pymongo import MongoClient
uri = "mongodb://adminuser:admin1234@ds227199.mlab.com:27199/gcp-database?retryWrites=false"
client = MongoClient(uri)
db = client["gcp-database"]
collections = db['comment']
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        # driver.get("https://twitter.com/trinityroots?lang=en")
        # driver.get("https://twitter.com/Odoo/status/1047510943461265409")
        driver.get("https://twitter.com/trinityroots?lang=en")
        print('-------------------------------------------------------------------------------------------------------------------------------')
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            time.sleep(5)
            lastCount = lenOfPage
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        link_all_post_admin = driver.find_elements_by_class_name("tweet-timestamp.js-permalink.js-nav.js-tooltip")
        list_page_status_all = []
        for i in range(len(link_all_post_admin)):
            list_page_status_all.append(link_all_post_admin[i].get_property("href"))
        print(list_page_status_all)
        print('-------------------------------------------------------------------------------------------------------------------------------')
        for i in range(len(list_page_status_all)):
            link_author = driver.get(list_page_status_all[i])
            print('link_author',list_page_status_all[i])

            author_name = driver.find_elements_by_class_name("fullname.show-popup-with-id.u-textTruncate")
            author_description = driver.find_elements_by_class_name("TweetTextSize")
            author_link = driver.find_elements_by_class_name("account-group.js-account-group.js-action-profile.js-user-profile-link.js-nav")
            admin_time = driver.find_elements_by_class_name("metadata")[0].text
            link_all_author_post = driver.find_elements_by_class_name("tweet-timestamp.js-permalink.js-nav.js-tooltip")
            user_time = driver.find_elements_by_class_name("_timestamp.js-short-timestamp")
            all_post_retweet_like = driver.find_elements_by_class_name("ProfileTweet-actionList.js-actions")
            for i in range(len(author_name)):
                try:
                    # print('----------------------------------------------------------------------------------')
                    print('author_name',author_name[i].text)
                    print('author_description',author_description[i].text)
                    print('author_link',author_link[i].get_property("href"))
                    print('author_link_post',link_all_author_post[i].get_property("href"))
                    author_time_stamp = int(user_time[i].get_attribute("data-time"))
                    author_time = datetime.fromtimestamp(author_time_stamp)
                    print('author_time_stamp',author_time_stamp)
                    print('author_time',author_time)
                    all_post = all_post_retweet_like[i].text
                    all_post_duplitcate = " ".join(all_post.split())
                    print(all_post_duplitcate)
                    print(all_post_duplitcate.split(' '))
                    print(len(all_post_duplitcate.split(' ')))
                    if len(all_post_duplitcate.split(' ')) == 6 and all_post_duplitcate.split(' ')[0] == 'Reply' and all_post_duplitcate.split(' ')[2] == 'Retweet' and all_post_duplitcate.split(' ')[4] == 'Like':
                        reply = all_post_duplitcate.split(' ')[1]
                        retweet = all_post_duplitcate.split(' ')[3]
                        like = all_post_duplitcate.split(' ')[5]
                    elif len(all_post_duplitcate.split(' ')) == 5 and all_post_duplitcate.split(' ')[0] == 'Reply' and all_post_duplitcate.split(' ')[3] == 'Like' and all_post_duplitcate.split(' ')[1] != 'Retweet':
                        reply = all_post_duplitcate.split(' ')[1]
                        retweet = "0"
                        like = all_post_duplitcate.split(' ')[4]
                    elif len(all_post_duplitcate.split(' ')) == 5 and all_post_duplitcate.split(' ')[0] == 'Reply' and all_post_duplitcate.split(' ')[2] == 'Retweet':
                        reply = all_post_duplitcate.split(' ')[1]
                        retweet = all_post_duplitcate.split(' ')[3]
                        like = "0"
                    elif len(all_post_duplitcate.split(' ')) == 5 and all_post_duplitcate.split(' ')[1] == 'Retweet' and all_post_duplitcate.split(' ')[3] == 'Like':
                        reply = "0"
                        retweet = all_post_duplitcate.split(' ')[2]
                        like = all_post_duplitcate.split(' ')[4]
                    elif len(all_post_duplitcate.split(' ')) == 4 and all_post_duplitcate.split(' ')[2] == 'Like':
                        reply = "0"
                        retweet = "0"
                        like = all_post_duplitcate.split(' ')[3]
                    elif len(all_post_duplitcate.split(' ')) == 4 and all_post_duplitcate.split(' ')[1] == 'Retweet':
                        reply = "0"
                        retweet = all_post_duplitcate.split(' ')[2]
                        like = "0"
                    elif len(all_post_duplitcate.split(' ')) == 4 and all_post_duplitcate.split(' ')[0] == 'Reply':
                        reply = all_post_duplitcate.split(' ')[1]
                        retweet = "0"
                        like = "0"
                    else:
                        reply = "0"
                        retweet = "0"
                        like = "0"
                    print('reply',reply)
                    print('retweet',retweet)
                    print('like',like)

                    print('----------------------------------------------------------------------------------')
                    # print('---------------------------------------------------sentiment analysic----------------------------------------------------------------------------')
                    url = "https://api.aiforthai.in.th/ssense"
                    text = " ".join(author_description[i].text.split())
                    params = {'text':text}
                    headers = {'Apikey': "h1Owx8wOh8UMX7fkwBESWGm2FMT57t0n"}
                    response = requests.get(url, headers=headers, params=params)
                    score = response.json()['sentiment']['score']
                    polarity_neg = response.json()['sentiment']['polarity-neg']
                    if polarity_neg == True:
                        word = 'bad'
                    elif polarity_neg == False:
                        word = 'good'
                    print(word)
                    # print('-------------------------------------------------------------------------------------------------------------------------------------------------')
                    dict_comment = {
                        'author_name':author_name[i].text,
                        'author_description':" ".join(author_description[i].text.split()),
                        'author_link_profile':author_link[i].get_property("href"),
                        'author_link_post':link_all_author_post[i].get_property("href"),
                        'author_time_stamp':author_time_stamp,
                        'author_time_string':author_time,
                        'reply':reply,
                        'retweet':retweet,
                        'like':like,
                        "time_day":f'{author_time}'.split(" ")[0].split('-')[2],
                        "time_month":f'{author_time}'.split(" ")[0].split('-')[1],
                        "time_year":f'{author_time}'.split(" ")[0].split('-')[0],
                        "time_hour":f'{author_time}'.split(" ")[1].split(':')[0],
                        "time_minute":f'{author_time}'.split(" ")[1].split(':')[1],
                        "time_second":f'{author_time}'.split(" ")[1].split(':')[2],
                        'word_feel':word
                    }
                    allData = {'MacthID':f'{author_name[i].text}_{" ".join(author_description[i].text.split())}_{author_time_stamp}','api': dict_comment}
                    query = {"MacthID":f'{author_name[i].text}_{" ".join(author_description[i].text.split())}_{author_time_stamp}'}
                    result = collections.find(query, {'_id': False})
                    print('result_count:', result.count())
                    if result.count() == 0:
                        print('Not found. inserting')
                        print('All Data', allData)
                        collections.insert_one(allData)
                    else:
                        collections.replace_one(query, allData)
                        print('Updated completed!')
                except:
                    print('error')
    # def tearDown(self):
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()