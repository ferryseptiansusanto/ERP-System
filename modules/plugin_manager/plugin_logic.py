# ---- file: modules/plugin_manager/plugin_logic.py ----
from typing import Callable, Optional
from modules.plugin_manager.plugin_state import PluginState

class PluginLogic:
    def __init__(self, state: PluginState) -> None:
        self.state = state
        self.on_change: Optional[Callable[[], None]] = None

    def install_plugin(self, plugin_id: str) -> None:
        """Simulasi proses instalasi modul"""
        for plugin in self.state.available_plugins:
            if plugin["id"] == plugin_id:
                plugin["is_installed"] = True
                self.state.status_message = f"Berhasil meng-install modul: {plugin['name']}"
                break
        self._notify_change()

    def uninstall_plugin(self, plugin_id: str) -> None:
        """Simulasi proses uninstalasi modul"""
        for plugin in self.state.available_plugins:
            if plugin["id"] == plugin_id:
                plugin["is_installed"] = False
                self.state.status_message = f"Berhasil menghapus modul: {plugin['name']}"
                break
        self._notify_change()

    def _notify_change(self) -> None:
        if self.on_change:
            self.on_change()