from celery.task import task
import httplib
import urllib
import json
import socket

SEARCH_HOST="search.twitter.com"
SEARCH_PATH="/search.json"

@task
def query(tag):
    '''
        Executes a GET request to search twitter API for the passed tags
        Returns a tuple (tag, number of results')
    '''
    c = httplib.HTTPConnection(SEARCH_HOST)
    params = {'q' : tag}
    path = "%s?%s" %(SEARCH_PATH, urllib.urlencode(params))
    try:
        c.request('GET', path)
        r = c.getresponse()
        data = r.read()
        c.close()
        try:
            result = json.loads(data)
        except ValueError:
            print 'Error in parsing the retrieved data'
            return (tag, 0)
        if 'results' not in result or not result['results']:
            print 'No results in the retrieved data'
            return (tag, 0)
        return (tag, len(result['results']))
    except (httplib.HTTPException, socket.error, socket.timeout), e:
        print "search() error: %s" %(e)
        return (tag, 0)