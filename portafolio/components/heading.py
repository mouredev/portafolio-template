import reflex as rx
from portafolio.styles.styles import Size


def heading(text: str, h1=False) -> rx.Component:
    return rx.heading(
        text,
        as_="h1" if h1 else "h2",
        size=Size.BIG.value if h1 else Size.MEDIUM.value
    )
