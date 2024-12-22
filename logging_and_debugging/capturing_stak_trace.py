import logging 

a=5
b=0

try:
    c = a / 0
except:
    logging.error('Exception ocurred', exc_info=True)


print("CONTINUE EXECUTION")