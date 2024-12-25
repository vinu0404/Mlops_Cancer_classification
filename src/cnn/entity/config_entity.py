from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_urls:str
    local_data:Path
    unzip_dir:Path