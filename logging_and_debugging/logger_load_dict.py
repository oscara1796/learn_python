import logging 
import logging.config
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    print(config)
    logging.config.dictConfig(config)
    
logger = logging.getLogger(__name__)

logger.debug('This is a debug message ')