import logging


logging.basicConfig(format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.warning("This is a warning message")


name = 'John'

logging.error(f'{name} found an error')