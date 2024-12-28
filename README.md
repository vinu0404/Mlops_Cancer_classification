# Mlops_Cancer_classification
Full Production Level Machine Learning Pipeline for Cancer Classification

## Workflows:

1.Update config.yaml
2.Update params.yaml
3.Update the entity
5.Update the configuration manager in src/config(First read param and config file in constant folder)
6.Update the components
7.Update the pipeline
8.Update the main.py
9.Update the dvc.yaml



## Credential for DAGSHUB:

```import dagshub
dagshub.init(repo_owner='vinu0404', repo_name='Mlops_Cancer_classification', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)```