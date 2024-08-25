from abc import ABC

class PipelineStepInterface(ABC):
    def __init__(self, step_name: str):
        self._step_name = step_name


    def get_step_name(self) -> str:
        """Obtains the name for a certain Pipeline step.

        Returns:
            str: The name of the pipeline step.
        """
        return self._step_name