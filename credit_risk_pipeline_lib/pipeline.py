from credit_risk_pipeline_lib.ingest.ingest_interface import IngestInterface
from credit_risk_pipeline_lib.transform.transform_interface import TransformInterface
from credit_risk_pipeline_lib.load.load_interface import LoadInterface
from credit_risk_pipeline_lib.pipeline_step_interface import PipelineStepInterface

from typeguard import typechecked
from pandas import DataFrame


class Pipeline:
    @typechecked
    def __init__(
            self, 
            ingest_stage: IngestInterface,
            transform_stage: TransformInterface | None = None,  # maybe I dont want to transform the data
            load_stage: LoadInterface | None = None,  # maybe I dont want to load the data
    ):
        self._ingest_stage = ingest_stage
        self._transform_stage = transform_stage
        self._load_stage = load_stage
        self._steps: list[PipelineStepInterface | None] = [self._ingest_stage, self._transform_stage, self._load_stage]

    
    def run(self):
        """
        Executes the defined Pipeline object.
        """
        ingested_data: DataFrame = self._ingest_stage.ingest()
        transformed_data: DataFrame = self._transform_stage.transform(ingested_data) \
            if self._transform_stage is not None else None
        if self._load_stage is not None:
            load_data: DataFrame = self._load_stage.load(transformed_data) \
                if transformed_data is not None else self._load_stage.load(ingested_data)
            
    
    def __str__(self) -> str:
        """Returns a String representation of Pipeline object.

        Returns:
            str: Representation of Pipeline object.
        """
        pipeline_representation = ""
        for step in self._steps:
            pipeline_representation += f"|-- {step.get_step_name()}" \
                if step is not None else ""
        return pipeline_representation