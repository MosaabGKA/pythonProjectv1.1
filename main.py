import time
import random
import flet as ft


def main(page: ft.Page):
    page.title = "Match the Pictures"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # page.window_full_screen = True

    def generate_answer(d):
        pics = [i for i in range(d // 2)] * 2
        random.shuffle(pics)
        ans = [[] for i in range(d // 2)]
        for i in range(d):
            ans[pics[i]].append(i)
        return ans

    def start_game(self):
        # tim = int(game_timer.current.value)
        x_options = [3, 4, 4]
        y_options = [2, 3, 4]
        x_dimension = x_options[int(game_dimensions.current.value)]
        y_dimension = y_options[int(game_dimensions.current.value)]
        num_of_pics = x_dimension * y_dimension
        answer_pairs = generate_answer(num_of_pics)
        game_options.current.visible = False
        game_title.current.controls[0] = ft.Text("Remember these pictures", size=40, weight=ft.FontWeight.W_700)
        pics_grid = ft.Ref[ft.GridView]()
        page.add(ft.GridView(
            ref=pics_grid,
            expand=0,
            # max_extent=200,
            width=800,
            runs_count=x_dimension,
            child_aspect_ratio=1.5,
            spacing=5,
            run_spacing=5,
        ))
        for i in range(num_of_pics // 2):
            for j in range(2):
                pics_grid.current.controls.insert(
                    answer_pairs[i][j],
                    ft.OutlinedButton(
                        content=ft.Container(
                            content=ft.Image(
                                src=f"{i}.jpg",
                                width=180,
                                height=120,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.all(7),
                            ),
                            # padding=ft.padding.all(10),
                        ),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=7),
                        ),
                        on_click=None
                    )
                )
        page.update()
        time.sleep((int(game_dimensions.current.value)+1)*3)
        pics_grid.current.controls.clear()
        for i in range(num_of_pics // 2):
            for j in range(2):
                pics_grid.current.controls.insert(
                    answer_pairs[i][j],
                    ft.OutlinedButton(
                        content=ft.Container(
                            content=ft.Image(
                                src="q.jpg",
                                width=180,
                                height=120,
                                fit=ft.ImageFit.COVER,
                                border_radius=ft.border_radius.all(7),
                            ),
                            # padding=ft.padding.all(10),
                        ),
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=7),
                        ),
                        on_click=None
                    )
                )
        page.update()


    game_title = ft.Ref[ft.Row]()
    game_options = ft.Ref[ft.Row]()
    game_dimensions = ft.Ref[ft.RadioGroup]()
    game_timer = ft.Ref[ft.RadioGroup]()
    game_starter = ft.Ref[ft.FilledButton]()
    page.add(
        ft.Row(ref=game_title, expand=0, wrap=False, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(ref=game_options, expand=0, wrap=False, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    )
    game_title.current.controls.append(
        ft.Text("Welcome to Match the Pictures Game", size=50, weight=ft.FontWeight.W_900)
    )
    game_options.current.controls.append(
        ft.RadioGroup(ref=game_dimensions, value="0", content=ft.Row([
            ft.Text("Choose Game Dimensions:", size=20),
            ft.Radio(value="0", label="3×2"),
            ft.Radio(value="1", label="4×3"),
            ft.Radio(value="2", label="4×4"),
        ]))
    )
    game_options.current.controls.append(
        ft.RadioGroup(ref=game_timer, value="30", content=ft.Row([
            ft.Text("Choose Game Timer:", size=20),
            ft.Radio(value="30", label="30"),
            ft.Radio(value="60", label="60"),
            ft.Radio(value="90", label="90"),
            ft.Radio(value="120", label="120"),
            ft.Text("(Seconds)", size=12),
        ])),
    )
    game_options.current.controls.append(
        ft.FilledButton(
            ref=game_starter,
            text="Start Game!",
            on_click=start_game,
        )
    )
    page.update()


ft.app(target=main)
