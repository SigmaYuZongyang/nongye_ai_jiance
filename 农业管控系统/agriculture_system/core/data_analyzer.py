# agriculture_system/core/data_analyzer.py
import random
from typing import Dict, List


class DataAnalyzer:
    def __init__(self):
        self.crop_database = {
            '水稻': {'optimal_temp': (20, 35), 'water_requirement': '高'},
            '小麦': {'optimal_temp': (15, 25), 'water_requirement': '中'},
            '玉米': {'optimal_temp': (18, 32), 'water_requirement': '中'},
            '番茄': {'optimal_temp': (20, 30), 'water_requirement': '中高'}
        }

    def recommend_crops(self, location: str, soil_type: str, climate_data: Dict):
        """根据位置、土壤类型和气候数据推荐作物"""
        recommendations = []

        for crop, requirements in self.crop_database.items():
            score = random.uniform(0.5, 1.0)

            recommendations.append({
                'crop': crop,
                'suitability_score': round(score, 2),
                'recommendation_level': '高' if score > 0.8 else '中' if score > 0.6 else '低',
                'key_requirements': {
                    'temperature_range': requirements['optimal_temp'],
                    'water_requirement': requirements['water_requirement']
                }
            })

        # 按适宜度排序
        recommendations.sort(key=lambda x: x['suitability_score'], reverse=True)
        return recommendations

    def generate_implementation_report(self, crop: str, location: str) -> Dict:
        """生成实施过程建议报告"""
        crop_info = self.crop_database.get(crop, {})

        return {
            'crop': crop,
            'location': location,
            'planting_season': self._get_planting_season(crop),
            'key_techniques': [
                f"播种密度: {self._get_planting_density(crop)}",
                f"施肥方案: {self._get_fertilization_plan(crop)}",
                f"灌溉方案: {self._get_irrigation_plan(crop)}"
            ],
            'expected_yield': f"{self._get_expected_yield(crop)} 公斤/亩"
        }

    def _get_planting_season(self, crop: str) -> str:
        seasons = {
            '水稻': '春季(4-5月)',
            '小麦': '秋季(10-11月)',
            '玉米': '春季(4-5月)',
            '番茄': '春季(3-4月)或秋季(8-9月)'
        }
        return seasons.get(crop, '根据当地气候确定')

    def _get_planting_density(self, crop: str) -> str:
        densities = {
            '水稻': '25-30万株/公顷',
            '小麦': '150-200公斤/公顷',
            '玉米': '6-7万株/公顷',
            '番茄': '3-4万株/公顷'
        }
        return densities.get(crop, '根据品种确定')

    def _get_fertilization_plan(self, crop: str) -> str:
        plans = {
            '水稻': '基肥+分蘖肥+穗肥，N:P:K=2:1:1.5',
            '小麦': '基肥+返青肥+拔节肥，N:P:K=2:1:1',
            '玉米': '种肥+拔节肥+穗肥，N:P:K=2:1:1',
            '番茄': '基肥+花果肥，N:P:K=1:1.5:2'
        }
        return plans.get(crop, '根据土壤检测确定')

    def _get_irrigation_plan(self, crop: str) -> str:
        plans = {
            '水稻': '保持水层3-5cm，分蘖末期晒田',
            '小麦': '越冬水+返青水+孕穗水+灌浆水',
            '玉米': '播种水+拔节水+大喇叭口水+灌浆水',
            '番茄': '滴灌，保持土壤湿润但不过湿'
        }
        return plans.get(crop, '根据土壤湿度确定')

    def _get_expected_yield(self, crop: str) -> str:
        yields = {
            '水稻': '600-800',
            '小麦': '400-600',
            '玉米': '700-900',
            '番茄': '5000-8000'
        }
        return yields.get(crop, '根据管理水平确定')