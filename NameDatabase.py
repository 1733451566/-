from collections import namedtuple
import random

Name = namedtuple("Name", ["text", "tags"])

class NameDatabase:
    def __init__(self):
        # 用默认名字预填充数据库
        self.names = [
            Name("遥", ["古风", "梦幻", "自然", "隽永", "文艺"]),
            Name("之", ["文雅", "书卷", "传统", "经典", "含蓄"]),
            Name("霄", ["自然", "宇宙", "远大", "豪迈", "古风"]),
            Name("凌", ["冷峻", "坚强", "高远", "文雅", "古风"]),
            Name("无", ["神秘", "另类", "极简", "抽象", "哲学"]),
            Name("浩", ["宏大", "豪迈", "气派", "深远", "浩瀚"]),
            Name("鸣", ["响亮", "自然", "生动", "表现", "音乐"]),
            Name("鸿", ["宏伟", "遥远", "丰富", "成功", "博大"]),
            Name("宏", ["宏大", "气宇", "远大", "开阔", "辉煌"]),
            Name("弘", ["宽广", "文化", "开扬", "扩张", "影响"]),
            Name("墨", ["文学", "沉稳", "深沉", "艺术", "文艺"]),
            Name("陌", ["陌生", "距离", "初见", "道路", "思念"]),
            Name("意", ["意境", "深远", "内涵", "情感", "哲理"]),
            Name("亦", ["平等", "亦然", "独特", "哲学"]),
            Name("宜", ["适宜", "恰当", "和谐", "平衡", ",雅致"]),
            Name("仪", ["规则", "礼节", "端庄", "和谐", "秩序"]),
            Name("逸", ["超脱", "安闲", "自在", "非凡", "闲适"]),
            Name("神", ["神秘", "古风", "传说", "超然", "豪迈"]),
            Name("凝", ["静谧", "深沉", "内敛", "冷峻", "雅致"]),
            Name("熙", ["温暖", "阳光", "和煦", "亲切", "明朗"]),
            Name("夕", ["夜晚", "宁静", "含蓄", "浪漫", "古风"]),
            Name("枫", ["自然", "秋天", "飘逸", "豪放", "文艺"]),
            Name("夜", ["神秘", "宁静", "深沉", "浪漫", "古风"]),
            Name("星", ["梦幻", "遥远", "科幻", "明亮", "希望"]),
            Name("君", ["尊贵", "古风", "文雅", "权威"]),
            Name("书", ["学识", "文雅", "传统", "书卷", "经典"]),
            Name("雅", ["文雅", "高洁", "典雅", "和谐", "古风"]),
            Name("狂", ["放纵", "自由", "激情", "热烈", "不羁"]),
            Name("钰", ["珍贵", "光彩", "坚硬", "富有", "闪耀"]),
            Name("琰", ["晶莹", "璀璨", "美玉", "贵重", "光亮"]),
            Name("燃", ["热情", "生命", "激昂", "光明", "力量"]),
            Name("雾", ["朦胧", "神秘", "自然", "轻柔", "变幻"]),
            Name("炎", ["热情", "强烈", "热烈", "阳光", "力量"]),
            Name("烟", ["轻盈", "飘渺", "朦胧", "悠长", "隐约"]),
            Name("颜", ["美丽", "外貌", "色彩", "和谐", "形象"]),
            Name("妍", ["美貌", "典雅", "温柔", "和谐", "明快"]),
            Name("宴", ["欢乐", "盛会", "喜庆", "享受", "繁华"]),
            Name("婵", ["美丽", "柔和", "女性", "婀娜", "优雅"]),
            Name("轩", ["高远", "开阔", "优雅", "飘逸", "升华"]),
            Name("烈", ["激烈", "强烈", "英勇", "刚毅", "热烈"]),
            Name("柏", ["坚韧", "自然", "繁茂", "古风", "雅致"]),
            Name("诗", ["文艺", "抒情", "优美", "浪漫", "文雅"]),
            Name("歌", ["欢快", "音乐", "悦耳", "自在", "表达"])
            # ... 根据需要添加更多名字
        ]


    def add_name(self, name):
        self.names.append(name)

    def get_names_by_tags(self, tags):
        return [name for name in self.names if set(tags).intersection(name.tags)]



