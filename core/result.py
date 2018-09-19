import requests
import json
import pymysql
from time import sleep

conn = pymysql.connect(
    host='127.0.0.1',
    port=3315,
    user='root',
    password='0000',
    db='main',
    charset='utf8'
)

url = 'http://ntry.com/data/json/games/dari/result.json'
payload = {}

while True:
    r = requests.get(url, params=payload).text
    result = json.loads(r)

    d = result['d']
    r = result['r']
    s = result['s']
    l = result['l']
    o = result['o']

    curs = conn.cursor()

    sql = '''
        select count(*)
        from gamble_result
        where gb_date = '{d}'
        and gb_round = '{r}'
    '''.format(d=d, r=r)
    curs.execute(sql)
    rows = curs.fetchall()

    if rows[0][0] == 0:
        sql = '''
            insert into gamble_result(gb_date, gb_round, gb_leftright, gb_threefour, gb_evenodd)
            values('{d}','{r}','{s}','{l}','{o}');
        '''.format(d=d, r=r, s=s, l=l, o=o)
        curs.execute(sql)
        conn.commit()
        print('데이터 삽입 완료 -> {0} {1}회'.format(d,r))
    else:
        print('데이터 중복 방지')
    sleep(5)
conn.close()
