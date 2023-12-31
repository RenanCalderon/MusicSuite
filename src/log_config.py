import logging, os, sys
from logging.handlers import RotatingFileHandler

executable_path = os.path.dirname(sys.argv[0])
log_file = os.path.join(executable_path, 'app.log')


def setup_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Check if logger already has handlers (to avoid duplication)
    if not logger.hasHandlers():
        # Create a handler to write to a rotating file
        file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3)
        file_handler.setLevel(logging.DEBUG)

        # Create a handler to display logs on the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a format for the logs
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Apply the format to the handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


LOG = setup_logger()
