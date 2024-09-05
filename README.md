# VSC Clean Uninstaller (Windows)

## About

Visual Studio Code's default uninstaller does not delete user settings and extensions, so I did this little script.

## How to use
> 
> _Please remember that this only works for Windows._

1. Download the latest version from the releases page.
2. Execute it.
   > **If any security pop-up is shown, ignore it; if you don't trust the program, just don't use it.**

## How to contribute

If you can add a new feature or fix something, you can contribute according to the [license](LICENSE).

### Things you will need:

- Python (I used version 3.11.9)

### Setting up the workspace

> _Windows only._

```pwsh
# Make a virtual environment
py -m venv .venv

# Activate it
.\.venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Building an executable

```pwsh
pyinstaller "VSC Clean Uninstaller.spec"
```

## Credits

Icon: <a href="https://www.flaticon.es/iconos-gratis/limpieza-de-cristales" title="limpieza de cristales iconos">Window cleaning icons created by Freepik - Flaticon</a>

## License

This project is under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/#), a copy of it can be found [here](LICENSE).

## Contact

Discord: `3xotic.`
