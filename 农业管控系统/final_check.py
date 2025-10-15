# final_check.py
def comprehensive_test():
    """全面测试"""
    print("🎯 开始全面系统测试...")

    tests = [
        ("天气系统", "from agriculture_system.core.weather_system import WeatherSystem"),
        ("温度监控", "from agriculture_system.core.temperature_monitor import TemperatureMonitor"),
        ("数据分析", "from agriculture_system.core.data_analyzer import DataAnalyzer"),
        ("生长模拟", "from agriculture_system.core.growth_simulator import GrowthSimulator"),
        ("病虫害监控", "from agriculture_system.core.pest_monitor import PestVirusMonitor"),
        ("湿度监控", "from agriculture_system.core.humidity_monitor import HumidityMonitor"),
        ("报警系统", "from agriculture_system.core.alert_system import AlertSystem"),
        ("CLI接口", "from agriculture_system.cli.main import cli")
    ]

    all_passed = True

    for test_name, import_stmt in tests:
        try:
            exec(import_stmt)
            print(f"✅ {test_name} - 通过")
        except Exception as e:
            print(f"❌ {test_name} - 失败: {e}")
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有测试通过！系统安装成功！")
        print("\n📋 现在您可以运行以下命令:")
        print("  agri-system analyze --location 北京 --crop 番茄")
        print("  agri-system monitor --location 我的农场 --interval 10")
        print("  agri-system demo")
        print("  agri-system --help")
    else:
        print("⚠️ 部分测试失败，需要进一步检查")

    return all_passed


if __name__ == "__main__":
    comprehensive_test()