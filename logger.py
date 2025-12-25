import logging

class Log4J:
    def __init__(self, spark):
        """
        Initialize a logger compatible with PySpark.
        :param spark: SparkSession object
        """
        # Get Spark's JVM logger
        self.logger = spark._jvm.org.apache.log4j.LogManager.getLogger(__name__)

    def info(self, message):
        """Log an info message"""
        self.logger.info(message)

    def warn(self, message):
        """Log a warning message"""
        self.logger.warn(message)

    def error(self, message):
        """Log an error message"""
        self.logger.error(message)
