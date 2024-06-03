import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import AVATAR_HEIGHT, BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size


def navbar() -> rx.Component:
    return rx.hstack(
        # rx.spacer(),
        rx.color_mode.button(
            rx.color_mode.icon(),
            position="absolute", 
            top="10px", right="5px",
        ),
    )
