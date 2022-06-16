"""Console script for create_meson_app."""
import os
import sys
import click
import inquirer
from meson_templates import CLIProjectTemplate, EmptyProjectTemplate, GnomeAdwaitaProjectTemplate, GnomeGTK4ProjectTemplate, GnomeProjectTemplate, LibraryProjectTemplate, get_project_templates, MesonTemplate

templates = {
    "GNOME Application - GTK4-based GUI application with Libadwaita":GnomeAdwaitaProjectTemplate,
    "GTK Application - GTK4-based GUI application without Libadwaita":GnomeGTK4ProjectTemplate,
    "GTK Application (legacy) - GTK3-based GUI application":GnomeProjectTemplate,
    "Shared Library":LibraryProjectTemplate,
    "Command Line Tool":CLIProjectTemplate,
    "Let's keep it empty! <3":EmptyProjectTemplate
}


@click.command()
# @click.option('--name', prompt="")
# @click.option('--license', prompt="Which copyright license would your lovely project use?", type=click.Choice(["MIT OR Apache-2.0", "LGPL-2.1-or-later", "GPL-2.1-or-later", "MPL-2.0-or-later"]), show_choices=True)
def main(args=None):
    """Console script for create_meson_app."""
    name = inquirer.text("What would you name your lovelyy project?")
    id = inquirer.text("What will the reverse DNS be?")
    license = inquirer.list_input(
        "What copyright license would you want to use?",
        choices=[
            "MPLv2-or-later",
            "MIT OR Apache2.0",
            "LGPLv2.1-or-later",
            "Keep it closed source!",
        ],
    )
    template = inquirer.list_input(
        "Which lovely template do you want to use?",
        choices=list(templates.keys()),
    )
    language = inquirer.list_input("What programming language would you like to use?", choices=templates[template]().languages)
    somewhere_else = "Place it somewhere else!"
    directory = inquirer.list_input("Where would you want to place the project in", choices=["Here! <3", somewhere_else])
    if directory == somewhere_else:
        dir_path = inquirer.shortcuts.path("Where would you like it to be in?",  path_type=inquirer.Path.DIRECTORY, normalize_to_absolute_path=True)
    else: 
        dir_path = os.path.join(os.getcwd(), name)
    git = inquirer.confirm("Would you like to create a pretty Git repository in the folder?", default=True)
    print(f"Done!! The project is now live at {dir_path}")
    print("Some things that you should now doo!!")
    if git:
        print("- Create an online Git repository: https://github.com/new")
    print("- Read the INSTRUCTIONS.md file in the project")
    print("- Hack it up noww and ship the project to production! <3")
    return 0
