import numpy as np
from sklearn.linear_model import LogisticRegression
import mlflow
import os

if __name__ == "__main__":

    # 环境准备--->>>模型准备&训练--->>>tracking

    # 1、prepare for environment
    # 1.1、oss
    os.environ['AWS_ACCESS_KEY_ID'] = "admin"
    os.environ['AWS_SECRET_ACCESS_KEY'] = "admin123456"
    os.environ['AWS_DEFAULT_REGION'] = "us-east-1"
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://localhost:19000"

    # 2、oss
    remote_server_uri = "http://localhost:15002"
    experiment_name = "test_exp"

    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(experiment_name)

    # 2、prepare for data
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])

    # 3、initialize & fit model
    lr = LogisticRegression()
    lr.fit(X, y)

    # 4、log
    score = lr.score(X, y)
    try:
        mlflow.log_metric("score", score)
        mlflow.sklearn.log_model(lr, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    except:
        # todo
        raise