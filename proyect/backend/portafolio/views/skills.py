import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.components.barporgress import bar_progress
from portafolio.data import Info
from portafolio.styles.styles import Size


def myskills(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        bar_progress("Python 60%", 60),
        bar_progress("C++ 30%", 30),
        bar_progress("Rust 20%", 20),
        bar_progress("Linux 40%", 40),
        width="100%",
    )
