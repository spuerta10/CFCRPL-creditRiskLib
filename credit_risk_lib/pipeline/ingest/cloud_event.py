from base64 import b64decode

from credit_risk_lib.pipeline.ingest.ingest_interface import IngestInterface

from cloudevents.http import CloudEvent
from pandas import DataFrame


class CloudEventV1(IngestInterface):
    def __init__(
            self,
            cloud_event: CloudEvent,
            step_name: str = "Cloud Event v1 ingestion"
    ):
        self._cloud_event = cloud_event
        self._step_name = step_name


    def ingest(self) -> DataFrame:
        """Ingests a Cloud Functions v1 event.

        Returns:
            DataFrame: The cloud event data transformed to DataFrame.
        """
        try:
            pubsub_msg: dict = b64decode(self._cloud_event.data["message"]["data"]).decode()
            ingested_data = DataFrame(pubsub_msg)
            return ingested_data 
        except Exception as e:
            ...


class CloudEventV2(IngestInterface):
    """
    Future implementation of ingestion of a V2 cloud event.
    """
    pass