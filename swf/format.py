from . import constants
import logging

from simpleflow.utils import json_dumps, json_loads_or_raw


logger = logging.getLogger(__name__)


def decode(content):
    return json_loads_or_raw(content)


def wrap(message, max_length):
    if not message:
        return message

    if len(message) > max_length:
        logger.warning(
            'message "{}" too long ({} chars), wrapped to {}'.format(
                message,
                len(message),
                max_length,
            ))
        return message[:max_length]

    return message


def details(message):
    return wrap(message, constants.MAX_DETAILS_LENGTH)


def execution_context(message):
    return wrap(message, constants.MAX_EXECUTION_CONTEXT_LENGTH)


def heartbeat_details(message):
    return wrap(message, constants.MAX_HEARTBEAT_DETAILS_LENGTH)


def identity(message):
    return wrap(message, constants.MAX_IDENTITY_LENGTH)


def input(message):
    return wrap(json_dumps(message), constants.MAX_INPUT_LENGTH)


def reason(message):
    return wrap(message, constants.MAX_REASON_LENGTH)


def result(message):
    return wrap(json_dumps(message), constants.MAX_RESULT_LENGTH)
