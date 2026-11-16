# ---- file: modules/plugin_manager/plugin_view.py ----
import flet as ft
from modules.plugin_manager.plugin_logic import PluginLogic

class PluginView(ft.Row):
    def __init__(self, logic: PluginLogic) -> None:
        super().__init__(expand=True, spacing=20)
        self.logic = logic
        self.logic.on_change = self.render

        # 1. Inisialisasi atribut text status terlebih dahulu (Tanpa walrus :=)
        self.status_text = ft.Text("", size=12, color=ft.Colors.GREEN, weight=ft.FontWeight.W_500)

        # Kontainer Daftar Modul (Panel Kanan/Utama)
        self.plugin_list_column = ft.Column(expand=True, spacing=15, scroll=ft.ScrollMode.AUTO)

        # Panel Kiri: Informasi / Pengaturan Plugin Manager
        left_panel = ft.Container(
            expand=1,
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            padding=20,
            border=ft.Border.all(1, ft.Colors.GREY_300),
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.EXTENSION, color=ft.Colors.BLUE, size=24),
                    ft.Text("Plugin Manager", size=18, weight=ft.FontWeight.BOLD),
                ], spacing=10),
                ft.Divider(),
                ft.Text(
                    "Kelola ekstensi dan modul tambahan untuk memperluas fungsionalitas sistem ERP Anda. "
                    "Modul yang di-install akan otomatis menambahkan menu ke sidebar utama.",
                    size=12,
                    color=ft.Colors.GREY_700
                ),
                ft.Container(height=10),
                self.status_text # 2. Gunakan atribut yang sudah dideklarasikan di sini
            ])
        )

        # Panel Kanan: List Card Plugin
        right_panel = ft.Container(
            expand=2,
            bgcolor=ft.Colors.WHITE,
            border_radius=8,
            padding=20,
            border=ft.Border.all(1, ft.Colors.GREY_300),
            content=self.plugin_list_column
        )

        self.controls = [left_panel, right_panel]
        self.render()

    def render(self) -> None:
        # Update teks status
        self.status_text.value = self.logic.state.status_message

        # Buat ulang daftar card plugin berdasarkan state
        cards = []
        for plugin in self.logic.state.available_plugins:
            is_installed = plugin["is_installed"]
            
            action_button = ft.Button(
                content="Uninstall" if is_installed else "Install",
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.RED_400 if is_installed else ft.Colors.GREEN_400,
                icon=ft.Icons.DELETE if is_installed else ft.Icons.DOWNLOAD,
                on_click=lambda _, pid=plugin["id"], inst=is_installed: 
                    self.logic.uninstall_plugin(pid) if inst else self.logic.install_plugin(pid)
            )

            card = ft.Container(
                bgcolor=ft.Colors.GREY_50,
                padding=15,
                border_radius=8,
                border=ft.Border.all(1, ft.Colors.GREY_300),
                content=ft.Row([
                    ft.Column([
                        ft.Row([
                            ft.Text(plugin["name"], size=14, weight=ft.FontWeight.BOLD),
                            ft.Container(
                                content=ft.Text(f"v{plugin['version']}", size=10, color=ft.Colors.BLUE_900),
                                bgcolor=ft.Colors.BLUE_50,
                                padding=ft.Padding.symmetric(horizontal=6, vertical=2),
                                border_radius=4
                            )
                        ], spacing=10),
                        ft.Text(plugin["description"], size=12, color=ft.Colors.GREY_600),
                    ], expand=True, spacing=5),
                    action_button
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
            cards.append(card)

        self.plugin_list_column.controls = [
            ft.Text("Daftar Modul Tersedia", size=16, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            *cards
        ]

        try:
            self.update()
        except RuntimeError:
            pass