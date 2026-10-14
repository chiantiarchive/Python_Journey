

from pathlib import Path

from rich.console import Console

from src.app import get_welcome_message


console = Console()


def main():
    base_dir = Path(__file__).parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "output"

    output_dir.mkdir(exist_ok=True)

    console.print(get_welcome_message("Python Journey"), style="bold green")
    console.print(f"Data folder exists: {data_dir.exists()}")
    console.print(f"Output folder exists: {output_dir.exists()}")


if __name__ == "__main__":
    main()