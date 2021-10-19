# 文字版的MySQL資料庫管理介面

一個簡單的資料庫管理介面，透過Python來控制MySQL資料庫的新增、修改、刪除。

使用pymysql來連結資料庫，用prettytable將資料表輸出成易閱讀的表格，由於更新和刪除的指令也會需要將會員資料表印出，故寫成function來重複使用。
```
def show_all_data():
    clear()
    # 搜尋資料庫找出會員列表
    cur.execute("SELECT * FROM `member`")
    data = cur.fetchall()

    # 先準備會員列表表格
    show_all = pt.PrettyTable(["編號", "姓名", "生日", "地址"])

    # 製作表格
    for item in data:
        show_all.add_row([item[0], item[1], item[2], item[3]])
    # 印出所有資料
    print(show_all)
    return data
```


## 功能選單

(0) 離開程式
(1) 顯示會員列表
(2) 新增會員資料
(3) 更新會員資料
(4) 刪除會員資料

## 印出的會員資料表範例

![screenshot image](/screenshot.PNG)


## 確認資訊

我多加一點功能，讓新增資料後顯示新建的最新一筆資訊：
```
newest_id = cur.lastrowid
cur.execute("SELECT * FROM `member` WHERE `id` = %s", newest_id)
print(cur.fetchone(), "新增成功")
```

![image](/new_inserted.PNG)


修改和刪除後也會印出資料編號進行確認：

![modified](/modified.PNG)

