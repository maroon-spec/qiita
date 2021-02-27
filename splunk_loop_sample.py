

# 変数指定
SERVER = 'https://<hostname>'   # Splunk Server URL (do not include port)
USER =  '<user-name>'
PASSWD = '<passwd>'
MACRO = '<macro-name>'  # Splunkのマクロ名
OUTPUT = 'test.csv'   # 最後に結果を書き込む lookup file名

# List 取得のための SPL 
search_list_query = """
search index=hoge source=*stock_price.csv | table "Local Code" | dedup "Local Code"
"""

##  リストデータの取得
import requests

data = {
  'search': search_list_query,
  'exec_mode': 'oneshot',
  'output_mode': 'json',
  'count': '0'   # default だと 100個しかリターンされない
}

response = requests.post(SERVER + ':8089/services/search/jobs' , data=data, verify=False, auth=(USER, PASSWD))

## 出力結果のうち、値だけを抜き出す
lists = list()
result=response.json()['results']
for i in result:
  lists.append(list(i.values()))

# 抜き出した値ごとに、特定のマクロを実行させて、最後はファイルに保存
for j in lists:

  data1 = {
    'search': '| `' + MACRO + '(' + j[0] + ')` | outputlookup ' + OUTPUT + ' append=t',
    'exec_mode': 'oneshot',
    'output_mode': 'json'
  }
  response = requests.post(SERVER + ':8089/services/search/jobs' , data=data1, verify=False, auth=(USER, PASSWD))

