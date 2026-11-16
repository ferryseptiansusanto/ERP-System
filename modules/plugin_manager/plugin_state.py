# ---- file: modules/plugin_manager/plugin_state.py ----
from typing import Dict, List, Any

class PluginState:
    def __init__(self) -> None:
        # Daftar semua modul yang tersedia di sistem beserta status is_installed-nya
        self.available_plugins: List[Dict[str, Any]] = [
            {
                "id": "accounting",
                "name": "Accounting & Finance",
                "description": "Modul akuntansi lengkap dengan COA dan Jurnal Umum.",
                "version": "1.0.0",
                "is_installed": True
            },
            {
                "id": "inventory",
                "name": "Inventory Management",
                "description": "Pengelolaan stok barang, gudang, dan mutasi barang.",
                "version": "1.1.0",
                "is_installed": False
            },
            {
                "id": "pos",
                "name": "Point of Sales (POS)",
                "description": "Modul kasir dan penjualan ritel cepat.",
                "version": "2.0.0",
                "is_installed": False
            }
        ]
        self.status_message: str = ""