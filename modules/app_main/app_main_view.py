# ---- file: modules/app_main/app_main_view.py ----
import flet as ft
from typing import Callable, List, Any
from modules.app_main.app_main_logic import AppMainLogic
from modules.app_main.layout import layout_top, layout_header

class AppMainView(ft.Column):
    def __init__(
        self, 
        page: ft.Page, 
        logic: AppMainLogic, 
        view_provider: Callable[[int], ft.Control],
        modules: List[Any]
    ) -> None:
        self.page_ref = page
        self.logic = logic
        self.view_provider = view_provider
        self.modules = modules

        # 1. Kontainer untuk dynamic content modul anak
        self.dynamic_content_container = ft.Container(
            expand=True,
            content=ft.Text("Pilih menu di samping", size=14, color=ft.Colors.GREY_600)
        )

        # 2. Sidebar Navigasi Dinamis Berdasarkan Modul Ter-install
        sidebar_controls = []
        for index, mod in enumerate(self.modules):
            is_active = (self.logic.state.active_nav_index == index)
            btn = ft.IconButton(
                icon=mod.icon,
                icon_color=ft.Colors.WHITE if is_active else ft.Colors.WHITE_70,
                tooltip=mod.title,
                on_click=lambda _, idx=index: self.logic.set_nav_index(idx)
            )
            sidebar_controls.append(btn)

        self.sidebar = ft.Container(
            bgcolor="#1A1C23",
            width=60,
            padding=ft.Padding.symmetric(vertical=10),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=sidebar_controls
            )
        )

        # 3. Body Utama (Sidebar Kiri & Konten Kanan)
        body_content = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                self.sidebar,
                ft.VerticalDivider(width=1),
                ft.Container(
                    expand=True,
                    bgcolor="#F4F5F7",
                    padding=20,
                    content=self.dynamic_content_container
                )
            ]
        )

        # 4. Rakit Layout Lengkap
        top_header = layout_top()
        tab_header = layout_header()

        super().__init__(
            expand=True,
            spacing=0,
            controls=[
                top_header,
                tab_header,
                body_content,
            ],
        )

    def render(self) -> None:
        # Update warna ikon sidebar yang aktif secara visual
        for index, control in enumerate(self.sidebar.content.controls):
            if isinstance(control, ft.IconButton):
                is_active = (self.logic.state.active_nav_index == index)
                control.icon_color = ft.Colors.WHITE if is_active else ft.Colors.WHITE_70

        # Ambil view dari modul anak yang sedang dipilih
        self.dynamic_content_container.content = self.view_provider(self.logic.state.active_nav_index)
        
        try:
            self.update()
            self.page_ref.update()
        except RuntimeError:
            pass