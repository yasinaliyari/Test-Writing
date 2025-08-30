from locust import HttpUser, task, between, constant, constant_pacing, tag


class SampleUser(HttpUser):
    wait_time = between(0.3, 0.5)
    # wait_time = constant(0.7)
    # wait_time = constant_pacing(1)

    # def on_start(self):
    #     pass

    @task
    def get_detail(self):
        pass

    @task
    def create_order(self):
        pass

    @task
    def orders_list(self):
        pass

    @tag("test_network")
    @task
    def test_html(self):
        self.client.get("/")

    # def on_stop(self):
    #     pass
