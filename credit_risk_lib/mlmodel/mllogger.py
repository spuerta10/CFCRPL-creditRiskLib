from typing import Any
from credit_risk_lib.mlmodel.conf_validator import ConfValidator
from credit_risk_lib.config.config import Config

from pydantic import BaseModel
import mlflow


class MLLogger(ConfValidator):
    
    allowed_logging_methods = {
        "log_param",
        "log_artifact",
        "log_metric"
    }
    
    def __init__(self, model_conf: str | Config, model_conf_schema: None | BaseModel = None) -> None:
        super().__init__(model_conf, model_conf_schema)
        
    
    def __getattr__(self, attribute):
        if attribute in self.allowed_logging_methods:
            return getattr(mlflow, attribute)
        raise AttributeError(f"MLLogger object has no attribute '{attribute}'")