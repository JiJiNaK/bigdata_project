# Crime Analysis

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

   * 2016 Escape from Police Custody

   ![1 create normal table2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e45b1d63-fd8c-4dc2-82c8-0ddc6ef2de48)
   ![1 loaddatahdfs2016(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a4ff78a0-2a9a-4200-bb4e-2e2b2b98be6c)

   * 2017 Escape from Police Custody
     
   ![2 create normal table 2017(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/506d03a6-d0f4-4225-95ca-2f5ea6cbfc27)
   ![2 loaddatahdfs2017(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a9724f1d-4d88-45ff-b44a-6f1727d89ccf)

   * 2018 Escape from Police Custody
     
   ![3 create noraml table 2018(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/77a2dba6-31aa-4e31-bb78-986245c8ea64)
   ![3 loaddata hdfs 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/96ba99d4-abec-4dd8-858c-14145836c846)

   The data is already in integer datatype, so the serde property is not used. Instead, a table is created and loaded directly into HDFS. (2016 victims of rape)

   * 2016 Victims of Rape
  
   ![1 create table vit2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/774e4723-c3e6-4854-8901-6086f47507d6)
   ![1 loaddatahsdfs2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/8100b71d-edbd-4ad6-ad52-d0a700d3a3e1)

   * 2017 Victims of Rape
  
   ![2 create table vit 2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/024acc2a-c7d7-4550-82af-9af58bab0add)
   ![2 loaddatahdfs2017(2)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ba82fdb8-ecba-4c26-8a81-b39010399fc7)

   * 2018 Victims of Rape

   ![3 create normal table2018 ](https://github.com/JiJiNaK/bigdata_project/assets/144101140/cc18d06c-cd52-497d-b725-2c19970396b7)
   ![3 loaddatafromhdfs2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/1a5526c9-f301-4e1b-9242-75c85e260883)

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

   * 2016 Escape from Police Custody

   ![1 newtable2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/da1ac221-b5dd-47eb-bde4-d5b3336a70b7)
   ![1 insert 2016 ](https://github.com/JiJiNaK/bigdata_project/assets/144101140/7be2b4c9-33eb-42fd-8c7e-c795356f1ee3)

   * 2017 Escape from Police Custody

   ![2 2017 new table create(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/caa3af72-7364-4c6e-82fc-37c3abc04131)

   * 2018 Escape from Police Custody

   ![3 create newtable 2018(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ddc2b8c5-17b2-4327-8087-8d4991e0055e)
   ![3 insert 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/20888b28-6466-4aab-833a-b7108729fb6e)

   * 2018 Victims of Rape

   ![3 create newtable2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3a1a8a43-3e95-419f-9849-f13a008539db)
   ![3 insert 3 table 2018(1)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/56258286-7e30-450f-9180-38413ce25dc9)

   c) Using the group by and order by functions in Hive, the top 10 states with the highest number of cases for three years(2016,2017,2018) recorded are filtered, and this          result is loaded into a table.

   * Total number of cases in three years(2016,2017,2018)

   ![creating_all_cases](https://github.com/JiJiNaK/bigdata_project/assets/144101140/cca69829-746d-4b99-89f0-bc701f5d94ee)
   ![insert_into_all_cases](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e7c59e6b-ca74-4abb-949d-8e8f27181b3f)
   ![insert_into_all_cases_2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/6a3dbf02-7f2a-4add-a203-54e86beef6d7)
   ![insert_into_all_cases_2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3403c123-09d9-4aa0-80e2-ceddbe6bbdff)
   
   ![1 total_cases police](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9706486d-7522-48a9-9868-8a949e970027)
   ![1 total_no_cases desc](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a7e7b867-e7a9-4382-a926-df9a57119d70)
   ![1 total no cases insert hdfs](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ee39a770-b772-42e9-8fc9-c9a636d6b4a8)

   * Total number of Escape in three years(2016,2017,2018)

   ![1 create 3 table 2016(2)](https://github.com/JiJiNaK/bigdata_project/assets/144101140/58dfa60a-089a-44be-9546-06c4c3a6ee2d)
   ![1 insert 3 tables2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/0fa271f6-f237-43e2-98ff-7e553d1917cc)
   ![2 insert 3 tables2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/b8db7806-bf53-499e-8167-5c6eeca0f1ab)
   ![3 insert 3 table 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/06c2ebe4-13fe-44a8-934a-72eff1b905dc)

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/823ff9dd-0017-4acd-abad-876d3226cea4)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/82414c63-70d0-4968-a29f-91437ea17d3b)
   ![insert](https://github.com/JiJiNaK/bigdata_project/assets/144101140/f2125446-2382-45fd-a010-72bbff50f2d5)

   * Total number of Victims in three years (2016,2017,2018)

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/1131e1cf-eaf5-40e1-adc4-2e31ddcffca0)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/4bbcaecb-1757-4d85-a076-a7f516db2f16)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9f01c2c9-b17a-4cc0-97fd-545ffc54d8c3)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/2c8901d7-ca75-4038-ba64-4dd236e8900a)

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/365309e8-c14a-4f86-b0cc-04d7446cf58c)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/cef793e3-8eec-4f06-b7ad-c5c994048544)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/bdc13e58-8b3f-44a1-8345-8506e3f245ab)



   d) From each table with cases in the years 2016, 2017, and 2018, the top 10 states with the highest number of cases reported in each year are filtered.

   * 2016 cases against Police Personals

   ![1 add table to new table2016](https://github.com/JiJiNaK/bigdata_project/assets/144101140/1264a8b3-60ab-4e67-bd45-56fe32ff07b8)
   ![creating_dir](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a8e6c3a2-d131-4829-9582-4083b7b971ab)
   ![1 new insert table 2016 to hdfs](https://github.com/JiJiNaK/bigdata_project/assets/144101140/02fad879-a964-47f1-9e02-3a69361aef7a)

   * 2017 cases against Police Personals

   ![2 add table newtable 2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/f544dcc8-bd69-43dd-bb65-6944efb3958f)
   ![2017_dir](https://github.com/JiJiNaK/bigdata_project/assets/144101140/2d0aa425-bfeb-497d-aefe-a890c539e55a)
   ![2 new insert hdfs2017](https://github.com/JiJiNaK/bigdata_project/assets/144101140/4ffe56c6-fbd8-49a0-b22f-eada35213133)

   * 2018 cases against Police Personals

   ![3 add table 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ce05c719-980a-4797-8165-d03367d573d7)
   ![2018_dir](https://github.com/JiJiNaK/bigdata_project/assets/144101140/509cfe27-8d7b-4712-af26-1f4e7d2315fe)
   ![3 new inserthdfs 2018](https://github.com/JiJiNaK/bigdata_project/assets/144101140/80c025ed-b71c-4590-8d24-00c3d36f3bd3)

   * 2016 Escape from Police Custody

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/fecb1977-22ae-4f4e-9b5a-1f8208c8bab5)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/ff2653b8-74a2-46dd-afdd-deaf828d6e56)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3e3e4279-54d7-4ca6-a3eb-01170c5ed493)

   * 2017 Escape from Police Custody

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/18ef9cac-17be-40c0-b7b9-510fbdd6b311)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/7cc0133e-080b-49fc-b006-2d0635bf3cea)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/debbcf2c-4a6b-4951-990e-98d6f53c3544)

   * 2018 Escape from Police Custody

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/dde4d505-edca-4dbf-81f5-eee23be15a47)
   ![directory](https://github.com/JiJiNaK/bigdata_project/assets/144101140/2ed2043d-3753-4d70-bd79-c2cc9757e9b0)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/2c66d680-a5b6-4895-8505-8a7fb7603c30)

   * 2016 Victims of Rape

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/564f3301-171c-458e-97a7-0ee76585311d)
   ![directory2](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3485c9e4-cd01-4998-95f4-ddd950c9cce8)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/fd49e4dd-60d8-4735-af90-457dbab1373a)

   * 2017 Victims of Rape

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/34d9bd48-9fd3-4e91-b7f4-dd3782863ace)
   ![dir3](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a6322e8a-8e99-4f5a-8f9d-733b6b1da0bb)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3e201327-366e-44c9-bca5-028d3f9e4211)

   * 2018 Victims of Rape

   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/8b01cbd2-ff37-4d78-9043-7391712d79c9)
   ![dir4](https://github.com/JiJiNaK/bigdata_project/assets/144101140/c68461cd-7c9c-482c-bc1d-08562dff50d4)
   ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/72f4546a-8e1a-41de-9360-e5212c5af8cd)

   
   e) The result are plotted using matplotlip in pyspark.

     * The files regarding the cases against police personnel escapes from police custody,and victims of rape are mentioned above as cases.py,escapes.py and victims.py              respectively.
     * The report are given below
  
  I) To find the top 10 states/UT with the highest number of cases reported in the year 2016.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/5a480783-ba22-4e92-9355-403902f56723)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/073b744c-8958-4958-884f-505556a5b2ce)

  II) To find the top 10 states/UT with the highest number of cases reported in the year 2017.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/67dcabc4-c229-4274-b1f2-78e36a232416)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/20d73e05-715c-4759-8544-6ea22ed19b5f)

  III) To find the top 10 states/UT with the highest number of cases reported in the year 2018.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/30aa178f-6326-4ed7-aef5-cdc320142549)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/1ea261f0-4236-4709-ba91-51e056d2b140)

  IV) To find the top 10 states/UT with the highest number of cases reported in the three years (2016,2017,2018).

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/bfd5e63c-d70d-4b45-a762-d900ae49ceaa)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/94118192-0f55-44f6-8ffc-9858e0b4c22a)

  V) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2016.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/0ff438c2-9631-40bf-a075-908138709d91)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/e06c6956-1f7f-4694-8cf0-0dc6b40246d6)

  VI) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2017.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/1b6ad8f0-4b2a-4aa7-933f-a82e616bf945)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/a45b78dc-bf5c-4a9c-8986-ac67997d714c)

  VII) To find the top 10 states/UT with total number of persons escaped from police custody in the year 2018.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/6782a77d-8f6d-4050-8b4c-46dd8e97ddfe)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/c9a13d55-2c85-48f7-b823-e3a1cecece51)

  VIII) To find the top 10 states/UT with total number of persons escaped from police custody in the three years (2016,2017,2018).

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9e7267e4-0091-4199-8637-aa9275497ea0)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/eebd3669-77c6-4ede-bbdb-dc2e43360a24)

  IX) To find the top 10 states with rape victims in india top 10 states in the year 2016.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/5f936e0f-dc64-4dc6-90d6-8f940f03a310)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/9d50fca8-2604-4893-980d-d7c7852cca3f)

  X) To find the top 10 states with rape victims in india top 10 states in the year 2017.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/26938e7d-6ec2-40dd-87fa-435996a85e93)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/c0fc61e0-5714-4472-84e9-2ab0002fc358)

  XI) To find the top 10 states with rape victims in india top 10 states in the year 2018.

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/3dc7d511-bc74-4534-89f8-3049b1d02df9)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/6961c870-a50e-433d-88a7-7c9b29c03d4c)

  XII) To find the top 10 states with rape victims in india top 10 states in the three years (2016,2017,2018).

  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/d5454d61-cae3-4c10-98fc-061d18a4305d)
  ![image](https://github.com/JiJiNaK/bigdata_project/assets/144101140/18581904-1bbd-49a8-8180-2b48faa608f8)


# Conclusion

1.The top 10 States/UTs with Highest Number of Cases Reported (2016, 2017, 2018) In conclusion, our analysis has revealed the top 10 states/union territories with the highest number of reported cases over the three-year period (2016-2018). This information can aid in understanding regional trends and facilitating targeted interventions.

2.The top 10 States/UTs with Total Number of Persons Escaped from Police Custody (2016, 2017, 2018) To summarize, our investigation has identified the top 10 states/union territories with the highest number of individuals who escaped from police custody during the three-year span (2016-2018). This data may inform efforts to enhance custodial security measures.

3.The top 10 States with Rape Victims in India (2016, 2017, 2018) In summary, our research has pinpointed the top 10 states in India with the highest number of reported rape cases over the three-year period (2016-2018). This insight is crucial for addressing and advocating for measures to combat sexual violence in these regions.



















   




