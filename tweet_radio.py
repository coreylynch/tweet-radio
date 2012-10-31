import tweetstream
import re 
import time
import commands
import sys

punctre = re.compile('[!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~]')
urlre = re.compile('(?P<url>https?://[^\s]+)')

with tweetstream.SampleStream('jerilynch','gracie') as stream:
	for tweet in stream:
		if 'text' in tweet:
			tweet_stripped = urlre.sub('',tweet['text'])
			tweet_stripped = punctre.sub('',tweet_stripped)
			if sys.argv[1] in tweet['text']:
				if sys.argv[2] == '':
					commands.getstatusoutput('say %s' % tweet_stripped) 
					time.sleep(1)
				else:
					commands.getstatusoutput('say -v %s %s' % (sys.argv[2], tweet_stripped))
					time.sleep(1)


				