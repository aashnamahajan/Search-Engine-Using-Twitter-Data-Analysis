
# coding: utf-8

# In[ ]:


get_ipython().system('pip install -U -q PyDrive')
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)


# In[ ]:


#downloaded = drive.CreateFile({'id':"13tNhU9cbcVyMvfhtgYZ8bGxSpO9sQJ8_"}) 
from google.colab import drive
drive.mount('/content/drive/')
#downloaded.GetContentFile('usa_tweets.json')


# In[ ]:


import json
import pandas as pd 
import numpy
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


# In[ ]:


tweets=[]
complete_tweets = []
final_tweets = []
brazil = ["jairbolsonaro", "carlosbolsonaro", "cirogomes", "Francischini_", "GuilhermeBoulos"]
india = ["ArvindKejriwal", "narendramodi", "PiyushGoyal", "sachinpilot", "sardesairajdeep", "ShashiTaroor", "VasundharaBJP"]
usa = ["BernieSanders","BetoORourke","ewarren","KamalaHarris","tedlieu","AdamSchefter", "CoryBooker"]
counter = 0
with open("/content/drive/My Drive/Colab Notebooks/combined_brazil.json","r",encoding = "utf-8") as infile:
  for line in infile:
    counter += 1
    try:
      tweet = json.loads(line.rstrip('\n'))
    except:
      break
    print (counter)
    if tweet["user"]["screen_name"] in brazil and tweet["in_reply_to_status_id"] == None:
      if tweet["tweet_lang"] != "en" and "translation" in tweet:
        tweets.append(tweet["translation"])
        complete_tweets.append(tweet)
      else:
        tweets.append(tweet["text_en"])
        complete_tweets.append(tweet)
    else:
      final_tweets.append(tweet)
df = pd.DataFrame({"text" : tweets})


# In[ ]:


len(final_tweets)


# In[ ]:


len(complete_tweets)#-len(final_tweets)


# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text

br_my_stop_words = text.ENGLISH_STOP_WORDS.union(["10","time","brazil","brazilian","thank","thanks","don","t","got","good","like","did","make","ll","just","yes","thing","sir","help","town","day","qb","wr","pm","news","https","39","pt","let", "today", "bolsonaro", "quot", "watch", "video", "people"])
en_my_stop_words = text.ENGLISH_STOP_WORDS.union(["thank","thanks","don","t","got","good","like","did","make","ll","just","yes","thing","sir","help","town","day","qb","wr","people","rb","hc"])
#hi_my_stop_words = text.ENGLISH_STOP_WORDS.union(["prime","time","indian","shri","ji","india","thank","thanks","don","t","got","good","like","did","make","ll","just","yes","thing","sir","pm","https","god","tv","watch","today","39","life"])
#hi_my_stop_words = text.ENGLISH_STOP_WORDS.union(["don","pm","news","day","https","ji","shri","years","today","39","new","time","god","tv"])
hindi_stopwords = text.ENGLISH_STOP_WORDS.union(["don","t","got","good","like","did","make","ll","just","yes","thing","sir","ji","today","39","mr","pm","tv","shri","wonderful","thank","wishes","day","met","various","time","years","going"])
count_vect = CountVectorizer(max_df=0.8, min_df=2, stop_words=br_my_stop_words)
doc_term_matrix = count_vect.fit_transform(df['text'].values.astype('U'))


# In[ ]:


LDA = LatentDirichletAllocation(n_components=5, random_state=42)

LDA.fit(doc_term_matrix)


# In[ ]:


for i,topic in enumerate(LDA.components_):
    print(f'Top 10 words for topic #{i}:')
    print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print('\n')


# In[ ]:


print (LDA.components_[0])


# In[ ]:


topic_values = LDA.transform(doc_term_matrix)
topic_values.shape


# In[ ]:


topic_values[0]


# In[ ]:


dict_india = {0:"governemnt", 1: "politics", 2:"government", 3:"development work", 4:"bjp", 5:"birthday wishes", 6:"indian railways"}
dict_brazil = {0:"ciro", 1:"lula", 2:"government crisis", 3:"education", 4:"pdt"}
i = 0

for tweet in complete_tweets:
  tweet["topic"] = dict_brazil[int(topic_values[i].argmax())]
  i += 1
  for twt in final_tweets:
    if tweet["id"] == twt["in_reply_to_status_id"]:
        twt["topic"] = tweet["topic"]


# In[ ]:


complete_tweets.extend(final_tweets) 

with open("/content/drive/My Drive/Colab Notebooks/combined_brazil_topics.json","w",encoding = "utf-8") as f:
  for tweet in complete_tweets:
    json.dump(tweet, f, ensure_ascii=False)
    f.write('\n')


# In[ ]:


complete_tweets[30667]


# In[ ]:


for tweet in complete_tweets:
    if tweet["id"] == 1170148460705669120:
    print (tweet["text_en"])
    print (tweet["topic"])


# In[ ]:


len(complete_tweets)

