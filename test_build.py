#!/usr/bin/env python3
import os

from ci.ci import CI
from ci.logger import configure_logging

def run_test():
    """Run tests on container tags then build and upload reports"""
    ci.run(ci.tags)
    ci.report_render()
    ci.badge_render()
    ci.report_upload()
    if ci.report_status == 'PASS':  # Exit based on test results
        logger.info('Tests PASSED')
        ci.log_upload()
        return
    logger.error('Tests FAILED')
    ci.log_upload()


if __name__ == '__main__':
    log_level = os.environ.get("CI_LOG_LEVEL","DEBUG")
    configure_logging(log_level)
    import logging
    logger = logging.getLogger(__name__)
    ci = CI()
    try:
        run_test()
    except Exception as err:
        logger.exception("%s\nI Can't Believe You've Done This",err)
