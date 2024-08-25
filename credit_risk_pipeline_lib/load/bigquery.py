from copy import deepcopy

#from credit_risk_pipeline_lib.load.load_interface import LoadInterface

from pandas import DataFrame
from pandas_gbq import to_gbq

class BigQuery():
    def __init__(
            self,
            gcp_project_id: str,
            gcp_bq_table_id: str, 
            stage_name: str = "BigQuery Load"
    ):
        """Load Step to Google BigQuery.

        Args:
            gcp_project_id (str): The GCP project ID where the BigQuery table is alocated.
            gcp_bq_table_name (str): The ID of the BigQuery table to load the data.
            stage_name (str, optional): Name of the current stage to be displayed in the pipeline info. Defaults to "BigQuery Load".
        """
        self._gcp_project_id = gcp_project_id
        self._gcp_bq_table_id = gcp_bq_table_id
        self._stage_name = stage_name

    def load(self, load_data: DataFrame):
        """Loads a given DataFrame to Google Big Query

        Args:
            load_data (DataFrame): DataFrame to load to GBQ.
        """
        try:
            to_gbq(
                deepcopy(load_data),
                self._gcp_bq_table_id,
                project_id=self._gcp_project_id
            )
        except Exception as e:
            ...