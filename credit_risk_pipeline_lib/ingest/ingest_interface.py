from abc import abstractmethod

from credit_risk_pipeline_lib.pipeline_step_interface import PipelineStepInterface

from pandas import DataFrame

class IngestInterface(PipelineStepInterface):

    @abstractmethod
    def ingest(self) -> DataFrame:
        """Ingest data from a source, returns the ingested data in Dataframe.

        Returns:
            DataFrame: Ingested data from source. 
        """
        pass