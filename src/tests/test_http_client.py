import unittest
import asyncio
import config
from src.services.http_client import HTTPClient

class TestHTTPClient(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repository = HTTPClient()

    def test_get(self) -> None:
        loop = asyncio.get_event_loop()
        response =  loop.run_until_complete(asyncio.gather(self.user_repository.get("http://httpbin.org/get")))
        print(response)

    def test_post(self) -> None:
        loop = asyncio.get_event_loop()
        response =  loop.run_until_complete(asyncio.gather(self.user_repository.post("http://httpbin.org/post", data = {"test" : 1})))
        print(response)
