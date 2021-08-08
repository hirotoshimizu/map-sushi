import json

json_data = [{'name': '鮨 桂太', 'lat': '35.665', 'lng': '139.773', 'business_hour': '昼＝11:30-14:30※昼は水・土・日のみ営業夜＝18:00-22:30'},  
             {'name': '天寿し 京町店', 'lat': '33.885', 'lng': '130.884', 'business_hour': '昼＝12:00-13:30、14:00-15:30夜＝17:30-19:00、19:30-21:00'},
             {'name': 'いづう', 'lat': '35.005', 'lng': '135.774', 'business_hour': '昼／夜＝11:00-22:00※日・祝　11:00-21:00'}
            ]


j = json.dumps(json_data)
print(j)


data_python = [{'name': 'Taro', 'age': 14, 'check': True}, 
{'name': 'Jiro', 'age': 23, 'check': False}, 
{'name': 'Tom', 'age': 16, 'check': False}]