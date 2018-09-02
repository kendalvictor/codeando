# !/bin/sh
. /home/jupyter/VICTOR_VILLACORTA/shellunix/set-env.sh
echo $FILE_OUT
spark2-submit \
--conf "spark.yarn.executor.memoryOverhead=512M" \
$FILE_OUT/sql_27_08_2018.py $FILE_OUT > $FILE_OUT/resultado.log
