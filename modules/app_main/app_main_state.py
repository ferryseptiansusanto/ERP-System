# ---- file: modules/app_main/app_main_state.py ----
from typing import List, Any

class AppMainState:
    def __init__(self) -> None:
        self.active_nav_index: int = 0
        self.installed_modules: List[Any] = []