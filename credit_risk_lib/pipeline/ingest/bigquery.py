from credit_risk_lib.pipeline.ingest.ingest_interface import IngestInterface

from google.cloud.bigquery import Client
from google.cloud.bigquery.job import QueryJob
from pandas import DataFrame


class BigQuery(IngestInterface):
    def __init__(
        self,
        client: Client = Client(),  # if not given let's try to init the BQ Client
        sql_query: None | str = None,
        gcp_project_id: None | str = None,
        step_name: str = "BigQuery ingestion"
    ):
        self._client: Client = client
        self._sql_query = sql_query
        self._gcp_project_id = gcp_project_id
        self._step_name = step_name
        
        
    @property
    def sql_query(self):
        return self.sql_query
        
        
    @sql_query.setter
    def sql_query(self, new_sql_query: str):
        self._sql_query = new_sql_query
    
    
    def ingest(self) -> DataFrame:
        if self._sql_query is None:
            raise ValueError("SQL query not found, please provide one!")
        ingested_data: QueryJob = self._client.query(self._sql_query) if self._gcp_project_id is None \
            else self._client.query(self._sql_query, project=self._gcp_project_id)
        return ingested_data.to_dataframe()
         