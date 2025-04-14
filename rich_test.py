import time
import random
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

# force_terminal 옵션은 사용하는 환경에 맞게 추가(여기서는 기본값 사용)
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

def rocket_launch_with_flame_and_space(total_steps=25):
    """
    로켓이 발사되는 동안 불꽃 애니메이션과 함께 점점 높이 올라가다가,
    발사 단계의 일정 부분 이후엔 우주(별 배경)를 표현합니다.
    """
    # 불꽃 애니메이션 프레임 (불꽃 모양 다양하게 표현)
    flame_frames = [
        r"""
         |  |
         |++|
         |++|
          \/""",
        r"""
         |  |
         |**|
         |**|
          \/""",
        r"""
         |  |
         |##|
         |##|
          \/"""
    ]
    # 우주 도착 시 보여줄 별이 반짝이는 배경
    star_field = r"""
       .       *       .    
   *       .      *       .
       .       *       .    
   *       .      *       .
    """
    with Live(refresh_per_second=10, console=console) as live:
        for step in range(total_steps):
            # 로켓 상승 효과: offset을 이용하여 위쪽으로 이동하는 모양 연출
            offset = "\n" * (total_steps - step)
            # 전체 진행 단계의 70%까지는 불꽃 애니메이션, 이후는 우주 배경
            if step < int(total_steps * 0.7):
                flame = flame_frames[step % len(flame_frames)]
            else:
                flame = star_field
            progress = f"[bold green]발사 진행 중: {int((step+1)/total_steps*100)}%[/bold green]"
            panel_content = offset + ROCKET_ART + "\n" + flame + "\n" + progress
            live.update(Panel(panel_content, title="[bold red]로켓 발사 시뮬레이터[/bold red]", border_style="bright_magenta"))
            time.sleep(0.3)
    console.clear()
    # 랜덤하게 성공 또는 폭발 결정 (50% 확률)
    outcome = random.choice(["success", "explode"])
    if outcome == "success":
        console.print(
            Panel(
                Text("우주 도착! 🌌", justify="center", style="bold cyan"),
                title="[bold blue]완료[/bold blue]",
                border_style="green"
            )
        )
    else:
        rocket_explosion_animation()

def rocket_explosion_animation():
    """
    폭발 애니메이션을 실행합니다.
    여러 단계를 거쳐 로켓 폭발을 시각화한 후 최종 패널에 폭발 메시지를 출력합니다.
    """
    explosion_frames = [
        r"""
       .
      .* *.
       '""",
        r"""
      .   .
    .  BOOM  .
      .   .""",
        r"""
  *         *
    * BOOM!! *
  *         *""",
        r"""
     !!!!!!!
     !!!!!!!
     !!!!!!!"""
    ]
    with Live(refresh_per_second=5, console=console) as live:
        for frame in explosion_frames:
            panel = Panel(frame, title="[bold red]로켓 폭발![/bold red]", border_style="red")
            live.update(panel, refresh=True)
            time.sleep(0.5)
    console.clear()
    console.print(
        Panel("로켓 폭발! 💥", title="[bold red]실패[/bold red]", border_style="red")
    )

def main():
    console.print(
        Panel(
            Text("로켓 발사 시뮬레이터", justify="center", style="bold magenta"),
            title="[bold blue]WELCOME[/bold blue]",
            border_style="bright_green"
        )
    )
    time.sleep(1)
    rocket_launch_with_flame_and_space()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("[bold red]시뮬레이션을 종료합니다.[/bold red]")
