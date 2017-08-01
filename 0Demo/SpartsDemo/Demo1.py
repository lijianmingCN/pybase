
from sparts.tasks.queue import QueueTask
from sparts.vservice import VService

class AQueueTask(QueueTask):
    counter = 0
    def initTask(self):
        super(AQueueTask, self).initTask()
        print 'init'

    def execute(self, item, context):
        self.counter += 1

class AtcdVService(VService):
    def initService(self):
        print 1
    def initLogging(self):
        print 'log'

if __name__ == '__main__':
    AQueueTask(AtcdVService)

