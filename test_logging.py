import logging

logger = logging.getLogger(__name__)

def test_logging_warning_success():
    logger.warning('\n\n @@@ this will NOT be printed \n\n')
    assert True

def test_logging_warning_fail():
    logger.warning('\n\n @@@ this WILL be printed @@@ \n\n')
    assert False

def test_logging_info_fail():
    logger.info('\n\n @@@ this will NOT be printed @@@ \n\n')
    assert False
    
