# ---- file: modules/app_main/app_main_coordinator.py ----
from typing import List, Any
import flet as ft
from modules.app_main.app_main_state import AppMainState
from modules.app_main.app_main_logic import AppMainLogic
from modules.app_main.app_main_view import AppMainView

from modules.plugin_manager.plugin_coordinator import PluginCoordinator

class AppMainCoordinator:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

        # 1. Inisialisasi State & Logic
        self.state = AppMainState()
        self.logic = AppMainLogic(state=self.state)

        # 2. Muat Daftar Modul yang Ter-install (Plugin Registry Loader)
        self.installed_modules: List[Any] = []
        self._load_installed_modules()

        # Simpan ke state
        self.logic.set_installed_modules(self.installed_modules)

        # 3. Inisialisasi View Utama
        self.view = AppMainView(
            page=self.page,                    
            logic=self.logic, 
            view_provider=self._get_module_view,
            modules=self.installed_modules
        )
        
        self.logic.on_change = self.view.render

        # 4. Masukkan ke halaman utama Flet
        self.page.add(self.get_view())

    def _load_installed_modules(self) -> None:
        """
        Tempat memuat modul yang aktif. 
        Nantinya bagian ini bisa membaca dari file konfigurasi JSON / database lokal.
        """
        # Contoh pendaftaran modul dasar:
        # self.installed_modules.append(UserManagementCoordinator(page=self.page))
        # self.installed_modules.append(PluginManagerCoordinator(page=self.page))
        
        # Contoh pendaftaran modul fungsional:
        #self.installed_modules.append(AccountingCoordinator(page=self.page))
        self.installed_modules.append(PluginCoordinator(page=self.page))

    def _get_module_view(self, index: int) -> ft.Control:
        """Mengembalikan view dari modul berdasarkan indeks navigasi aktif."""
        if 0 <= index < len(self.installed_modules):
            return self.installed_modules[index].get_main_view()
        
        return ft.Container(
            content=ft.Text("Modul tidak ditemukan", size=16, italic=True),
            alignment=ft.Alignment.CENTER
        )

    def get_view(self) -> ft.Control:
        self.view.render()
        return self.view