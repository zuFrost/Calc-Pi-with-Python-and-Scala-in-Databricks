# Databricks notebook source
# MAGIC %md This notebook uses Python

# COMMAND ----------

from random import random 
def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0
  
NUM_SAMPLES = 1000000 # Increment by 10x 
count = sc.parallelize(range(0,NUM_SAMPLES)).map(sample)\
             .reduce(lambda a, b: a + b)
print ("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))

# COMMAND ----------

# MAGIC %md Using Scala

# COMMAND ----------

# MAGIC %scala 
# MAGIC val NUM_SAMPLES = 10000000   //increment by 10x, i.e. 10, 100 and view Spark Jobs
# MAGIC val count = sc.parallelize(1 to NUM_SAMPLES).map{i =>
# MAGIC   val x = Math.random()
# MAGIC   val y = Math.random()
# MAGIC   if (x*x + y*y < 1) 1 else 0
# MAGIC }.reduce(_ + _)
# MAGIC println("Pi is roughly " + 4.0 * count / NUM_SAMPLES)
