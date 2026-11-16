# ---- file: layout.py ----
import flet as ft

def layout_top():
    # 1. Header Bagian Atas
    top_header = ft.Container(
        bgcolor="#1A1C23",
        padding=ft.Padding.symmetric(horizontal=15, vertical=8),
        content=ft.Row([
            ft.Row([
                ft.Icon(ft.Icons.ALL_INCLUSIVE, color=ft.Colors.WHITE, size=24),
                ft.Text("accurate", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text("online", size=12, color=ft.Colors.GREEN_ACCENT, weight=ft.FontWeight.BOLD),
            ], spacing=2),
            ft.Row([
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE_70, icon_size=18),
                ft.IconButton(icon=ft.Icons.HELP_OUTLINE, icon_color=ft.Colors.WHITE_70, icon_size=18),
                ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.WHITE_70, icon_size=18),
                ft.Container(
                    bgcolor="#374151",
                    padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                    border_radius=15,
                    content=ft.Row([
                        ft.CircleAvatar(content=ft.Text("GM"), radius=12, bgcolor=ft.Colors.BLUE),
                        ft.Text("CV Mitra Spesialis", color=ft.Colors.WHITE, size=12, weight=ft.FontWeight.W_500),
                    ], spacing=8)
                )
            ], spacing=5)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    return top_header

def layout_header():
    # 2. Sub-Header Tab Bar
    tab_header = ft.Container(
        bgcolor="#FFFFFF",
        padding=ft.Padding.symmetric(horizontal=15, vertical=8),
        border=ft.Border.only(bottom=ft.border.BorderSide(1, ft.Colors.GREY_300)),
        content=ft.Row([
            ft.Row([
                ft.TextButton(content=ft.Text("Dashboard", color=ft.Colors.GREY_700, size=13)),
                ft.Container(
                    bgcolor=ft.Colors.PINK_ACCENT,
                    padding=ft.Padding.symmetric(horizontal=12, vertical=6),
                    border_radius=4,
                    content=ft.Text("Persiapan Data Perusahaan", color=ft.Colors.WHITE, size=12, weight=ft.FontWeight.BOLD)
                )
            ], spacing=10)
        ])
    )

    return tab_header

def left_panel():
    # 3. Konten Panel Kiri (Ilustrasi / Sambutan)
    left_panel = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=8,
        padding=20,
        expand=1,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    height=200,
                    alignment=ft.alignment.Alignment(0, 0),
                    content=ft.Column([
                        ft.Icon(ft.Icons.AUTO_GRAPH, size=70, color=ft.Colors.PINK_300),
                        ft.Text("Area Ilustrasi / Grafik", size=14, color=ft.Colors.GREY_600, weight=ft.FontWeight.W_500)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),
                ft.Column([
                    ft.Text("Selamat Datang di Aplikasi", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK_87),
                    ft.Container(height=8),
                    ft.Text(
                        "Area ini digunakan untuk menampilkan informasi ringkas, panduan, "
                        "atau deskripsi modul yang sedang aktif di sebelah kanan.",
                        size=12,
                        color=ft.Colors.GREY_700,
                        text_align=ft.TextAlign.CENTER
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Row([
                    ft.Button(content=ft.Text("Tombol Aksi 1", size=12), bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, expand=True),
                    ft.Button(content=ft.Text("Tombol Aksi 2", size=12), bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE, expand=True),
                ], spacing=10)
            ]
        )
    )

    return left_panel

def right_panel():
    # 4. Konten Panel Kanan (Area Kotak-kotak / List Layout)
    right_panel = ft.Container(
        bgcolor=ft.Colors.WHITE,
        border_radius=8,
        padding=20,
        expand=1,
        border=ft.Border.all(1, ft.Colors.GREY_300),
        content=ft.Column([
            ft.Text("Area Daftar / Konten Utama", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK_87),
            ft.Divider(height=15),
            ft.Column(
                expand=True,
                spacing=10,
                controls=[
                    ft.Container(bgcolor=ft.Colors.GREY_100, padding=15, border_radius=6, content=ft.Text("Baris Konten 1", color=ft.Colors.BLACK_87)),
                    ft.Container(bgcolor=ft.Colors.GREY_100, padding=15, border_radius=6, content=ft.Text("Baris Konten 2", color=ft.Colors.BLACK_87)),
                    ft.Container(bgcolor=ft.Colors.GREY_100, padding=15, border_radius=6, content=ft.Text("Baris Konten 3", color=ft.Colors.BLACK_87)),
                ]
            )
        ])
    )

    return right_panel

def layout_body(sidebar: ft.Control, dynamic_content: ft.Control) -> ft.Control:
    # 5. Body Utama (Sidebar Kiri & Konten Tengah)
    body_content = ft.Row(
        expand=True,
        spacing=0,
        controls=[
            # Sidebar Kiri (Ikon Navigasi Vertikal)
            sidebar,
            ft.VerticalDivider(width=1),
            # Area Konten Utama yang dibagi menjadi 2 Kolom (Kiri & Kanan)
            ft.Container(
                expand=True,
                bgcolor="#F4F5F7",
                padding=20,
                content=dynamic_content
            )
        ]
    )

    return body_content