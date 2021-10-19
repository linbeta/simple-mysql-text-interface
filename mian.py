import pymysql
import prettytable as pt
import os

# 登入資料庫

id = input("請輸入資料庫帳號： ")
pw = input("請輸入資料庫密碼： ")

link = pymysql.connect(
    host="teaching-db.bo-yuan.net",
    user=id,
    passwd=pw,
    db="AI09_02",
    charset="utf8",
    port=3306
)

# 取得指令操作變數
cur = link.cursor()

# 清除螢幕指令


def clear(): return os.system('cls')

# 列出所有資料，由於更新和刪除的指令也會需要將會員資料表印出，故寫成function來重複使用


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


# 登入成功後印出選單
while True:
    command = input(
        "(0) 離開程式\n(1) 顯示會員列表\n(2) 新增會員資料\n(3) 更新會員資料\n(4) 刪除會員資料\n指令： ")
    if command == "1":
        # 搜尋資料庫找出會員列表
        show_all_data()

    elif command == "2":
        clear()
        name = input("請輸入會員姓名： ")
        birthday = input("請輸入會員生日： ")
        address = input("請輸入會員地址： ")
        cur.execute("INSERT INTO `member`(`name`, `birthday`, `address`) VALUES (%s, %s, %s)", [
                    name, birthday, address])
        link.commit()

        # 印出最新一筆新增資料
        clear()
        newest_id = cur.lastrowid
        cur.execute("SELECT * FROM `member` WHERE `id` = %s", newest_id)
        print(cur.fetchone(), "新增成功")

    elif command == "3":
        data = show_all_data()
        update_id = input("請選擇你要修改的資料編號： ")

        # check all_ids: 有在all_ids列表中的才執行修改、收input值，其他輸入則無動作
        all_ids = [str(item[0]) for item in data]
        if update_id in all_ids:
            name = input("請輸入會員姓名： ")
            birthday = input("請輸入會員生日： ")
            address = input("請輸入會員地址： ")
            cur.execute("UPDATE `member` SET `name`=%s,`birthday`=%s,`address`=%s WHERE `id`=%s", [
                        name, birthday, address, int(update_id)])
            link.commit()
            clear()
            print(f"編號{update_id}資料已修改")
        else:
            clear()

    elif command == "4":
        data = show_all_data()
        delete_id = input("請選擇你要刪除的資料編號： ")

        # check all_ids: 有在all_ids列表中的才執行刪除，其他輸入值無動作
        all_ids = [str(item[0]) for item in data]
        if delete_id in all_ids:
            cur.execute("DELETE FROM `member` WHERE `id`=%s", int(delete_id))
            link.commit()
            clear()
            print(f"編號{delete_id}資料已刪除")
        else:
            clear()

    elif command == "0":
        break

# Here's my GitHub repository link: https://github.com/linbeta/simple-mysql-text-interface.git
