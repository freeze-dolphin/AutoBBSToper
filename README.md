# AutoBBSToper

A Selenium script that top your server thread.

## Usage

```shell
$ make exec # this will not use x, and thus you can run this script without a screen
```

```shell
$ make interactive # run in interactive mode, useful for obtain cookies
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

- Download [`Chrome WebDriver`](https://googlechromelabs.github.io/chrome-for-testing/#stable) and put the binary
  executable file under `/usr/bin/`:
