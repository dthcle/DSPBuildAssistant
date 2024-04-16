import logging
from typing import List, Union, Literal

from item import Item

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class Craft:
    Assembler = "制造设备"  # 制造台
    Smelter = "冶炼设备"  # 冶炼设备
    ChemicalPlant = "化工设备"  # 化工厂
    Fractionator = "分馏设备"  # 分馏器
    MiniatureParticleCollider = "MiniatureParticleCollider"
    OilRefinery = "精炼设备"
    # And So On
    # 没玩太多 没整完 欢迎补充


class Formula:
    # generate_time的单位是ms 比如1s生成时间的话 这个值就应该赋值为1000
    def __init__(self, target: Item, generate_time: int, craft: Union[Craft, List[Craft]], resource: str | List[Union[Item, str]]):
        self.target = target
        self.generate_time = generate_time
        self.craft = [craft, ] if isinstance(craft, Craft) else craft
        self.formula_dict = {}

        # 在字符串格式的formula上支持的分隔符
        self._support_separate = "+:, "

        if isinstance(resource, str):
            # formula_str格式应该为 "材料A*10+材料B+材料C*10" (不加*默认为1个)
            self.formula_dict = self._parse_formula_str(resource, separate="+")
        elif isinstance(resource, list):
            for each in resource:
                if isinstance(each, str):
                    item_name = each
                elif isinstance(each, Item):
                    item_name = each.name
                else:
                    logger.error("list {resource} must be consist of str or Item")
                    exit(1)
                if item_name in self.formula_dict:
                    self.formula_dict[item_name] += 1
                else:
                    self.formula_dict[item_name] = 1
        else:
            logger.error("param {resource} must be str or list")
            exit(1)

    def _parse_formula_str(self, formula_str: str, separate: str = "+") -> dict:
        if separate not in self._support_separate:
            logger.error(f"{{separate}} must be in {self._support_separate}, current {{separate}} is {separate}")
        item_list = formula_str.split(separate)
        formula_dict = {}
        for each_item_str in item_list:
            if "*" in each_item_str:
                item_name, item_amount = each_item_str.split("*")
                formula_dict[item_name] = int(item_amount)
            else:
                formula_dict[each_item_str] = 1

        return formula_dict

