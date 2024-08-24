from abc import ABC, abstractmethod

class PipelineStepInterface(ABC):
    def __init__(self, stage_name: str):
        self._stage_name = stage_name

    @abstractmethod
    def get_step_name(self) -> str:
        """Obtains the name for a certain Pipeline step.

        Returns:
            str: The name of the pipeline step.
        """
        return self._stage_name