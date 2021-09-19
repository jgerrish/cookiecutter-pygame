===================
Cookiecutter Pygame
===================

This is a cookiecutter template for the Python.  It lets you quickly create a
new game project.

========
Features
========

You can also build a Pygame project with jupyterlab incuded for
editing.  The combination of jupyter and Pygame provide a great interactive
environment to learn programming and game development.

Additional modules can be added to the project to show how to use
Pygame.  For example, including the animation module shows how to
animate a simple shape.

=======
Install
=======

To install:

pip install -U pipenv
pip install -U cookiecutter

cookiecutter https://github.com/jgerrish/cookiecutter-pygame.git

This will create a directory with your game.  If you named your game
"My Game" it creates a directory called my_game.

Then install the requirements.  This will install pygame and Jupyter
if you selected it.

pipenv install


=======
Running
=======

If your game name is "My Game".  In the project directory type the following:

python -m my_game.main

If you installed jupyterlab:

jupyter-lab my_game/main.py

=======
Details
=======

The cookiecutter project has info if you want to learn more about
cookiecutter.

Cookiecutter: https://github.com/cookiecutter/cookiecutter

Parts of this template are copied from the KidsCanCode pygame tutorials
https://github.com/kidscancode/pygame_tutorials

This template attempts to balance easily building new projects and
allowing users to explore how to build games with pygame.

Basic concepts are explained in the code, encouraging users to
experiment with settings and defaults.

