from NameDatabase import NameDatabase
from SurnameDatabase import SurnameDatabase
from random import Random


class NameGenerator:
    def __init__(self):
        self.name_db = NameDatabase()
        self.surname_db = SurnameDatabase()
        self.random_state = Random()

    def generate_name(self, tags, double_name=False):
        # 从名字数据库中基于标签筛选名字
        filtered_names = self.name_db.get_names_by_tags(tags)

        # 获取随机姓氏
        surname = self.surname_db.get_random_surname(self.random_state)

        # 随机选择一个或两个名字
        selected_names = self.random_state.sample(filtered_names, 2 if double_name else 1)
        name_texts = [name.text for name in selected_names]

        # 组合姓氏和名字
        return surname + ''.join(name_texts)

    def start_generation(self):
        # 显示所有可用标签
        available_tags = list(set(tag for name in self.name_db.names for tag in name.tags))
        print(f"以下是所有可用的标签：\n{', '.join(available_tags)}")

        # 输入标签
        tags_input = input("请选择标签，用逗号分隔：").split(',')
        tags = [tag.strip() for tag in tags_input]

        # 选择单字或双字名
        name_length = input("您想要生成单字名还是双字名？(单/双)：")
        double_name = True if name_length.strip().lower() == '双' else False

        # 生成名字并询问用户是否满意
        satisfied = False
        while not satisfied:
            new_name = self.generate_name(tags, double_name)
            print(f"生成的名字为：{new_name}")
            if input("您是否满意这个名字？(yes/no)：").strip().lower() == 'yes':
                satisfied = True
            else:
                if input("是否要保留当前的标签？(yes/no)：").strip().lower() == 'no':
                    tags_input = input("请选择标签，用逗号分隔：").split(',')
                    tags = [tag.strip() for tag in tags_input]


if __name__ == "__main__":
    # 实例化名字生成器
    name_gen = NameGenerator()
    # 开始生成流程
    name_gen.start_generation()
