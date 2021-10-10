import sys

sys.path.append('C:\\Users\\nurik\\Desktop\\Project\\Python Projects\\parser2')
from src import parser

# My package can provide a functionality to declare an object
object = parser.CryptoNews()
coin = input("Enter a name of currency: ")
# get_news method from CryptoNews class receives coin name
print(parser.CryptoNews.get_news(coin))
