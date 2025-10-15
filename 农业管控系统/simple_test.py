# simple_test.py
try:
    from agriculture_system.core.weather_system import WeatherSystem
    print("✅ 成功导入 WeatherSystem")
    ws = WeatherSystem()
    print("✅ 成功创建 WeatherSystem 实例")
except Exception as e:
    print(f"❌ 导入失败: {e}")