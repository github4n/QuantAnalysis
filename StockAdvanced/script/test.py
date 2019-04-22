from quantdata.stock import quotes



if __name__ == "__main__":
    stokList = quotes.get_stock_hq_list()
    print(stokList['code'])