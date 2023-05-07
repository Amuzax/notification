import requests
from bs4 import BeautifulSoup

# LINE通知用
token = '44Y273T6DMePeaNG3rsqOpRjG8dv0BrNM3ccAUSTRIN'
url = 'https://notify-api.line.me/api/notify'

# ヤフオク商品ページ情報を取得
item_url = 'https://page.auctions.yahoo.co.jp/jp/auction/b1090530615'
response = requests.get(item_url)
soup = BeautifulSoup(response.text, 'html.parser')

def main():
    # 商品価格を取得
    item_price = int(soup.select('dd.Price__value')[0].text.strip().split('円')[0])
    # print('価格:', item_price)
    # print(type(item_price))

    # しきい値設定
    threshold = 650

    # LINE認証情報
    auth = {'Authorization': 'Bearer ' + token}
    # 送信メッセージ
    if item_price > threshold:
        content = {'message': f'現在の価格は{item_price}円です'}
    else:
        content = {'message': f'価格は{threshold}円以下です'}

    # LINEメッセージを送信
    requests.post(url, headers=auth, data=content)

if __name__ == "__main__":
    main()