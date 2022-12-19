# Word Frequency count 

import sys
import json
import string

#Load the tweets from the file and extract the english tweets
def tweet_load(tweet_file):
    a=0
    tweets={}
    for line in tweet_file:
	tweetDict=json.loads(line)                                          #parsing into python dictionary
        if "text" in tweetDict and tweetDict['lang']=='en':
		   tweets[a]= tweetDict["text"].encode('utf-8').lower().translate(None,string.punctuation)
		   a+=1
    #print tweets
    return tweets


#Calculate frequency of the words
def calc_freq(tweets):
    frequency_output=open("frequency_first20.txt","w")        #File to write output of the program. Check if closed properly
    totalwords=0
    tweet_words={}
    freq_words={}

    for k,v in tweets.iteritems():                               #iterate python dictionary and split the string into words
        words=v.split()
        totalwords+=len(words)                                   #count total no of words

        for k in words:
            if k in tweet_words and tweet_words[k]>0:          #no need to check tweet_words[k]>0
	        tweet_words[k]+=1
	    else:
	        tweet_words[k]=1


    for k in tweet_words:
	freq_words[k]=float(tweet_words[k])/totalwords
    	print "%s,%.6f" %(str(k),freq_words[k])
        frequency_output.write(str(k)+" : %.6f"%(freq_words[k])+" \n")                #write to output file

    #print totalwords

    frequency_output.close()
    return


def main():
    tweet_file = open(sys.argv[1])
    calc_freq(tweet_load(tweet_file))

#Call the main() using this boiler plate method.
if __name__ == '__main__':
    main()
