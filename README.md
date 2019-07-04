# nDPI-warpper

Python wrapper of the library nDPI, it will allow you to analize data without warring so much about c code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Firstly compile nDPI following the instraction of README.md on the nDPI folder.

### Prerequisites

This software has been tested under python 3.5 but every python version higher or equal  2.7 should be fine(just change print() and use it without the Brackets)

### Installing

Go inside the folder /example/ and extract all the file of nDPI-wrapper inside that folder. Then you need to create a shared library, to do so just type

```
make -f Makefile.wrap
```

so to test it just use

```
python ndpi_Reader_wrap.py -i <interface>
```

alternatively run it like this and see what it can offer you

```
python ndpi_Reader_wrap.py
```

### More information
To have a closer look at my wrapper see the ndpi_wrapper.pdf file
