from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task(2)
    def topics(self):
        self.client.get("/topics/")

    @task(1)
    def login(self):
        self.client.get("/login/")

    @task(1)
    def hello(self):
        self.client.get("/hello/")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
