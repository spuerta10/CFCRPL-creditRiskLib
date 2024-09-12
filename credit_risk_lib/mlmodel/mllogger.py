from credit_risk_lib.mlmodel.conf_validator import ConfValidator
from credit_risk_lib.config.config import Config

from pydantic import BaseModel
import mlflow


class MLLogger(ConfValidator):
    def __init__(self, model_conf: str | Config, model_conf_schema: None | BaseModel = None) -> None:
        super().__init__(model_conf, model_conf_schema)
        
    
    def log_param(self, *args):
        mlflow.log_param(args)
    
    
    def log_artifact(self, *args):
        mlflow.log_artifact(args)
        
    
    def log_metric(self, *args):
        mlflow.log_metric(args)