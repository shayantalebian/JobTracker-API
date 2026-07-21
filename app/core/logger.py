import logging
import sys


def setup_logger() -> logging.Logger:
    """Configures and returns the main application logger."""
    logger = logging.getLogger("jobtrackr")
    logger.setLevel(logging.INFO)

    # Define a clean format: Time - LoggerName - Level - Message
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Output logs to the standard console (stdout)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Prevent adding multiple handlers if logger is called multiple times
    if not logger.handlers:
        logger.addHandler(stream_handler)

    return logger


# Expose a globally accessible logger instance
logger = setup_logger()
