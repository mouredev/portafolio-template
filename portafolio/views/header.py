import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.media import media
from portafolio.data import Data
from portafolio.styles.styles import AVATAR_HEIGHT, BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size


def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.mobile_only(
            rx.flex(
                rx.center(
                    rx.avatar(
                        src=data.avatar,
                        size=Size.XBIG.value,
                        radius="medium",
                        height=AVATAR_HEIGHT,
                    ),
                    width="100%",
                ),                
                rx.vstack(
                    heading(data.name, True),
                    heading(data.skill),
                    rx.text(
                        rx.icon("map-pin"),
                        data.location,
                        display="inherit"
                    ),
                    media(data.media),
                    spacing=Size.SMALL.value,
                    padding_x=EmSize.MEDIUM.value,
                    padding_y=EmSize.BIG.value,
                ),
                wrap="wrap",
                spacing=Size.SMALL.value,
            ),
        ),
        rx.tablet_and_desktop(
            rx.hstack(
                rx.avatar(
                    src=data.avatar,
                    size=Size.XBIG.value,
                    radius="medium",
                    height=AVATAR_HEIGHT,
                ),
                rx.vstack(
                    heading(data.name, True),
                    heading(data.skill),
                    rx.text(
                        rx.icon("map-pin"),
                        data.location,
                        display="inherit"
                    ),
                    media(data.media),
                    spacing=Size.SMALL.value,
                    padding_x=EmSize.MEDIUM.value,
                    padding_y=EmSize.BIG.value,
                ),
                spacing=Size.DEFAULT.value,
            ),
        ),
    )
