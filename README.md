# FlickrDownloadr_cli

A simple way to download pictures from Flickr.

### Features

- Easy way of downloading (no need to right-click > Save image)
- Support for batch download
- Works with Linux and OS X
- It may work with Windows (who cares?)

### Requirements

- Python 2.7 (not tested with 2.6 or 3.x)
- BeautifulSoup module (bs4)

### Installation

1. clone the repo
2. cd the directory
3. chmod +x the script
4. execute it!

**OR**

You can install permanently (kind of) on your system running:

```
sudo cp flickdl.py /usr/local/bin/flickdl
sudo chmod +x /usr/local/bin/flickdl
```

### Usage

```
./flickdl.py url1,url2,...
```

**Example**

```
./flickrdl.py https://www.flickr.com/photos/example/12345678910/sizes/o/,https://..."
```

### License

The software in this repository are released under the GNU GPLv3 License by Francesco Pira (dev[at]fpira[dot]com, fpira.com). You can read the terms of the license [here](http://www.gnu.org/licenses/gpl-3.0.html).
