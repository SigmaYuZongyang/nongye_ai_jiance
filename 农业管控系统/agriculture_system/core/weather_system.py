import random
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


class EnhancedWeatherSystem(WeatherSystem):
    """增强的天气系统，集成真实API"""

    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        # 这里可以初始化真实天气服务，但我们现在只是模拟
        self.real_weather_service = None  # 实际中这里可能是RealWeatherService(api_key)

    def get_real_time_weather(self, location: str):
        """获取实时天气数据"""
        # 如果配置了真实API，则使用真实数据，否则使用模拟数据
        if self.real_weather_service:
            return self.real_weather_service.get_current_weather(location)
        else:
            # 模拟数据
            return {
                'temperature': random.uniform(10, 35),
                'humidity': random.uniform(30, 90),
                'description': '晴朗'
            }