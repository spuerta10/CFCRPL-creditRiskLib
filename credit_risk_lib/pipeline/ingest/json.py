from pathlib import Path
from os.path import abspath

from credit_risk_lib.pipeline.ingest.ingest_interface import IngestInterface

from pandas import DataFrame, read_json


class JSON(IngestInterface):
    def __init__(self, content: str | dict):
        if isinstance(content, str) and not Path(content).exists():
            raise ValueError("")
        self._content = content
    
    
    def ingest(self) -> DataFrame:
        # for now the JSON passed must be plain
        try:
            data: DataFrame = read_json(abspath(self._content), index=[0]) \
                if isinstance(self._content, str) else DataFrame(self._content, index=[0])
            return data
        except Exception as e:
            raise ValueError("")
    
    