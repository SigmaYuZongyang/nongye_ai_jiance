# verify_fix.py
import sys
import os


def verify_imports():
    """验证所有导入"""
    print("🔍 验证导入...")

    imports_to_test = [
        "from agriculture_system.core.weather_system import WeatherSystem, EnhancedWeatherSystem",
        "from agriculture_system.core.temperature_monitor import TemperatureMonitor",
        "from agriculture_system.core.data_analyzer import DataAnalyzer",
        "from agriculture_system.core.growth_simulator import GrowthSimulator",
        "from agriculture_system.cli.main import cli, main"
    ]

    all_success = True

    for import_stmt in imports_to_test:
        try:
            exec(import_stmt)
            print(f"✅ {import_stmt}")
        except Exception as e:
            print(f"❌ {import_stmt}")
            print(f"   错误: {e}")
            all_success = False

    return all_success


def test_functionality():
    """测试功能"""
    print("\n🔍 测试功能...")

    try:
        from agriculture_system.core.weather_system import WeatherSystem
        from agriculture_system.core.data_analyzer import DataAnalyzer
        from agriculture_system.core.growth_simulator import GrowthSimulator

        # 测试天气系统
        weather = WeatherSystem()
        forecast = weather.get_weather_forecast("测试", 2)
        print(f"✅ 天气系统: 生成 {len(forecast)} 天预报")

        # 测试数据分析
        analyzer = DataAnalyzer()
        recommendations = analyzer.recommend_crops("测试", "壤土", {})
        print(f"✅ 数据分析: 生成 {len(recommendations)} 个推荐")

        # 测试生长模拟
        simulator = GrowthSimulator()
        growth_data = simulator.simulate_growth("番茄", 3, {})
        print(f"✅ 生长模拟: 生成 {len(growth_data)} 天数据")

        return True

    except Exception as e:
        print(f"❌ 功能测试失败: {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("农业系统 - 修复验证")
    print("=" * 60)

    imports_ok = verify_imports()
    functionality_ok = test_functionality()

    print("\n" + "=" * 60)
    if imports_ok and functionality_ok:
        print("🎉 所有验证通过！系统现在应该可以正常工作了。")
        print("\n📋 接下来可以运行:")
        print("   agri-system --help")
        print("   agri-system analyze --location 北京 --crop 番茄")
        print("   agri-system demo")
    else:
        print("⚠️ 系统仍有问题，请检查上面的错误信息")