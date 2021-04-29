punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(tweets):
    for x in punctuation_chars:
        if x in tweets:
            tweets = tweets.replace(x,'')
    return tweets


def get_pos(tweets):
    lst = strip_punctuation(tweets)
    lst = lst.lower().split()
    
    count = 0
    for word in lst:
        if word in positive_words:
            count += 1
    return count

def get_neg(tweets):
    lst = strip_punctuation(tweets)
    lst = lst.lower().split()
    
    count = 0
    for word in lst:
        if word in negative_words:
            count += 1
    return count 

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

output = open('resulting_data.csv','w')
output.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
output.write('\n')

file = open('project_twitter_data.csv','r')
rows = file.readlines()[1:]
for line in rows:
    positive_score = get_pos(line)
    negative_score = get_neg(line)
    net_score = positive_score - negative_score
    #print(f"positive words: {positive_score}, negative words: {negative_score}, Net score: {net_sco}")
    
    words = line.split(',')
    retweets = int(words[1])
    n_reply = int(words[2])
    
    file_rows = "{},{},{},{},{}".format(retweets,n_reply,positive_score,negative_score,net_score)
    output.write(file_rows)
    output.write('\n')
