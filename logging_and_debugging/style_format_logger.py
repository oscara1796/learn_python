import logging

# Configure the logger
formatter = logging.Formatter(
    fmt='{asctime} - {name} - {levelname} - {message}', 
    style='{'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('example')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Log a message
logger.debug('This is a debug message')
