# ---- file: core/base_module.py ----
import flet as ft
from abc import ABC, abstractmethod

class BaseModule(ABC):
    
    @property
    @abstractmethod
    def module_id(self) -> str:
        """ID unik untuk modul, contoh: 'accounting' atau 'pos'"""
        pass

    @property
    @abstractmethod
    def title(self) -> str:
        """Nama yang akan tampil sebagai tooltip/label di sidebar"""
        pass

    @property
    @abstractmethod
    def icon(self) -> ft.Icons:
        """Ikon Flet yang akan otomatis dipasang di sidebar utama"""
        pass

    @abstractmethod
    def get_main_view(self) -> ft.Control:
        """Fungsi yang mengembalikan tampilan utama (UI) dari modul tersebut"""
        pass