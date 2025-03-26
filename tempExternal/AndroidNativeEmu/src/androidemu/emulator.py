import logging
from unicorn import Uc, UC_ARCH_ARM, UC_MODE_ARM

logger = logging.getLogger(__name__)

class Emulator:
     def __init__(self, vfs_root: str = None, vfp_inst_set: bool = False):
        # Unicorn.
        self.uc = Uc(UC_ARCH_ARM, UC_MODE_ARM)
        if vfp_inst_set:
            self._enable_vfp()