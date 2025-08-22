"""
Logger setup for the project.
Centralized logger with optional file and console output.
Enable/disable logging via .env variable LOG_ENABLED=True/False.
"""

import logging
from logging.handlers import RotatingFileHandler
from config import BASE_DIR
import os

LOG_ENABLED = os.getenv("LOG_ENABLED", "True").lower() in ["true", "1", "yes"]

def get_logger(name: str, log_file: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger instance.

    Args:
        name (str): Logger name, typically __name__.
        log_file (str, optional): Optional path relative to BASE_DIR to store logs.
        level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Disable logger entirely if LOG_ENABLED is False
    logger.disabled = not LOG_ENABLED

    if not logger.handlers and LOG_ENABLED:
        # Console handler
        ch = logging.StreamHandler()
        ch_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(ch_formatter)
        logger.addHandler(ch)

        # Optional file handler
        if log_file:
            log_path = BASE_DIR / log_file
            log_path.parent.mkdir(parents=True, exist_ok=True)
            fh = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=3)
            fh_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            fh.setFormatter(fh_formatter)
            logger.addHandler(fh)

    return logger


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    log = get_logger("demo_logger", "logs/demo.log")
    log.info("Logger initialized successfully.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
