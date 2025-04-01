from typing import List

from zero_to_one_hundred.src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from zero_to_one_hundred.src.zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.src.zero_to_one_hundred.models.section import Section
from zero_to_one_hundred.src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_process_fs import (
    ZTOHProcessFS,
)
from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator


class RefreshSectionContentsProcessor(AProcessor):
    """RefreshSectionContentsProcessor"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        process_fs: ZTOHProcessFS,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan sections an update links."""
        sections: List[Section] = Map.build_from_dirs(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.persist_fs.list_dirs(self.config_map.get_repo_path),
        )
        for s in sections:
            try:
                s.look_for_materialized_https()
                s.delete_orphan_images()
            except Exception as e:
                Validator.print_e(e)
