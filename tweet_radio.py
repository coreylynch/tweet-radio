import tweetstream
import re 
import time
import commands
import sys

punctre = re.compile('[!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~]')
urlre = re.compile('(?P<url>https?://[^\s]+)')

with tweetstream.SampleStream('username','pass') as stream:
	for tweet in stream:
		if 'text' in tweet:
			tweet_stripped = urlre.sub('',tweet['text'])
			tweet_stripped = punctre.sub('',tweet_stripped)
			if sys.argv[1] in tweet['text']:
				commands.getstatusoutput('say %s' % tweet_stripped) 
				time.sleep(1)