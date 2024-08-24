from abc import abstractmethod

from pipeline_step_interface import PipelineStepInterface

from pandas import DataFrame

class IngestInterface(PipelineStepInterface):

    def ingest(self) -> DataFrame:
        """Ingest data from a source, returns the ingested data in Dataframe.

        Returns:
            DataFrame: Ingested data from source. 
        """
        pass