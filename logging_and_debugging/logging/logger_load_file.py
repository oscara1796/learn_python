import logging
import logging.config

# Load the configuration from the file
logging.config.fileConfig('file.conf', disable_existing_loggers=False)

# Create a logger
logger = logging.getLogger('sampleLogger')

# Log events of different levels
logger.debug("This is a DEBUG message")   # Level: DEBUG
logger.info("This is an INFO message")   # Level: INFO
logger.warning("This is a WARNING message")  # Level: WARNING
logger.error("This is an ERROR message")  # Level: ERROR
