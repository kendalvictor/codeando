
# coding: utf-8

# In[1]:


import findspark
findspark.init('/opt/cloudera/parcels/SPARK2-2.3.0.cloudera3-1.cdh5.13.3.p0.458809/lib/spark2')
##findspark.init("/home/ubuntu/spark-2.2.1-bin-hadoop2.7")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('KENDVIC_27_08_2018').getOrCreate()


# In[2]:


spark.sql("show tables from default").show()


# In[3]:


df_csv = spark.read.csv('/user/grupo_3/villacorta/csv/2015-summary.csv', inferSchema=True, header=True)
df_csv.show()


# In[4]:


df_csv.createOrReplaceTempView('kendal_table')


# In[6]:


df3 = spark.sql("""
    select DEST_COUNTRY_NAME, count(1) as cantidad
    from kendal_table
    group by DEST_COUNTRY_NAME
""")
df3.show()


# In[8]:


df3.write.format('csv').mode('OVERWRITE').option('sep', '|').save('/user/grupo_3/villacorta/dataset')


# In[9]:


get_ipython().system(u'hdfs dfs -ls /user/grupo_3/villacorta/')

