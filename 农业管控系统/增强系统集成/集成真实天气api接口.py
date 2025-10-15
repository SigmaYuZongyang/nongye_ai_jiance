# weather_service.py
import requests
import json
from datetime import datetime, timedelta
from typing import Dict, Optional


class RealWeatherService:
    """真实天气API服务"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city: str, country: str = "CN") -> Optional[Dict]:
        """获取当前天气数据"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': f"{city},{country}",
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'zh_cn'
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            return {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed'],
                'timestamp': datetime.now()
            }
        except Exception as e:
            print(f"获取天气数据失败: {e}")
            return None

    def get_forecast(self, city: str, days: int = 3, country=None) -> Optional[Dict]:
        """获取天气预报"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': f"{city},{country}",
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'zh_cn'
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            forecasts = []

            for item in data['list'][:days * 8]:  # 每3小时一个数据点
                forecast_time = datetime.fromtimestamp(item['dt'])
                forecasts.append({
                    'timestamp': forecast_time,
                    'temperature': item['main']['temp'],
                    'humidity': item['main']['humidity'],
                    'description': item['weather'][0]['description'],
                    'rainfall': item.get('rain', {}).get('3h', 0)
                })

            return forecasts
        except Exception as e:
            print(f"获取天气预报失败: {e}")
            return None


class WeatherSystem(object):
    pass


class EnhancedWeatherSystem(WeatherSystem):
    """增强的天气系统，集成真实API"""

    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        self.real_weather_service = RealWeatherService(api_key) if api_key else None

    def get_real_time_weather(self, location: str) -> Optional[Dict]:
        """获取实时天气数据"""
        if self.real_weather_service:
            return self.real_weather_service.get_current_weather(location)
        else:
            print("未配置天气API密钥，使用模拟数据")
            return self._get_simulated_weather()

    def get_enhanced_forecast(self, location: str, days: int = 3) -> Optional[Dict]:
        """获取增强的天气预报"""
        if self.real_weather_service:
            return self.real_weather_service.get_forecast(location, days)
        else:
            print("未配置天气API密钥，使用模拟数据")
            return super().get_weather_forecast(location, days)