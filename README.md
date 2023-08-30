# AutoBBSToper

A Selenium script that top your server thread.

## Usage

```shell

$ BBSTOPER_NOT_USE_X=1 python3 main.py # this will not use x, and thus you can run this script without a screen

$ python3 -i main.py # run in interactive mode, useful for login

```

## Preparation

- Please install `Xvfb` to your system first:

    ```shell
    $ sudo apt install xvfb
    ```

- Then to pip:

    ```shell
    $ pip install xvfbwrapper
    ```

- Also the `Selenium`:

    ```shell
    $ pip install selenium
    ```

- Download [`Chrome WebDriver`](https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/) and put the binary executable file under `/usr/bin/`:
