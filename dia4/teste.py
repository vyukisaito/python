import flet
from flet import (
    Page,
    colors
)

if __name__ == "__main__":
 
    def main(page: Page):
        page.bgcolor = colors.BLUE_GREY_200

    flet.app(target=main, view=flet.WEB_BROWSER)
