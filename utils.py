import configparser

from pyspark import SparkConf


def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    config.read("spark.conf")
    
    # Read configs from section SPARK_APP_CONFIGS
    for (key, val) in config.items("SPARK_APP_CONFIGS"):
        # Only set keys that start with spark.
        if key.startswith("spark."):
            spark_conf.set(key, val)
    
    
    return spark_conf


def load_csv_df(spark , filepath):
    return spark.read\
        .option("header" , "true")\
        .option("inferSchema" , "true")\
        .csv(filepath)
    
def count_by_country(survey_df):
    return survey_df.where("Age < 40").select("Age" , "Gender" ,"Country" , "State").groupBy("Country").count()