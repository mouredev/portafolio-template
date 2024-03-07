import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface"
        ),
        href=url,
        is_external=True
    )
