# ssdeep-ftw
SSDEEP Python Wrapper - For The Windows 

[Blog post here](https://c0d.ist/ssdeep-python-windows-wrapper/)

## Introduction
[SSDEEP](http://ssdeep.sourceforge.net/), I believe, is an essential tool to many researchers, malware analysts, reverse engineers, etc. It is available as binary for various platforms. However, same is not the case with Python bindings.
Linux users can use [ssdeep](https://pypi.python.org/pypi/ssdeep) or [pydeep](https://github.com/kbandla/pydeep) to compute or compare hashes.
However, for Windows users, it is not all that easy.

Therefore, `ssdeep-ftw` aims to provide a Python interface for Windows users. 
The wrapper is merely a dirty hack around the original `ssdeep.exe` in your system. **(Use it at your own risk)**
However, the wrapper works as expected, as least on the setup listed below.

#### Tested on:
- OS: Windows 7
- Python: 2.7
- SSDEEP: [2.13](http://sourceforge.net/projects/ssdeep/files/ssdeep-2.13/ssdeep-2.13.zip/download)

## Requirements:
The code depends upon ssdeep executable in your system. 
Therefore, it goes on without saying that you should have working ssdeep.exe on your system.
The version that we used for testing is available [here](http://sourceforge.net/projects/ssdeep/files/ssdeep-2.13/ssdeep-2.13.zip/download).

## Supported Operations:
- Computing ssdeep hash from a file.
- Computing ssdeep hash from a string.
- Comparing two ssdeep hashes.

### To-do
- Comparing two files

## Examples:
The example code can found in [example.py](example.py).

## License
The code is licensed under [The Beerware License](https://fedoraproject.org/wiki/Licensing/Beerware).
