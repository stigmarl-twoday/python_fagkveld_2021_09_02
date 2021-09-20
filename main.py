from pathlib import Path

import click

from gen.chars import generate_char, generate_char_set


@click.command()
@click.option(
    "--length", help="Length of the generated password", type=click.INT, required=True
)
@click.option(
    "--grade",
    help="Security grade of the password",
    type=click.IntRange(0, 3, clamp=True),
    default=0,
)
@click.option("--file", type=click.Path(), default="verdens_beste_passord.txt")
def generate(length: int, grade: int, file: str):

    char_set = generate_char_set(grade)

    gen_pwd = "".join(generate_char(char_set) for i in range(length))

    file_path = Path(file)

    if not file_path.parent.is_dir():
        file_path.parent.is_dir()

    with open(file_path, "w") as f:
        f.write(gen_pwd)


if __name__ == "__main__":
    generate()
