c9twitter
=========

Python/J25 minimal tutorial shows the distributed processing with J25 horizontally scaleble workers

Installation
------------

### Prerequisites:

Python 2.7
RabbitMQ
Python-PyPI

Prepare your development environment:


Create a virtualenv:
arefaey@arefaey-Ideapad:~/workspace$ virtualenv c9devel --distribute --extra-search-dir=/usr/local/lib/python2.7/dist-packages/
From your created virtualenv, activate the virtualenv:
arefaey@arefaey-Ideapad:~/workspace/c9devel$ source bin/activate
Prompt should now be turned into:
	(c9devel)arefaey@arefaey-Ideapad:
install J25 framework
	(c9devel)arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter$ pip install -v j25framework
Installation of J25 will automatically download and install all J25 dependencies
Test your successful installation by the command j25 with no options:
	(c9devel)arefaey@arefaey-Ideapad:~/workspace/c9devel$ j25
	No command is given
	Possible commands: ['run-worker', 'dump-config', 'run-server', 'new-project', 'new-app', 'install-app']

Create a new project:
	(c9devel)arefaey@arefaey-Ideapad:~/workspace/c9devel$ j25 new-project c9twitter
	Creating project: c9twitter
	2012-06-06 16:26:47,914 - root - INFO - dumping configuration into file c9twitter/server.ini

From your project directory, add a new app to your project:
	arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter$ j25 new-app crawler
	2012-06-06 16:36:36,710 - root - INFO - loading configuration from file server.ini
	2012-06-06 16:36:36,730 - root - INFO - dumping configuration into file server.ini
	2012-06-06 16:36:36,731 - j25 - INFO - Application crawler has been created. Current project has been configured.

You now will notice like most MVC framework, you have a new app directory “crawler” under project/apps/ “c9devel/apps/”:
	arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter$ cd apps/crawler/
	arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter/apps/crawler$ ls
	config.py  controllers  __init__.py  lib  model  routing.py  static  tasks  templates  tests  tmp

Scenario
--------

Our scenario will be very simple, we will create a web controller responds to a specific URL requests and accepts a twitter search query as an array of tags, which will fire set of tasks to run asynchronously, each will grab the results of a tag.
We will notice the time consumed to execute these search processes decrease proportionally with the increase of the number of workers.
This is to endorse the idea of viral asynchronous tasks invocation and workers scalability.

### Test
-------

Now you are ready to run your project, start the server:
	(c9devel)arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter$ j25 run-server -l INFO
Start a worker in another shell:
	(c9devel)arefaey@arefaey-Ideapad:~/workspace/c9devel/c9twitter$ j25 run-worker -l INFO
From your browser request this URL passing your favorite tag array to search twitter for:
	http://127.0.0.1:8800/crawler/?tag=127.0.0.1:8800/crawler/?tag=montaro23&tag=cloud9ers&tag=j25&tag=tahrir&tag=invalidtag

You should get some results in the browser like this:

	Your search results: 
	montaro23
	has 15 tweets
	cloud9ers
	has 5 tweets
	j25
	has 15 tweets
	tahrir
	has 15 tweets
	invalidtag
	has 0 tweets
	All search queries consumed in: 239.180707932 ms.

Start now 2 additional workers in 2 separate shells, hit the same link and watch the difference in the time consumed:

	Your search results: 
	montaro23
	has 15 tweets
	cloud9ers
	has 5 tweets
	j25
	has 15 tweets
	tahrir
	has 15 tweets
	invalidtag
	has 0 tweets
	All search queries consumed in: 84.3038082123 ms.
	
### Enjoy ;)