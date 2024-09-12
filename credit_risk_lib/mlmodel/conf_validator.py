from credit_risk_lib.config.config import Config
from credit_risk_lib.config.config_factory import ConfigFactory

from pydantic import BaseModel
import mlflow
from mlflow.exceptions import MlflowException


class ConfValidator:
    def __init__(self, model_conf_path: str, model_conf_schema: None | BaseModel = None):
        """Instance to retrieve a specified model from MLFlow. 

        Args:
            model_conf_path (str): The absolute or relative path to JSON config file.
            model_conf_schema (None | BaseModel, optional): A pydantic class to validate that the content of a config file follows a given schema. 
            Defaults to None.
        Raises:
            ValueError: If mlflow_ip field is not present in config file.
            ValueError: If mlflow_ip field is not str type.
        """
        self._conf: Config = ConfigFactory.get_conf(model_conf_path, model_conf_schema)
        if not hasattr(self._conf, "mlflow_ip"):  # force that mlflow_ip is present in config file
            raise ValueError("mlflow_ip field must be in conf and was not found.")
        if not isinstance(getattr(self._conf, "mlflow_ip"), str):  # force that mlflow_ip is str type.
            raise ValueError("mlflow_ip field must be type str.")
        try:
            mlflow.set_tracking_uri(self._conf.mlflow_ip)
        except MlflowException:
            raise ValueError(f"Unable to connect to MLFlow remote server: {self._conf.mlflow_ip}")