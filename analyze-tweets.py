import json
import pandas as pd
import matplotlib.pyplot as plt
import re


def search_string_in_text(search_string, text):
    search_string = search_string.lower()
    text = text.lower()
    match = re.search(search_string, text)
    if match:
        return True
    else:
        return False


twitter_data_file_name = 'twitter-data2.txt'

search_terms = ['brain cancer', 'colon cancer', 'lung cancer', 'breast cancer', 'prostate cancer',
'leukemia', 'melanoma','pancreatic cancer']

tweets_array = []
twitter_data_file = open(twitter_data_file_name, 'r')
for line in twitter_data_file:
    try:
        tweet = json.loads(line)
        tweets_array.append(tweet['text'])
    except:
        print('There was an error loading a JSON representation of a tweet; we will just ignore it.')
        continue


print('We read {} tweets from the file {}'.format(len(tweets_array), twitter_data_file_name))

# Create a pandas dataframe to store our twitter data:
tweets = pd.DataFrame(data=tweets_array, columns=['text'])

tweets['python'] = tweets['text'].apply(lambda tweet: search_string_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: search_string_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: search_string_in_text('ruby', tweet))
tweets['fortran'] = tweets['text'].apply(lambda tweet: search_string_in_text('fortran', tweet))
# Better way to do this one too???
tweets['brain cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('brain cancer', tweet))
tweets['colon cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('colon cancer', tweet))
tweets['lung cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('lung cancer', tweet))
tweets['breast cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('breast cancer', tweet))
tweets['prostate cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('prostate cancer', tweet))
tweets['leukemia'] = tweets['text'].apply(lambda tweet: search_string_in_text('leukemia', tweet))
tweets['melanoma'] = tweets['text'].apply(lambda tweet: search_string_in_text('melanoma', tweet))
tweets['pancreatic cancer'] = tweets['text'].apply(lambda tweet: search_string_in_text('pancreatic cancer', tweet))


print(tweets.head(10))

# Original solution:
# tweets_by_prog_lang = [tweets['python'].value_counts()[True], 
#         tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True],
#             tweets['fortran'].value_counts()[True]]
#
# We fix this by using a list comprehension that sets the count to zero in the columns
# where there is no True values:
tweets_by_prog_lang = [tweets[st].value_counts()[True] if True in tweets[st].value_counts() else 0 for st in search_terms]

x_pos = list(range(len(search_terms)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prog_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs javascript vs ruby vs fortran(Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(search_terms)
plt.grid()
plt.show()
