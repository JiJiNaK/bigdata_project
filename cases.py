from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('project').getOrCreate()

## 1) most_10_criminal_cases_in_2016

most_10_criminal_cases_in_2016=spark.read.csv('hdfs://localhost:9000/project1/Cases_against_Police_Personnels/2016_cases/000000_0',inferSchema=True)
most_10_criminal_cases_in_2016.show()

most_10_criminal_cases_in_2016=most_10_criminal_cases_in_2016.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS total_criminal_cases')
most_10_criminal_cases_in_2016.show()

import matplotlib.pyplot as plt

most_10_criminal_cases_in_2016.toPandas().plot(kind='bar', x='state_ut', y='total_criminal_cases', figsize=(20, 10))
plt.xlabel("State")
plt.ylabel("Count")
plt.title("2016")
plt.xticks(rotation=90)
plt.show()

# ### 2) most_10_criminal_cases_in_2017
#
# most_10_criminal_cases_in_2017=spark.read.csv('hdfs://localhost:9000/project1/Cases_against_Police_Personnels/2017_cases/000000_0',inferSchema=True)
# most_10_criminal_cases_in_2017.show()
#
# most_10_criminal_cases_in_2017=most_10_criminal_cases_in_2017.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS number_of_cases_registered')
# most_10_criminal_cases_in_2017.show()
#
# import matplotlib.pyplot as plt
#
# most_10_criminal_cases_in_2017.toPandas().plot(kind='bar', x='state_ut', y='number_of_cases_registered', figsize=(20, 10))
# plt.xlabel("State")
# plt.ylabel("Count")
# plt.title("2017")
# plt.xticks(rotation=90)
# plt.show()

### 3) most_10_criminal_cases_in_2018

# most_10_criminal_cases_in_2018=spark.read.csv('hdfs://localhost:9000/project1/Cases_against_Police_Personnels/2018_cases/000000_0',inferSchema=True)
# most_10_criminal_cases_in_2018.show()
#
# most_10_criminal_cases_in_2018=most_10_criminal_cases_in_2018.selectExpr('_c0 AS s_no','_c1 AS category','_c2 AS state_ut','_c3 AS number_of_cases_registered')
# most_10_criminal_cases_in_2018.show()
#
# import matplotlib.pyplot as plt
#
# most_10_criminal_cases_in_2018.toPandas().plot(kind='bar', x='state_ut', y='number_of_cases_registered', figsize=(20, 10))
# plt.xlabel("State")
# plt.ylabel("Count")
# plt.title("2018")
# plt.xticks(rotation=90)
# plt.show()

### 4)

# total_no_of_cases=spark.read.csv('hdfs://localhost:9000/project1/Cases_against_Police_Personnels/total_no_of_cases/000000_0',inferSchema=True)
# total_no_of_cases.show()
#
# total_no_of_cases=total_no_of_cases.selectExpr('_c0 AS s_no','_c1 AS state_ut','_c2 AS total_cases')
# total_no_of_cases.show()
#
# import matplotlib.pyplot as plt
#
# total_no_of_cases.toPandas().plot(kind='bar', x='state_ut', y='total_cases', figsize=(20, 10))
# plt.xlabel("State")
# plt.ylabel("cases")
# plt.title("total_no_of_cases")
# plt.xticks(rotation=90)
# plt.show()