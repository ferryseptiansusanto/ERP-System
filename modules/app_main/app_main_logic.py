# ---- file: modules/app_main/app_main_logic.py ----
from typing import Callable, Optional, List, Any
from modules.app_main.app_main_state import AppMainState

class AppMainLogic:
    def __init__(self, state: AppMainState) -> None:
        self.state = state
        self.on_change: Optional[Callable[[], None]] = None

    def set_nav_index(self, index: int) -> None:
        if self.state.active_nav_index != index:
            self.state.active_nav_index = index
            self._notify_change()

    def set_installed_modules(self, modules: List[Any]) -> None:
        self.state.installed_modules = modules
        self._notify_change()

    def _notify_change(self) -> None:
        if self.on_change:
            self.on_change()