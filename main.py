from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from src.detect import detect_mail
from src.parse_email import parse_email

console = Console()


def display_menu():
    console.clear()

    console.print(
        Panel.fit(
            "[bold cyan]Phishing Email Detector[/bold cyan]",
            border_style="green",
        )
    )

    menu = Table(show_header=True, header_style="bold magenta")
    menu.add_column("Option", justify="center")
    menu.add_column("Action")

    menu.add_row("1", "Detect Email", style="green")
    menu.add_row("2", "Exit", style="red")

    console.print(menu)


while True:

    display_menu()

    choice = console.input(
        "\n[bold yellow]Enter your choice:[/bold yellow] "
    ).strip().lower()

    match choice:

        case "1":

            console.clear()

            console.print(
                Panel.fit(
                    "[bold cyan]Paste Email[/bold cyan]",
                    border_style="cyan",
                )
            )

            console.print(
                "[green]Paste the complete email below.[/green]"
            )

            console.print(
                "[dim]Type END on a new line when finished.[/dim]\n"
            )

            email_lines = []

            while True:

                line = console.input()

                if line.strip().upper() == "END":
                    break

                email_lines.append(line)

            raw_email = "\n".join(email_lines)

            if not raw_email.strip():

                console.print(
                    "\n[bold red]Email cannot be empty.[/bold red]"
                )

                console.input(
                    "\nPress Enter to continue..."
                )

                continue

            console.rule()

            try:

                email = parse_email(raw_email)

                detect_mail(
                    text=email["text"],
                    url=email["url"],
                )

            except Exception as e:

                console.print(
                    Panel.fit(
                        str(e),
                        title="Error",
                        border_style="red",
                    )
                )

            console.rule()

            console.input(
                "\nPress Enter to return to menu..."
            )

        case "2" | "q" | "quit" | "exit":

            console.print(
                "\n[bold green]Goodbye![/bold green]"
            )

            break

        case _:

            console.print(
                "\n[bold red]Invalid Option![/bold red]"
            )

            console.input(
                "Press Enter to continue..."
            )