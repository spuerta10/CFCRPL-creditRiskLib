from credit_risk_pipeline_lib.pipeline.ingest.ingest_interface import IngestInterface

from pandas import DataFrame, read_csv

class CSV(IngestInterface):
    def __init__(
            self,
            path: str,
            step_name: str = "CSV ingestion"
    ):
        # TODO: Validate the path
        self._path = path
        self._step_name = step_name
    
    def ingest(self) -> DataFrame:
        try:
            return read_csv(self._path)
        except Exception as e:
            ...
