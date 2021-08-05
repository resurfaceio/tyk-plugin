from tyk.decorators import *
from time import time
from usagelogger import HttpLogger, HttpMessage, HttpRequestImpl, HttpResponseImpl


class HttpLoggerForTyk:
    def __init__(self, URL, logging_rules):
        self.start_time = 0
        self.req = None
        self.res = None
        self.logger = HttpLogger(url=URL, rules=logging_rules)

    def get_interval(self):
        interval = time() - self.start_time
        self.start_time = 0
        return interval

    def log_request(self, request):
        self.start_time = time()
        self.req = HttpRequestImpl(
            method=request.object.method,
            url="{}://{}{}".format(
                request.object.scheme,
                request.get_header("Host"),
                request.object.request_uri
                ),
            headers=request.object.headers,
            params=request.object.params,
            body=request.object.body
        )
    
    def log_response(self, response):
        self.res = HttpResponseImpl(
            status=response.status_code,
            headers=response.headers,
            body=response.body
        )

    def send(self):
        HttpMessage.send(
            self.logger,
            request=self.req,
            response=self.res,
            interval=self.get_interval()
        )
        self.req = None
        self.res = None

resurface_logger = HttpLoggerForTyk("http://172.17.0.1:4001/message", "include debug")


@Hook
def PreHook(request, session, spec):
    resurface_logger.log_request(request)
    return request, session


@Hook
def ResponseHook(request, response, session, metadata, spec):
    resurface_logger.log_response(response)
    resurface_logger.send()
    return response
