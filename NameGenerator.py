
import random
from SurnameDatabase import SurnameDatabase
from NameDatabase import NameDatabase

class NameGenerator:
    def __init__(self, surname_db, name_db):
        self.surname_db = surname_db
        self.name_db = name_db
        self.random_state = random.Random()

    def generate_name(self, tags, double_name):
        # 确保传递tags给get_random_surname方法
        surname = self.surname_db.get_random_surname(tags)
        matching_names = self.name_db.get_names_by_tags(tags)

        # 确保在随机选择之前传递一个列表
        chosen_names = self.random_state.sample(matching_names, 2 if double_name else 1)

        # 组合姓和名，确保surname不是None
        if surname:
            return surname + ''.join(name.text for name in chosen_names)
        else:
            return None

# 实例化SurnameDatabase和NameDatabase
surname_db = SurnameDatabase()
name_db = NameDatabase()

# 实例化NameGenerator
name_gen = NameGenerator(surname_db, name_db)

# 开始生成名字
name_gen.start_generation()
