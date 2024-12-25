import logging

default_log_levels = {
    "asyncio": logging.INFO,
    "boto3": logging.INFO,
    "botocore": logging.ERROR,
    "docker": logging.WARNING,
    "elasticsearch": logging.ERROR,
    "hpack": logging.ERROR,
    "moto": logging.WARNING,
    "requests": logging.WARNING,
    "s3transfer": logging.INFO,
    "urllib3": logging.WARNING,
    "werkzeug": logging.WARNING,
    "rolo": logging.WARNING,
    "parse": logging.WARNING,
    "localstack.aws.accounts": logging.INFO,
    "localstack.aws.protocol.serializer": logging.INFO,
    "localstack.aws.serving.wsgi": logging.WARNING,
    "localstack.request": logging.INFO,
    "localstack.request.internal": logging.WARNING,
    "localstack.state.inspect": logging.INFO,
    "localstack_persistence": logging.INFO,
}

trace_log_levels = {
    "rolo": logging.DEBUG,
    "localstack.aws.protocol.serializer": logging.DEBUG,
    "localstack.aws.serving.wsgi": logging.DEBUG,
    "localstack.request": logging.DEBUG,
    "localstack.request.internal": logging.INFO,
    "localstack.state.inspect": logging.DEBUG,
}


