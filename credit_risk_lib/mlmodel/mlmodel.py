from credit_risk_lib.mlmodel.conf_validator import ConfValidator
from credit_risk_lib.config.config import Config

from pydantic import BaseModel
import mlflow
from mlflow.exceptions import MlflowException
from pandas import DataFrame
from numpy import ndarray


class MLModel(ConfValidator):
    def __init__(self, model_conf: str | Config, model_conf_schema: None | BaseModel = None):
        """Instance to retrieve a specified model from MLFlow. 

        Args:
            model_conf_path (str): The absolute or relative path to JSON config file.
            model_conf_schema (None | BaseModel, optional): A pydantic class to validate that the content of a config file follows a given schema. 
            Defaults to None.
        """
        super().__init__(model_conf, model_conf_schema)
    
    
    def fetch(
        self,
        mlmodel_name_attribute: str,
        mlmodel_version_or_alias_attribute: str
    ) -> 'MLModel':
        """Retrieves a model from MLFlow server given the name and version or alias of the model.
        Can retrieve the model either from specified version or alias.

        Args:
            mlmodel_name_attribute (str): Name of the field in config file where the model name is registered.
            mlmodel_version_or_alias_attribute (str): Name of the field in config file where the model version or alias is registered. 

        Raises:
            AttributeError: If the searched model name is not found in the config file.
            AttributeError: If the searched model version or alias is not found in the config file.
            ValueError: If the model name in the config file is not a string.
            ValueError: If the model version is not int or model alias is not string found in the config file.
            ValueError: If the model can't be loaded from MLFlow.

        Returns:
            Model: The object with the MLFlow model loaded inside .model attribute. 
        """
        if not hasattr(self._conf, mlmodel_name_attribute):
            raise AttributeError(f"ML model name attribute {mlmodel_name_attribute} not found on configs.")
        if not hasattr(self._conf, mlmodel_version_or_alias_attribute):
            raise AttributeError(f"ML model attribute {mlmodel_version_or_alias_attribute} not found on configs.")
        model_name_attribute: str = getattr(self._conf, mlmodel_name_attribute)
        fetch_attribute: int | str = getattr(self._conf, mlmodel_version_or_alias_attribute)
        if not isinstance(model_name_attribute, str):
            raise ValueError(f"{model_name_attribute} attribute must be str")
        if not isinstance(fetch_attribute, (int, str)):
            raise ValueError(f"{mlmodel_version_or_alias_attribute} attribute must be str (model alias) or int (model version).")
        version_or_alias: str = f"/{fetch_attribute}" if isinstance(fetch_attribute, int) else f"@{fetch_attribute}"  
        fetch_path = f"models:/{model_name_attribute}" + version_or_alias
        try:
            model = mlflow.pyfunc.load_model(fetch_path)
            setattr(self, "model", model)
        except MlflowException as e:
            raise ValueError(f"Unable to load model from path: {fetch_path}")
        return self
    
    
    def predict(self, data: DataFrame) -> ndarray:
        return self.model.predict(data)