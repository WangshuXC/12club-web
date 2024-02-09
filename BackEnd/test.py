import pymysql
from faker import Faker
import random
import os
import shutil

faker = Faker()

# 配置数据库连接
USERNAME = "root"
PASSWORD = "root"
HOST = '127.0.0.1'
PORT = 3306
DATABASE = '12Club'

# 连接数据库
connection = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE)
cursor = connection.cursor()

# 创建anime表
create_table_query = """
CREATE TABLE IF NOT EXISTS anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    title_another VARCHAR(255),
    title_japanese VARCHAR(255),
    description VARCHAR(4095),
    release_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    view_count INT DEFAULT 0 NOT NULL,
    download_count INT DEFAULT 0 NOT NULL,
    cover VARCHAR(255)
)
"""
cursor.execute(create_table_query)

anime_list = [
    "我心里危险的东西",
    "我心里危险的东西 第二季",
    "药屋少女的呢喃",
    "鬼灭之刃",
    "鬼灭之刃 无限列车篇",
    "鬼灭之刃 游郭篇",
    "鬼灭之刃 刀匠村篇",
    "咒术回战",
    "咒术回战 第二季",
    "间谍过家家",
    "间谍过家家 第二季",
    "关于我转生变成史莱姆这档事",
    "关于我转生变成史莱姆这档事 第二季",
    "紫罗兰永恒花园",
    "小林家的龙女仆",
    "小林家的龙女仆 第二季",
    "Re：从零开始的异世界生活",
    "Re：从零开始的异世界生活 第二季",
    "工作细胞",
    "工作细胞 第二季",
    "冰菓",
    "青春猪头少年不会梦到兔女郎学姐",
    "埃罗芒阿老师",
    "欢迎来到实力至上主义的教室",
    "四月是你的谎言",
    "转生成蜘蛛又怎样",
    "盾之勇者成名录",
    "盾之勇者成名录 第二季",
    "盾之勇者成名录 第三季",
    "在下坂本，有何贵干？",
    "中二病也要谈恋爱！",
    "约会大作战",
    "约会大作战 第二季",
    "约会大作战 第三季",
    "约会大作战 第四季",
    "总之就是非常可爱",
    "总之就是非常可爱 第二季",
    "我的青春恋爱物语果然有问题",
    "路人女主的养成方法",
    "五等分的新娘",
    "夏日重现"
]
source_cover_path = 'D:\\Codefile\\12club\\Data\\Anime\\Cover.jpg'
base_anime_folder = 'D:\\Codefile\\12club\\Data\\Anime\\'

# 添加假数据
for anime in anime_list:
    # 创建动漫名称对应的文件夹
    anime_folder_path = os.path.join(base_anime_folder, anime)
    
    if not os.path.exists(anime_folder_path):
        os.makedirs(anime_folder_path)
    
        # 复制Cover.jpg到新创建的文件夹中
        destination_cover_path = os.path.join(anime_folder_path, 'Cover.jpg')
        shutil.copy(source_cover_path, destination_cover_path)

    insert_query = """
    INSERT INTO anime (title, release_date, view_count, download_count, cover)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        anime,
        faker.date_time_between(start_date='-10d', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
        random.randint(0, 10000),
        random.randint(0, 5000),
        'Cover.jpg'
    ))

# 提交改变并关闭连接
connection.commit()
connection.close()

print("Fake data added successfully.")
