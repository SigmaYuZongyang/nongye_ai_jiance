# fix_imports.py
import os
import shutil


def create_core_files():
    """创建核心文件"""
    core_dir = "D:\\农业管控系统\\agriculture_system\\core"

    # 确保目录存在
    os.makedirs(core_dir, exist_ok=True)

    # 创建 weather_system.py
    weather_content = '''import random
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List

@dataclass
class WeatherData:
    temperature: float
    humidity: float
    rainfall: float
    wind_speed: float
    timestamp: datetime

class WeatherSystem:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.weather_history = []

    def get_weather_forecast(self, location: str, days: int = 3):
        forecasts = []
        current_time = datetime.now()

        for i in range(days):
            forecast_time = current_time + timedelta(days=i)
            weather = WeatherData(
                temperature=random.uniform(15, 35),
                humidity=random.uniform(30, 90),
                rainfall=random.uniform(0, 50),
                wind_speed=random.uniform(0, 15),
                timestamp=forecast_time
            )
            forecasts.append(weather)

        print(f"已生成未来{days}天天气预测")
        return forecasts
'''

    with open(os.path.join(core_dir, "weather_system.py"), "w", encoding="utf-8") as f:
        f.write(weather_content)

    print("✅ 创建 weather_system.py")

    # 创建 core/__init__.py
    core_init_content = '''from .weather_system import WeatherSystem, WeatherData

__all__ = ['WeatherSystem', 'WeatherData']
'''

    with open(os.path.join(core_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write(core_init_content)

    print("✅ 创建 core/__init__.py")

    # 创建主 __init__.py
    main_init_content = '''from .core.weather_system import WeatherSystem, WeatherData

__version__ = "1.0.0"
__all__ = ['WeatherSystem', 'WeatherData']
'''

    with open("D:\\农业管控系统\\agriculture_system\\__init__.py", "w", encoding="utf-8") as f:
        f.write(main_init_content)

    print("✅ 创建主 __init__.py")


if __name__ == "__main__":
    print("🔧 开始修复导入问题...")
    create_core_files()
    print("🎯 修复完成！请重新运行: pip install -e .")