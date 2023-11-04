# AutoBBSToper

A Selenium script that top your server thread.

## Usage

```shell
$ make auto # top the thread
```

```shell
$ make interactive # run in interactive mode, useful to obtain cookies
```

### For Windows Users

If you are on Windows, firstly set env-var `BBSTOPER_HEADLESS` to `2` and then run the script by:

```shell
python main.py
```

As for the interactive, use the one below:

```shell
python -i main.py
```

## Preparation

- Install the `Selenium`:

    ```shell
  $ pip install selenium
    ```

- Download [`Chrome WebDriver`](https://googlechromelabs.github.io/chrome-for-testing/#stable) and put the binary
  executable file under `/usr/bin/` or in your `$PATH`:

## Automation

If there is any problem encountered during topping, the program will exit with non-zero code.

Judging from the return value might be useful for your writing automation scripts.

The following powershell is an example:

```powershell
$Env:BBSTOPER_HEADLESS = '2'
do
{
    $proc = Start-Process python3.exe -ArgumentList "main.py" -Wait -PassThru
} while ($proc.ExitCode ! = 0)
```

Consider the script above, maybe you need to replace `python3.exe` to the exact absolute path to python executable, also
remember to keep the working dir to the repository that you clone.
