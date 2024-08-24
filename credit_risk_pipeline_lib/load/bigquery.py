from copy import deepcopy

from credit_risk_pipeline_lib.load.load_interface import LoadInterface

from pandas import DataFrame

class BigQuery(LoadInterface):
    def __init__(
            self,
            gcp_project_id: str,
            gcp_bq_table_name: str, 
            stage_name: str = "BigQuery Load"
    ):
        self._gcp_project_id = gcp_project_id
        self._gcp_bq_table_name = gcp_bq_table_name
        self._stage_name = stage_name

    def load(self, load_data: DataFrame):
        try:
            load_data: DataFrame = deepcopy(load_data)
        except Exception as e:
            ...