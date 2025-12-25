from unittest import TestCase
from pyspark.sql import SparkSession
from utils import load_csv_df , count_by_country

class TestUtils(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = SparkSession.builder.master("local[3]").appName("HelloSparkTest").getOrCreate()
        
    
    def test_Datafile_load(self):
        sample_df = load_csv_df(self.spark , "datasets/survey.csv")
        count_list = count_by_country(sample_df).collect()
        
        count_dict = {}
        for row in count_list:
            count_dict[row["Country"]] = row["count"]
            
        
        self.assertEqual(count_dict["UK"] , 2  , "UK has 2 ")
        self.assertEqual(count_dict["USA"] , 2  , "USA has 2 ")
        self.assertEqual(count_dict["Canada"] , 5  , "Canada has 5 ")
        self.assertEqual(count_dict["India"] , 1  , "India has 1 ")
        
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.spark.stop()
    
    
if __name__ == "__main__":
    import unittest
    unittest.main()