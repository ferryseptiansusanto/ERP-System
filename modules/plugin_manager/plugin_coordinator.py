# ---- file: modules/plugin_manager/plugin_coordinator.py ----
import flet as ft
from core.base_module import BaseModule
from modules.plugin_manager.plugin_state import PluginState
from modules.plugin_manager.plugin_logic import PluginLogic
from modules.plugin_manager.plugin_view import PluginView

class PluginCoordinator(BaseModule):
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.state = PluginState()
        self.logic = PluginLogic(state=self.state)
        self.view = PluginView(logic=self.logic)

    @property
    def module_id(self) -> str:
        return "plugin_manager"

    @property
    def title(self) -> str:
        return "Plugin Manager"

    @property
    def icon(self) -> ft.Icons:
        return ft.Icons.EXTENSION

    def get_main_view(self) -> ft.Control:
        return self.view