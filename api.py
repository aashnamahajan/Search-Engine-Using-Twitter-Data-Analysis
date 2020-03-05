
# coding: utf-8

# In[ ]:


from random import shuffle

import pytz
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import request
import json
import urllib.request
from flask_cors import CORS
import urllib
from datetime import datetime, timedelta
import requests


app = Flask(__name__)
api = Api(app)
CORS(app)
# def getNews(docs):
#
#     verified = [405427035,42736936,30354991,2410755840,21059255,216776631,33374761,762402774260875265,18839785,56304605,
#                 1288175774,342863309,357606935,128372940,1324334436,24705126]
#     poi_list = {}
#     returnobj = []
#     for doc in docs:
#         if "user.id" in doc:
#
#             id = doc["user.id"]
#             id = id[0]
#
#             if id in verified:
#                 # print(True)
#                 # print(doc["tweet_date"])
#                 username = doc["user.name"]
#                 username = username[0]
#                 tweetdte = doc["tweet_date"]
#                 if username in poi_list:
#                     if len(poi_list[username]) <=4:
#                         poi_list[username] = poi_list[username].append(datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ'))
#                 else:
#                     poi_list[username] = [datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ')]
#                 #print(poi_list)
#
#
#
#
#     for name,time in poi_list.items():
#         q = urllib.parse.quote(name)
#         key = '5cf6b44cf02277e94b89770649fdd578'
#         json_obj = {}
#         mindate = time - timedelta(days=1)
#         maxdate = time + timedelta(days=1)
#         mindate = mindate.strftime('%Y-%m-%d')
#         maxdate = maxdate.strftime('%Y-%m-%d')
#         url = 'https://gnews.io/api/v3/search?token={}&q={}&maxdate={}'.format(key, q,maxdate)
#         print(url)
#         response = requests.get(url)
#         res = response.json()
#         if response.status_code ==200:
#             json_obj["key"] = name
#             json_obj["value"] = res["articles"]
#             returnobj.append(json_obj)
#
#     return returnobj

def Getmaxflows(flows):
    maks = max(flows, key=lambda k: len(flows[k]))
    return len(flows[maks])


def getNews(docs,query):
    poi_country = {}
    poi_country["Vasundhara Raje"] = ["India",1288175774]
    poi_country["Shashi Tharoor"] = ["India", 24705126]
    poi_country["Rajdeep Sardesai"] = ["India", 56304605]
    poi_country["Sachin Pilot"] = ["India", 2410755840]
    poi_country["Piyush Goyal"] = ["India", 1324334436]
    poi_country["Narendra Modi"] = ["India", 18839785]
    poi_country["Arvind Kejriwal"] = ["India", 405427035]
    poi_country["Beto O'Rourke"] = ["USA", 342863309]
    poi_country["Joe Biden"] = ["USA", 939091]
    poi_country["Elizabeth Warren"] = ["USA", 357606935]
    poi_country["Bernie Sanders"] = ["USA", 216776631]
    poi_country["Ted Lieu"] = ["USA", 21059255]
    poi_country["Ciro Gomes"] = ["Brazil", 33374761]
    poi_country["Carlos Bolsonaro"] = ["Brazil", 68712576]
    poi_country["Flavio Bolsonaro"] = ["Brazil", 40053694]
    poi_country["DelegadoFrancischini"] = ["Brazil", 42736936]
    poi_country["Guilherme Boulos"] = ["Brazil", 762402774260875265]
    poi_country["Jair M. Bolsonaro"] = ["Brazil", 128372940]
    poi_country["Kamala Harris"] = ["USA",30354991]
    poi_country["Cory Booker"] = ["USA",15808765]







    verified = [405427035,42736936,30354991,2410755840,21059255,216776631,33374761,762402774260875265,18839785,56304605,
                1288175774,342863309,357606935,128372940,1324334436,24705126,68712576]
    poi_list = {}
    returnobj = []
    json_obj = {}
    json_obj["articles"] = []
    for doc in docs:
        if "user.id" in doc:

            id = doc["user.id"]
            id = id[0]

            if id in verified:
                # print(True)
                # print(doc["tweet_date"])
                #if "user.name" in doc:
                username = doc["user.name"]
                username = username[0]
                tweetdte = doc["tweet_date"]
                tweet_dte_datetime = datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ')

                temp = username + "~~~" + str(datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ'))


                #poi_list.append(temp)
                if username in poi_list:
                    if tweet_dte_datetime > poi_list[username][1]:
                        poi_list[username][1] = tweet_dte_datetime#datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ')
                    elif tweet_dte_datetime < poi_list[username][0]:
                        poi_list[username][0] = tweet_dte_datetime#datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ')
                    # if len(poi_list[username]) <=4:
                    #     poi_list[username].append(datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ'))
                else:
                    poi_list[username] = [datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ'),datetime.strptime(tweetdte,'%Y-%m-%dT%H:%M:%SZ')]

                #print(poi_list)


    print(poi_list)
    #l = Getmaxflows(poi_list)

    #key = '5cf6b44cf02277e94b89770649fdd578' #prithvi
    #key = '9ea64eee9b3e8452773935328dc1246f' #aashna
    #key = 'fc6320dbc1989f65643e319571a5f601' #priya
    #key = 'b838261a008d46ba88b53f9afc0a4200' #navpinder
    #key = 'e6f9e1dbbabdc89833b4b74bf137bb5f' #prithvi
    #key = 'f850535dc10ade556903962fe9c36d1c'  # prithvi
    key = '579caeeb80e563dd950a37beb7bc6a1b' #prithvi
    #key = '9936216a88585a652caaf98eeb7f1ab5' #prithvi

    # count = 0
    for name, value in poi_list.items():
        # spl = poi.split("~~~")
        mindate = value[0]
        maxdate = value[1]
        mindate = mindate - timedelta(days=2)
        maxdate = maxdate + timedelta(days=2)
        mindate = mindate.strftime('%Y-%m-%d')
        maxdate = maxdate.strftime('%Y-%m-%d')

        #time = datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
        q = urllib.parse.quote(name)
        q = q + "%20" +query
        # -- commented for limiting api counts starts here ---
        url = 'https://gnews.io/api/v3/search?token={}&q={}&maxdate={}&mindate={}'.format(key,q,maxdate, mindate)
        response = requests.get(url)
        print(url)
        res = response.json()
        if response.status_code == 200:
            for article in res["articles"]:
                if name in poi_country:
                    val = poi_country[name]
                    country = val[0]
                    poiId = val[1]
                    article["country"] = country
                    #article["language"]= lang
                    article["poiId"] = poiId

                json_obj["articles"].append(article)
        # --- ends here ---
    #     datelimit = datetime.strptime('2019-07-15 12:00:00','%Y-%m-%d %H:%M:%S')
    #     if time>datelimit:
    #         mindate = time - timedelta(days=1)
    #         maxdate = time + timedelta(days=2)
    #         mindate = mindate.strftime('%Y-%m-%d')
    #         maxdate = maxdate.strftime('%Y-%m-%d')
    #         q = urllib.parse.quote(name)
    #         q  = q + "%20" + query
    #         print(q)
    #         url = 'https://gnews.io/api/v3/search?token={}&q={}&maxdate={}'.format(key, q, maxdate)
    #
    #         if len(json_obj["articles"]) <30 and count<15:
    #             print(url)
    #             response = requests.get(url)
    #             count +=1
    #             res = response.json()
    #             # print(response.status_code)
    #             # print(res)
    #             if response.status_code == 200:
    #                 for article in res["articles"]:
    #                     json_obj["articles"].append(article)


    # j = 0
    # while(j<l):
    #     i=0
    #     while(i<len(poi_list)):
    #         name = list(poi_list)[i]
    #         if j<len(poi_list[name]):
    #             time = poi_list[name][j]
    #             mindate = time - timedelta(days=1)
    #             maxdate = time + timedelta(days=1)
    #             mindate = mindate.strftime('%Y-%m-%d')
    #             maxdate = maxdate.strftime('%Y-%m-%d')
    #             q = urllib.parse.quote(name)
    #             url = 'https://gnews.io/api/v3/search?token={}&q={}&maxdate={}'.format(key, q, maxdate)
    #             print(url)
    #             response = requests.get(url)
    #             res = response.json()
    #             if response.status_code == 200:
    #                 for article in res["articles"]:
    #                     json_obj["articles"].append(article)
    #         i+=1
    #     j+=1
    #shuffle(json_obj["articles"])
    # print(json_obj["articles"][0])
    return json_obj





class GetData(Resource):
    def post(self):
        docs_return = []
        facet_country= {}
        facet_hashtags= {}
        input_json = request.get_json()
        query = input_json['query']
        query = urllib.parse.quote(query)
        url_query = "translation:" + "%28"+query+"%29"+"%20tweet_text:" + "%28" + query+ "%29"
        inurl = 'http://ec2-18-224-141-207.us-east-2.compute.amazonaws.com:8983/solr/IRP4/select?defType=edismax&q='+ query +'&qf=tweet_text%20translation&facet=on&facet.field=country&facet.field=hashtags&f.hashtags.facet.limit=10&indent=true&rows=30000&wt=json&fl=id%2Ccountry%2Ccreated_at%2Csentiment%2Ctweet_text%2Ctweet_lang%2Ctweet_date%2Cverified%2Cuser.screen_name%2Clang%2Cpoi_id%2Cpoi_name%2Cuser.profile_image_url_https%2Cuser.name%2Ctopic%2Chashtags%2Cuser.id'


        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        facets = json.loads(data.decode('utf-8'))['facet_counts']['facet_fields']


        if "country" in facets:
            country_count = facets["country"]
            i = 0
            while(i<len(country_count)-1):
                facet_country[country_count[i]] = country_count[i+1]
                i+=2
        if "hashtags" in facets:
            j = 0
            hashtag_count = facets["hashtags"]
            while(j<len(hashtag_count)-1):
                facet_hashtags[hashtag_count[j]] = hashtag_count[j+1]
                j+=2






        # print(facets)
        # print(facet_hashtags)

        #print(type(docs))
        print("Docs Retrived: ",len(docs))
        docs_return.append(docs)
        news = getNews(docs,query)
        if len(news) >0:

            docs_return.append(news)
        else:
            docs_return.append({"articles":[]})

        #print(docs)
        #docs_return.append(facet_country)
        docs_return.append(facet_hashtags)

        return docs_return, 200


# Todo change the key of gnews api and remove the count limit of 5 hits
# Todo change the logic of url requests for gnews(to limit the number of calls)

##
## Actually setup the Api resource routing here
##
api.add_resource(GetData, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

