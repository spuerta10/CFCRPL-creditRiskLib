from credit_risk_pipeline_lib.ingest.ingest_interface import IngestInterface

class CloudEvent(IngestInterface):
    def __init__(
            self,
            cloud_event: ...
    ):
        ...