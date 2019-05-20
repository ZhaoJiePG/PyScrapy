# Author:Aliex ZJ
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymongo

try:
    # 1.连接mongod的服务
    mongo_py= pymongo.MongoClient()

    # 2.库和表的名字；有数据自动建表
    # 数据库
    db = mongo_py['sex']

    # 表 集合
    collection = db['stu']
    collection = mongo_py['sex']['stu']

    # 3.插入数据
    one = {"name":"张三","age":"50"}

    # 插入多条数据
    two_many=[
        {"name":"张三","age":"50"},
        {"name":"李四","age":"60"},
        {"name":"王五","age":"70"},
        {"name":"小刘","age":"80"}
    ]

    #collection.insert_one(one)
    #collection.insert_many(two_many)
    # collection.insert()

    # 删除数据
    # collection.delete_one({"age":"50"})
    # collection.delete_many({"age":"50"})

    # 修改数据
    # collection.update({"age":80},{"$set":{"name":"刘刘"}})
    # collection.update_many({"name":"张三"},{"$set":{"age":"100"}})

    # 查询
    result = collection.find({"age": "60"})
    for i in result:
        print(i)

except Exception as e:
    print(e)

finally:
    # 关闭数据库
    mongo_py.close()