from pyspark import SparkConf
from pyspark.sql import SparkSession
from utils import count_by_country, get_spark_app_config, load_csv_df
from logger import Log4J  # import your custom logger
import os

# Suppress Java incubator warnings
# os.envir/on['PYSPARK_SUBMIT_ARGS'] = '--conf "spark.driver.extraJavaOptions=-Xlint:none" pyspark-shell'

if __name__ == '__main__':
    
    conf = get_spark_app_config()

    # Create Spark session
    spark = SparkSession.builder \
        .config(conf=conf) \
        .getOrCreate()

    # Hide Spark internal logs
    spark.sparkContext.setLogLevel("WARN")

    # Initialize logger
    logger = Log4J(spark)
    # conf_out = spark.sparkContext.getConf()
    # logger.info(conf_out.toDebugString())
    
    logger.error("Hello")
    survey_df = load_csv_df(spark=spark , filepath="datasets/survey.csv")
    partitioned_df = survey_df.repartition(2)
    count_df = count_by_country(partitioned_df)
    count_df.show()
    logger.error(count_df.collect())
    # a = str(input("Press Enter"))
    # spark.stop()
    logger.error("Finished")