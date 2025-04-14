from time import sleep
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

console = Console()

# 로켓 본체 (불꽃 제외)
ROCKET_ART = r"""
         /\
        /  \
       |    |
       |    |
       |    |
       |    |
      /______\
       |    |
       |    |
       |    |
       |    |
       |    |
"""

# 불꽃 애니메이션 프레임 (빨간색과 노란색을 활용한 불꽃 모양)
flame_frames = [
r"""         [bold red]  .   [/bold red]
         [bold red] / \  [/bold red]
         [bold yellow] \ /  [/bold yellow]
         [bold yellow]  '   [/bold yellow]""",
r"""         [bold yellow]  .   [/bold yellow]
         [bold red] / \  [/bold red]
         [bold yellow] \ /  [/bold yellow]
         [bold red]  '   [/bold red]""",
r"""         [bold red]  .   [/bold red]
         [bold yellow] / \  [/bold yellow]
         [bold red] \ /  [/bold red]
         [bold yellow]  '   [/bold yellow]"""
]

# 우주 도착 시 보여줄 별이 반짝이는 배경
star_field = r"""
       .       *       .
   *       .      *       .
       .       *       .
   *       .      *       .
"""

def rocket_launch_with_flame_and_space(total_steps=25):
    """
    로켓이 발사되는 동안 불꽃 애니메이션과 함께 점점 높이 올라간 후,
    전체 단계의 70% 이후부터는 불꽃 대신 우주(별 배경)를 보여준다.
    """
    with Live(refresh_per_second=10) as live:
        for step in range(total_steps):
            # 로켓이 상승하는 효과: offset으로 빈 줄 추가
            offset = "\n" * (total_steps - step)
            # 진행 단계에 따라 불꽃 또는 별 배경을 보여줌
            if step < int(total_steps * 0.7):
                flame = flame_frames[step % len(flame_frames)]
            else:
                flame = star_field
            progress = f"[bold green]발사 진행 중: {int((step+1)/total_steps*100)}%[/bold green]"
            panel_content = offset + ROCKET_ART + "\n" + flame + "\n" + progress
            live.update(Panel(panel_content, title="[bold red]로켓 발사 시뮬레이터[/bold red]", border_style="bright_magenta"))
            sleep(0.3)
    console.clear()
    console.print(Panel(Text("우주 도착! 🌌", justify="center", style="bold cyan"),
                        title="[bold blue]완료[/bold blue]", border_style="green"))

def main():
    console.print(
        Panel(
            Text("로켓 발사 시뮬레이터", justify="center", style="bold magenta"),
            title="[bold blue]WELCOME[/bold blue]",
            border_style="bright_green"
        )
    )
    sleep(1)
    rocket_launch_with_flame_and_space()

if __name__ == "__main__":
    main()
