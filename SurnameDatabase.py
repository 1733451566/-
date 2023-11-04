from collections import namedtuple
import random

Surname = namedtuple("Surname", ["text", "tags"])

class SurnameDatabase:
    def __init__(self):
        # 用默认姓氏预填充数据库
        self.surnames = [
            Surname("赵", ["华北", "古代", "单姓"]),
            Surname("钱", ["商贸", "文雅", "单姓"]),
            Surname("孙", ["单姓"]),
            Surname("李", ["常见", "通用", "单姓"]),
            Surname("周", ["文化", "历史", "单姓"]),
            Surname("吴", ["江南", "文雅", "单姓"]),
            Surname("郑", ["华中", "历史", "单姓"]),
            Surname("王", ["常见", "通用", "单姓"]),
            Surname("冯", ["华北", "文雅", "单姓"]),
            Surname("陈", ["华南", "常见", "单姓"]),
            Surname("褚", ["少见", "独特", "单姓"]),
            Surname("卫", ["华北", "历史", "单姓"]),
            Surname("蒋", ["华东", "单姓"]),
            Surname("沈", ["江南", "古典", "单姓"]),
            Surname("韩", ["文雅", "单姓"]),
            Surname("杨", ["通用", "积极", "单姓"]),
            Surname("朱", ["华东", "历史", "单姓"]),
            Surname("秦", ["古代", "历史", "单姓", "霸气"]),
            Surname("尤", ["少见", "独特", "单姓"]),
            Surname("许", ["华东", "通用", "单姓"]),
            Surname("何", ["华南", "常见", "单姓"]),
            Surname("吕", ["华北", "历史", "单姓"]),
            Surname("施", ["文雅", "江南", "单姓"]),
            Surname("张", ["常见", "通用", "单姓"]),
            Surname("孔", ["儒家", "文化", "单姓"]),
            Surname("曹", ["文化", "历史", "单姓"]),
            Surname("严", ["严肃", "华东", "单姓"]),
            Surname("华", ["华南", "文雅", "单姓"]),
            Surname("金", ["商贸", "华北", "单姓"]),
            Surname("魏", ["古代", "历史", "单姓"]),
            Surname("陶", ["文化", "单姓"]),
            Surname("姜", ["古风", "单姓"]),
            Surname("戚", ["少见", "单姓"]),
            Surname("谢", ["江南", "单姓"]),
            Surname("邹", ["历史", "单姓"]),
            Surname("喻", ["文雅", "单姓"]),
            Surname("柏", ["自然", "单姓"]),
            Surname("水", ["文雅", "稀有", "单姓"]),
            Surname("窦", ["古代", "单姓"]),
            Surname("章", ["文化", "单姓"]),
            Surname("云", ["自然", "文雅", "单姓"]),
            Surname("苏", ["文雅", "江南", "单姓"]),
            Surname("潘", ["江南", "单姓"]),
            Surname("葛", ["古风", "单姓"]),
            Surname("奚", ["稀有", "古风", "单姓"]),
            Surname("范", ["通用", "单姓"]),
            Surname("彭", ["历史", "单姓"]),
            Surname("郎", ["文化", "单姓"]),
            Surname("鲁", ["历史", "单姓"]),
            Surname("韦", ["少见", "单姓"]),
            Surname("昌", ["阳光", "单姓"]),
            Surname("马", ["通用", "单姓"]),
            Surname("苗", ["少见", "民族", "单姓"]),
            Surname("凤", ["特殊", "单姓"]),
            Surname("花", ["自然", "单姓"]),
            Surname("方", ["方正", "单姓"]),
            Surname("俞", ["江南", "单姓"]),
            Surname("任", ["文化", "单姓"]),
            Surname("袁", ["历史", "单姓"]),
            Surname("柳", ["文雅", "自然", "单姓"])
            # ... 根据需要添加更多姓氏
        ]

    def get_surnames_by_tags(self, tags):
        # 按照标签筛选姓氏
        if not tags:  # 如果没有指定标签，返回所有姓氏
            return self.surnames
        else:
            # 只返回包含所有指定标签的姓氏
            return [surname for surname in self.surnames if all(tag in surname.tags for tag in tags)]

    def get_random_surname(self, tags, random_state):
        # 根据标签获取筛选后的姓氏列表
        matching_surnames = self.get_surnames_by_tags(tags)
        # 如果有匹配的姓氏，随机选择一个返回；如果没有，返回None
        return random_state.choice(matching_surnames) if matching_surnames else None