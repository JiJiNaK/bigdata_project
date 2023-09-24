# bigdata_project

"In this project, I am going to analyze crime data in India. Here, we used big data tools such as Hadoop, Hive, Spark, and Matplotlib. The data downloaded from Kaggle is loaded into Hadoop and then into a Hive table. Analysis is performed on this Hive table. In Hive, we used the SerDe method, as well as group by and order by functions for filtering the data. The output obtained is plotted in a bar graph using Matplotlib in pyspark."
![collage](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9c76e5d5-82ec-46e1-a519-6538e2813116)

Steps:
1. The dataset is downloaded from Kaggle and loaded into HDFS.
   ![1_creating_directory_hadoop](https://github.com/JiJiNaK/bigdata_project/assets/144101140/6aeda6a4-41ab-449b-b539-43bfa5679cb4)
   ![2_dataloadedto_hadoop](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ffd96247-73ec-4b95-879e-2dccdfcdbe9b)

2. From HDFS, data is loaded into Hive by creating database.
   ![creating_database_1](https://github.com/JiJiNaK/bigdata_project/assets/144101140/cf554834-63d9-4a19-8335-561ea1ceb69d)

   a) Using SerDe properties, data is loaded into the table by removing quotes.

   * 2016 cases against Police Personals

   ![01_creating_table_using_serde_method](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e997a1c2-cfaa-4e17-a781-28f7b015ad0a)
   ![1 loaddatahdfs2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/5a8ec393-6215-4101-bb89-6c8c80b3eeb2)


   * 2017 cases against Police Personals

   ![2 createnormal table 2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/0e052bba-68c2-4b96-95a9-57072450e556)
   ![2 loaddatahdfs2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/f560c245-cc87-40bb-ba7d-bd4e8009aa2e)


   * 2018 cases against Police Personals
  
   ![3 create normal table 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9a056e18-39cf-42dc-9c49-e98b46e3c65e)
   ![3 loaddatahdfs2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/dec55abe-e4f0-4026-9a23-eeddfe2d0adc)

   b) From this table, data is loaded into a main table.

   * 2016 cases against Police Personals

   ![1 newtable created 2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e48a71ef-a80c-461e-b4fb-07f21cc85b9f)
   ![1 insert2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/07769757-1877-4724-9a06-2ee42afce372)

   * 2017 cases against Police Personals

   ![2 create newtable2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/22115f6e-ea12-4aec-aa82-70c736e80555)
   ![2 insert2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/55efca23-5390-4844-86a8-44e8ccd4f258)

   * 2018 cases against Police Personals
  
   ![3 create new table 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a957106d-b598-46cc-b8ba-c85bd0fb8b84)
   ![3 insert 2018 ](https://github.com/JiJiNaK/bigdata_project/assets/144101140/619f6a56-0421-46e4-8434-4033660b3cfa)

   c) Using the group by and order by functions in Hive, the top 10 states with the highest number of cases for three years(2016,2017,2018) recorded are filtered, and this          result is loaded into a table.

   ![creating_all_cases](https://github.com/JiJiNaK/bigdata_project/assets/144101140/cca69829-746d-4b99-89f0-bc701f5d94ee)
   ![insert_into_all_cases](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e7c59e6b-ca74-4abb-949d-8e8f27181b3f)
   ![insert_into_all_cases_2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/6a3dbf02-7f2a-4add-a203-54e86beef6d7)
   ![insert_into_all_cases_2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3403c123-09d9-4aa0-80e2-ceddbe6bbdff)
   
   ![1 total_cases police](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9706486d-7522-48a9-9868-8a949e970027)
   ![1 total_no_cases desc](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a7e7b867-e7a9-4382-a926-df9a57119d70)
   ![1 total no cases insert hdfs](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ee39a770-b772-42e9-8fc9-c9a636d6b4a8)

   d) From each table with cases in the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported in each year are filtered.








   
   

4.
   a) Using SerDe properties, data is loaded into the table by removing quotes (strings).
   b) From this table, data is loaded into a main table.
   c) From each table with cases in the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported in each year are filtered.
   d)  Using the group by and order by functions in Hive, the top 10 states with the highest number of cases recorded are filtered, and this result is loaded into a table.
   e) Finally, the output is loaded into the Hadoop directory, and graphs are plotted using Matplotlib.


   




