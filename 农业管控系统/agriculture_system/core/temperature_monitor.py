# agriculture_system/core/temperature_monitor.py
import random
from datetime import datetime
from typing import Optional


class TemperatureMonitor:
    """温度温差监控系统"""

    def __init__(self):
        self.temperature_readings = []
        self.max_temp_threshold = 35
        self.min_temp_threshold = 5

    def read_temperature(self) -> float:
        """模拟读取温度传感器数据"""
        temperature = random.uniform(10, 40)
        self.temperature_readings.append({
            'temperature': temperature,
            'timestamp': datetime.now()
        })
        return temperature

    def calculate_temperature_difference(self, hours: int = 24) -> float:
        """计算温差"""
        if len(self.temperature_readings) < 2:
            return 0

        recent_readings = self.temperature_readings[-hours:]
        temps = [r['temperature'] for r in recent_readings]

        return max(temps) - min(temps)

    def check_temperature_alert(self) -> Optional[str]:
        """检查温度异常报警"""
        if not self.temperature_readings:
            return None

        current_temp = self.temperature_readings[-1]['temperature']

        if current_temp > self.max_temp_threshold:
            return f"高温警报！当前温度: {current_temp:.1f}°C"
        elif current_temp < self.min_temp_threshold:
            return f"低温警报！当前温度: {current_temp:.1f}°C"

        return None