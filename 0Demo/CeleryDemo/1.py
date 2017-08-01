from celery import Celery

app = Celery('tasks', broker='redis://123.57.230.194:9001/0')

@app.task
def add(x, y):
    return x + y



