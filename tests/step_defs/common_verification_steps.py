from pytest_bdd import then, parsers
from main.core.utils.logger import logger_request
from main.movies.utils.verify_response import VerifyResponse

@then(
    parsers.parse('the response status code should be "{statuscode}"')
)
def validate_status_code(request,statuscode):
    logger_request.info("validating the status code respnse"+
                        f"if should be {statuscode} and the real status code "+
                        f"is {request.respnse.status_code}")
    assert request.respnse.status_code == int(statuscode)

@then(
    parsers.parse(
        'the response body should have "{number}" elements'
    )
)
def validate_number_elements(request, number):
    logger_request.info(f"validating the response has {number} elements")
    assert len(request.response.json()) == int(number)
@then(
    parsers.parse('the response should fit the following schma "get_movies_schema.json"')
)
def validate_schema(request, schema):
    logger_request.info(
        f"validating the response against {schema} schema")
    schema_rep = request.response.json()
    veredict, msg = VerifyResponse.verify_schema(
        response = schema_rep,
        schema = schema
    )
    logger_request.info(f"the veredict:{veredict} whith the message: {msg}")
    assert veredict