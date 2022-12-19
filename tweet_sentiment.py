# Tweet Sentiment Analyzer

import sys
import json
import string

#Create a dictionary of words and their scores using the AFINN file
def reference():
    afinnfile = open("Data.txt")
    scores = {}					 	# initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t") 			# The file is tab-delimited."\t" means "tab character"
	scores[term] = int(score) 			# Convert the score to an integer.
    #print scores.items()                               # Print every (term, score) pair in the dictionary
    return scores


#Load the tweets from the file and extract the english tweets
def tweet_load(tweet_file):
    a=0
    tweets={}                                                        #get the twitter stream data and store in this dictionary
    for line in tweet_file:
	tweetDict=json.loads(line)                                          #parsing entire file into a dictionary
        if "text" in tweetDict and tweetDict['lang']=='en':
		   tweets[a]= tweetDict["text"].encode('utf-8').lower().translate(None,string.punctuation)
		   a+=1
    #print tweets
    return tweets                               #returns the dictionary which consists of only english tweets


#Calculate sentiment of english tweets
def calc_senti(tweets,scores):
    sentiment_output=open("tweet_sentiment_first20.txt","w")           #File to write output of the program.Close it properly
    for k,v in tweets.iteritems():                                                 #iterate python dictionary and split the string into words
        x=0  							                   #used to keep sum of score
        words=v.split()
        for v in words:
            if v in scores:
                x+=scores[v]
        print x
        sentiment_output.write(str(x)+ "\n") 	                 #write to output file
    sentiment_output.close()
    return


def main():
    senti_file = open("Data.txt")                      #command line args -#(sys.argv[1])
    tweet_file = open("first20.txt")    #(sys.argv[2])
    scores=reference()
    calc_senti(tweet_load(tweet_file),scores)

#Call the main() using this boiler plate method.
if __name__ == '__main__':
    main()
