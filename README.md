# #aufschrei revisited

## Analysing #aufschrei with Python

### Requirements

* Python 3 with all necessary packages installed
  * nltk==3.0.2
  * numpy==1.9.2
  * pandas==0.16.0
  * pymongo==3.0.1
  * python-dateutil==2.4.2
  * pytz==2015.2
  * six==1.9.0
* MongoDB (or enabled port-forwarding to a remote MongoDB)

### Set-up

* Either:
  * EITHER: import the tweets to your local MongoDB instance using `tweets2db.py`
  * OR: open a an ssh port-forwarding connection in a separate command line window
```
ssh -L 27017:localhost:27017 username@server
```
* start the iPython notebook by running
    `ipython3 notebook`

* when done: save notebook and stop the notebook server
* close the ssh connection by typing `exit`

### Contents
- Word statistics
  * tokenizing
  * word freqs
  * removing stopwords
  * extracting usernames and hashtags
  * text concordance, common contexts, collocations
  * text dispersion
- Cooccurrences and ngrams
  * most common tweets (that are not technically RTs)
  * ngrams
- User stats
  * user activity (most active, ranking users by activity)
  * creating user specific corpora

### Ideas for further research
* Does applying machine learning algorithms aid the categorization of Tweets?
* Tweet statistics (such as: Most often retweeted, most favourited) and examine
whether this kind of 'meta-data' can aid categorization
* Fancy graphs and timelines! (matplotlib or R/ggplot2)

### Bibliography
* Steven Bird, Ewan Klein & Edward Loper: Natural Language Processing with Python. O'Reilly 2009
* Wes McKinney: Python for Data Analysis. O'Reilly 2013
* Matthew A. Russell: Mining the Social Web. O'Reilly 2014
* Axel Maireder, Stephan Schlögl: [24 hours of an #outcry: The networked publics of a socio-political debate](http://ejc.sagepub.com/content/29/6/687). EJC 2014

### Related Projects
* [aufschreiStat](https://github.com/lenaschimmel/aufschreiStat) - Aufschrei
statistics in Java, which was never finished but served as an inspiration to
this project
* [aufschreib](https://github.com/ffalt/aufschreib) - A JavaScript webapp to
classify #aufschrei Tweets (manually and through automatic categorization) and
create statistics/timelines
* [#aufschrei Timeline](http://aufschrei.konvergenzfehler.de/) - Display of all
#aufschrei Tweets
* [24 hours of an #outcry: The networked publics of a socio-political debate](http://homepage.univie.ac.at/axel.maireder/2014/02/24-hours-of-an-outcry-the-networked-publics-of-a-socio-political-debate/)
([EJC paper](http://ejc.sagepub.com/content/early/2014/09/01/0267323114545710.abstract))
 - Analysis of the first 24 hours (timeline, content, user networks)
