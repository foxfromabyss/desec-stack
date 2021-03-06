import json

from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError


class RequestEntityTooLarge(APIException):
    status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    default_detail = 'Payload too large.'
    default_code = 'too_large'


class PDNSValidationError(ValidationError):
    pdns_code = 422

    def __init__(self, response=None):
        try:
            detail = json.loads(response.text)['error']
        except json.JSONDecodeError:
            detail = response.text

        return super().__init__(detail={'detail': detail}, code='invalid')


class PDNSException(APIException):
    def __init__(self, response=None):
        self.response = response
        return super().__init__(f'pdns response code: {response.status_code}, pdns response body: {response.text}')


class ConcurrencyException(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = 'Too many concurrent requests.'
    default_code = 'concurrency_conflict'
