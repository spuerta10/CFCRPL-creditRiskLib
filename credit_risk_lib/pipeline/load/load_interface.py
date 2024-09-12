from abc import abstractmethod

from credit_risk_lib.pipeline.pipeline_step_interface import PipelineStepInterface

from pandas import DataFrame


class LoadInterface(PipelineStepInterface):
    @abstractmethod
    def load(data: DataFrame):
        """Loads given data to a certain source

        Args:
            data (DataFrame): Data to be loaded into a source.
        """
        pass