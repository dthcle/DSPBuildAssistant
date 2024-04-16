import re
import logging
from typing import Union, Tuple

from formula import Formula, Craft

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class Item:
    def __init__(self, name, stack_limit):
        self.name = name  # 物品名称
        self.stack_limit = stack_limit  # 物品单格堆叠上限

        self.formulas = []  # 配方列表

    def add_formula(self, formula: Formula):
        self.formulas.append(formula)
        return self


class Building(Item):
    # interface表示建筑四面的接口数量 从短边开始计算
    # 此处并未考虑异形建筑 好像没见过
    def __init__(self, name, stack_limit, area: Tuple[int, int], interface: Tuple[int, int, int, int]):
        super(Building, self).__init__(name, stack_limit)
        self.area = area  # 建筑占地面积
        self.interface = interface  # 建筑接口数量

        self.storage = None  # 储物空间数量
        self.max_height = None  # 建筑垂直建造上限 tuple 分别对应0级到满级
        # self.requirement = None  # 科技需求 应该为 class Technology
        self.craft_type: Craft | None = None  # 建筑类型

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_max_height(self, max_height):
        self.max_height = max_height
        return self

    def set_craft_type(self, craft_type: Craft):
        self.craft_type = craft_type
        return self


class EnergyItem(Item):
    def __init__(self, name, stack_limit, energy, energy_acc):
        super(EnergyItem, self).__init__(name, stack_limit)
        self.energy = energy  # 一个物品所包含的能量
        self.energy_acc = energy_acc  # 用于机甲驱动的时候 获得的额外效率



