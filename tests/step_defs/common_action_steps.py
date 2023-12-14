from pytest_bdd import when, parsers
from main.core.utils.logger import logger_request
from main.core.api.request_manager import RequestManager


@when(
    parsers.parse(
        'the user send "{httpmethod}" request to "{endpoint}" endpoint'
    )
)
def send_request(request, httpmethod, endpoint):
    logger_request.info(f"sending a request{httpmethod} to {endpoint} endpoiint")
    request_manager = RequestManager.get_instance()
    try:
        params = request.params
    except AttributeError:
        params = None
    request.response = request_manager.make_request(
        httpmethod = httpmethod,
        endpoint = endpoint,
        payload = params
    )
