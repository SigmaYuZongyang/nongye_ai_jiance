# agriculture_system/core/growth_simulator.py
import random
from typing import Dict, List


class GrowthSimulator:
    """作物生长过程模拟系统"""

    def __init__(self):
        self.growth_models = {
            '水稻': self._rice_growth_model,
            '小麦': self._wheat_growth_model,
            '玉米': self._corn_growth_model,
            '番茄': self._tomato_growth_model
        }

    def simulate_growth(self, crop_type: str, days: int, conditions: Dict) -> List[Dict]:
        """模拟作物生长过程"""
        if crop_type not in self.growth_models:
            raise ValueError(f"不支持 {crop_type} 的生长模拟")

        growth_data = []
        model = self.growth_models[crop_type]

        for day in range(days):
            growth_stage = model(day, conditions)
            growth_data.append({
                'day': day + 1,
                'growth_stage': growth_stage['stage'],
                'height': growth_stage['height'],
                'health': growth_stage['health'],
                'yield_potential': growth_stage['yield']
            })

        return growth_data

    def _rice_growth_model(self, day: int, conditions: Dict) -> Dict:
        """水稻生长模型"""
        stages = ['发芽期', '苗期', '分蘖期', '拔节期', '抽穗期', '开花期', '成熟期']
        stage_index = min(day // 15, len(stages) - 1)

        return {
            'stage': stages[stage_index],
            'height': min(1.2, 0.1 + day * 0.02),
            'health': random.uniform(0.7, 0.95),
            'yield': min(1.0, day * 0.01)
        }

    def _wheat_growth_model(self, day: int, conditions: Dict) -> Dict:
        """小麦生长模型"""
        stages = ['出苗期', '分蘖期', '拔节期', '孕穗期', '抽穗期', '开花期', '灌浆期', '成熟期']
        stage_index = min(day // 10, len(stages) - 1)

        return {
            'stage': stages[stage_index],
            'height': min(1.0, 0.05 + day * 0.015),
            'health': random.uniform(0.75, 0.98),
            'yield': min(1.0, day * 0.012)
        }

    def _corn_growth_model(self, day: int, conditions: Dict) -> Dict:
        """玉米生长模型"""
        stages = ['发芽期', '苗期', '拔节期', '大喇叭口期', '抽雄期', '开花期', '灌浆期', '成熟期']
        stage_index = min(day // 12, len(stages) - 1)

        return {
            'stage': stages[stage_index],
            'height': min(2.5, 0.1 + day * 0.04),
            'health': random.uniform(0.7, 0.96),
            'yield': min(1.0, day * 0.008)
        }

    def _tomato_growth_model(self, day: int, conditions: Dict) -> Dict:
        """番茄生长模型"""
        stages = ['发芽期', '苗期', '开花期', '坐果期', '果实膨大期', '成熟期']
        stage_index = min(day // 10, len(stages) - 1)

        return {
            'stage': stages[stage_index],
            'height': min(1.5, 0.05 + day * 0.025),
            'health': random.uniform(0.65, 0.94),
            'yield': min(1.0, day * 0.015)
        }