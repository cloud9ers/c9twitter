from j25.web import Controller
from apps.crawler.tasks.asynch import query
from celery.task.sets import TaskSet
from time import time

class C9Twitter(Controller):
    def search(self):
        '''
            Extracts the search tags from the request query string
            Runs set of tasks asynchronusly, each per tag
            Returns the search results and the time consumed
        '''
        tags = self.request.GET.getall('tag')
        tasks = []
        # prepare list of sub tasks
        for tag in tags:
            tasks.append(query.subtask((tag, )))
        job = TaskSet(tasks=tasks)
        result = job.apply_async()
        # calculate the time consumed
        start_time = time()
        all_tags_data = result.join()
        end_time = time()
        spent = (end_time - start_time)*100
        # prepare the output text
        output = 'Your search results: \n'
        for tag_data in all_tags_data:
            output += tag_data[0] + '\n' + 'has %s tweets' % tag_data[1] + '\n'
        output  += 'All search queries consumed in: %s ms.' % spent
        return output