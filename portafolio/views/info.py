import reflex as rx

from portafolio.components.heading import heading
from portafolio.components.info_detail import info_detail
from portafolio.styles.styles import Size


def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
