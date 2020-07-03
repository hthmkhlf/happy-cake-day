import logging


# logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger  = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('learn.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
def divv(num1,num2):
    try:
        div =  num1 / num2
        logging.debug(div)
    except Exception as e:
        logger.error("Exception Raised", exc_info=True)

divv(2,0)