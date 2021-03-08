# -*- coding: utf-8 -*-
# @Time : 2021/3/6 15:38
# @author :lidong

from mitmproxy import http

class Counter:
    def __init__(self):
        self.num = 0

    def request(self,flow: http.HTTPFlow) -> None:
        if f"v5/stock/batch/quote.json" in flow.request.pretty_url:
            with open(r"") as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )


addons = [
    Counter()
]