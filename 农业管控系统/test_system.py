# test_system.py
import sys
import os


def test_imports():
    """测试所有模块导入"""
    print("🧪 开始测试系统模块导入...")

    modules_to_test = [
        "agriculture_system",
        "agriculture_system.core.weather_system",
        "agriculture_system.core.temperature_monitor",
        "agriculture_system.core.pest_monitor",
        "agriculture_system.core.growth_simulator",
        "agriculture_system.core.humidity_monitor",
        "agriculture_system.core.data_analyzer",
        "agriculture_system.core.alert_system",
        "agriculture_system.cli.main"
    ]

    for module_name in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {module_name} - 导入成功")
        except ImportError as e:
            print(f"❌ {module_name} - 导入失败: {e}")

    print("\n🎯 测试完成!")


def test_basic_functionality():
    """测试基本功能"""
    print("\n🧪 测试基本功能...")

    try:
        from agriculture_system.core.weather_system import WeatherSystem
        from agriculture_system.core.data_analyzer import DataAnalyzer

        # 测试天气系统
        weather = WeatherSystem()
        forecast = weather.get_weather_forecast("北京", 2)
        print(f"✅ 天气系统 - 生成 {len(forecast)} 天预报")

        # 测试数据分析
        analyzer = DataAnalyzer()
        recommendations = analyzer.recommend_crops("北京", "壤土", {})
        print(f"✅ 数据分析 - 生成 {len(recommendations)} 个作物推荐")

        print("🎯 基本功能测试通过!")

    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")


if __name__ == "__main__":
    print("=" * 50)
    print("农业智能系统 - 安装验证测试")
    print("=" * 50)

    test_imports()
    test_basic_functionality()

    print("\n📋 使用说明:")
    print("1. 分析功能: agri-system analyze --location 北京 --crop 番茄")
    print("2. 监控功能: agri-system monitor --location 我的农场 --interval 10")
    print("3. 演示功能: agri-system demo")
    print("4. 帮助信息: agri-system --help")