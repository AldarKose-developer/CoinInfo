# CoinInfo
CoinInfo parse latest information about cryptocurrency that you want.

## Installation
YOU SHOULD HAVE THE GOOGLE CHROME BROWSER  94.0.4606.71 IN ORDER TO CODE WORK!!!
### Install libraries
Selenium
```
pip install selenium
```
Requests
```
pip install requests
```
Beautiful Soup
```
pip install beautifulsoup4
```
### Change path in test.py file
You should change path in test.py file. Replace path with path where folder with project located in your system.
```
sys.path.append('MYPATH')
```

## Usage
Call get_news() method from parser module and provide name of coin
```
parser.CryptoNews.get_news('cardano')
```

## Examples
You should input name of coin in lowercase e.g 'monero'.
Then it will return you dictionary with title and paragraphs
### For example
```
Enter a name of currency: bitcoin

{' Bitmain stops shipment of Antminer crypto mining rigs into China ': " Bitmain plans to identify green energy mining opportunities from power generation projects in Chinese provinces.  Bitmain, a Chinese manufacturer of cryptocurrency mining equipment, has been forced to stop its business in China from Oct. 11 following the crypto ban imposed by local authorities. ...
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
