# 测试脚本
python3 test-script.py
# 设置数据库&OSS
python3 set-oss.py
python3 set-mysql.py


# 启动mlflow trancking server
mlflow server --backend-store-uri \
       mysql+pymysql://root:123456@mysql-host:3306/mlflow_test \
       --host 0.0.0.0 -p 5002 \
       --default-artifact-root s3://mlflow-bucket/