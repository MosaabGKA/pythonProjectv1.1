import time
import random
import flet as ft


def main(page: ft.Page):
    page.title = "Match the Pictures"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    def generate_answer(d):
        pics = [i for i in range(d // 2)] * 2
        random.shuffle(pics)
        ans = [[] for i in range(d // 2)]
        for i in range(d):
            ans[pics[i]].append(i)
        return ans

    def start_game(self):
        # tim = int(game_timer.current.value)
        page.window_width = 850
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

        def end_of_game():
            time.sleep(1)
            pics_grid.current.controls.clear()
            game_title.current.controls[0] = ft.Text(
                "CONGRATULATIONS!!! \n You matched all the pictures.",
                text_align=ft.TextAlign.CENTER,
                size=30, weight=ft.FontWeight.W_700
            )
            page.update()

        selected = []
        correct_matches = answer_pairs[:]

        def picture_selected(e):
            if len(selected) == 0:
                selected.append(e.control.data)
                e.control.style.side = ft.BorderSide(2, ft.colors.WHITE)
                page.update()
            else:
                if e.control.data in selected:
                    e.control.style.side = ft.BorderSide(0, ft.colors.WHITE)
                    page.update()
                    selected.remove(e.control.data)
                else:
                    selected.append(e.control.data)
                    e.control.style.side = ft.BorderSide(2, ft.colors.WHITE)
                    page.update()
                    selected_mirror = selected[-1:-3:-1]
                    time.sleep(0.5)
                    if selected in answer_pairs:
                        for i in selected:
                            pics_grid.current.controls[i].style.side = ft.BorderSide(0, ft.colors.GREEN)
                            pics_grid.current.controls[i].disabled = True
                            pics_grid.current.controls[i].content.content.src = f"pics/{answer_pairs.index(selected)}.jpg"
                        page.update()
                        correct_matches.remove(selected)
                        selected.clear()
                        selected_mirror.clear()
                        if len(correct_matches) == 0:
                            end_of_game()
                    elif selected_mirror in answer_pairs:
                        for i in selected_mirror:
                            pics_grid.current.controls[i].style.side = ft.BorderSide(0, ft.colors.GREEN)
                            pics_grid.current.controls[i].disabled = True
                            pics_grid.current.controls[i].content.content.src = f"pics/{answer_pairs.index(selected_mirror)}.jpg"
                        page.update()
                        correct_matches.remove(selected_mirror)
                        selected.clear()
                        selected_mirror.clear()
                        if len(correct_matches) == 0:
                            end_of_game()
                    else:
                        for i in selected:
                            pics_grid.current.controls[i].style.side = ft.BorderSide(0, ft.colors.WHITE)
                        page.update()
                        selected.clear()
                        selected_mirror.clear()

        pics_grid.current.controls = [0 for i in range(num_of_pics)]
        for i in range(len(answer_pairs)):
            for j in range(2):
                indx = answer_pairs[i][j]
                pics_grid.current.controls[indx] = ft.OutlinedButton(
                    content=ft.Container(
                        content=ft.Image(
                            src=f"pics/{i}.jpg",
                            width=180,
                            height=120,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(7),
                        ),
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=7),
                    ),
                    disabled=True,
                )
        page.update()
        time.sleep((int(game_dimensions.current.value) + 1) * 3)
        game_title.current.controls[0] = ft.Text("Match Similar Pictures", size=40, weight=ft.FontWeight.W_700)
        pics_grid.current.controls = [0 for i in range(num_of_pics)]

        for i in range(len(answer_pairs)):
            for j in range(2):
                indx = answer_pairs[i][j]
                pics_grid.current.controls[indx] = ft.OutlinedButton(
                    content=ft.Container(
                        content=ft.Image(
                            src="pics/q.jpg",
                            width=180,
                            height=120,
                            fit=ft.ImageFit.COVER,
                            border_radius=ft.border_radius.all(7),
                        ),
                    ),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=7),
                    ),
                    data=indx,
                    on_click=picture_selected,
                )
        page.update()

    game_title = ft.Ref[ft.Row]()
    game_options = ft.Ref[ft.Row]()
    game_dimensions = ft.Ref[ft.RadioGroup]()
    # game_timer = ft.Ref[ft.RadioGroup]()
    game_starter = ft.Ref[ft.FilledButton]()
    page.add(
        ft.Row(ref=game_title, expand=0, wrap=False, alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(ref=game_options, expand=0, wrap=False, alignment=ft.MainAxisAlignment.SPACE_AROUND),
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
    # game_options.current.controls.append(
    #     ft.RadioGroup(ref=game_timer, value="30", content=ft.Row([
    #         ft.Text("Choose Game Timer:", size=20),
    #         ft.Radio(value="30", label="30"),
    #         ft.Radio(value="60", label="60"),
    #         ft.Radio(value="90", label="90"),
    #         ft.Radio(value="120", label="120"),
    #         ft.Text("(Seconds)", size=12),
    #     ])),
    # )
    game_options.current.controls.append(
        ft.FilledButton(
            ref=game_starter,
            text="Start Game!",
            on_click=start_game,
        )
    )
    page.update()


ft.app(target=main)
