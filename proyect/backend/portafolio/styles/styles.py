from enum import Enum
import reflex as rx

MAX_WIDTH = "1000px"
IMAGE_HEIGHT = "200px"
AVATAR_HEIGHT = "300px"

class EmSize(Enum):
    ZERO = "0em"
    DEFAULT = "1em"  # 16px
    MEDIUM = "2em"
    BIG = "4em"
    XBIG = "6em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8px
    DEFAULT = "4"  # 16px/1em
    MEDIUM = "6"  # 32px
    BIG = "8"  # 48px
    XBIG = "9"

glassmorphism = dict(
    background_color="rgba(225, 225, 225, 0.25)",
    box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.37)",
    backdrop_filter="blur(0.1px)",
    border="2px solid rgba(225, 225, 225, 0.15)",
    border_radius="20px"
)
    

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}
