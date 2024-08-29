from abc import abstractmethod

from credit_risk_pipeline_lib.pipeline.pipeline_step_interface import PipelineStepInterface

from pandas import DataFrame

class TransformInterface(PipelineStepInterface):
    
    @abstractmethod
    def transform(self, data: DataFrame) -> DataFrame:
        """_summary_

        Args:
            data (DataFrame): _description_

        Returns:
            DataFrame: _description_
        """
        pass