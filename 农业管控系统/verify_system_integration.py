# verify_system_integration.py
import sys
import os


def test_system_integration():
    """测试系统集成功能"""
    print("🔗 系统集成测试")
    print("=" * 50)

    # 测试所有核心模块
    modules = {
        "WeatherSystem": "agriculture_system.core.weather_system",
        "DataAnalyzer": "agriculture_system.core.data_analyzer",
        "GrowthSimulator": "agriculture_system.core.growth_simulator",
        "TemperatureMonitor": "agriculture_system.core.temperature_monitor",
        "PestVirusMonitor": "agriculture_system.core.pest_monitor",
        "HumidityMonitor": "agriculture_system.core.humidity_monitor",
        "CLI Interface": "agriculture_system.cli.main"
    }

    all_working = True

    for name, module_path in modules.items():
        try:
            module = __import__(module_path, fromlist=[name])
            print(f"✅ {name} - 模块加载成功")

            # 测试具体功能
            if name == "WeatherSystem":
                ws = getattr(module, 'WeatherSystem')()
                forecast = ws.get_weather_forecast("测试", 2)
                print(f"   📅 生成 {len(forecast)} 天天气预报")

            elif name == "DataAnalyzer":
                da = getattr(module, 'DataAnalyzer')()
                recs = da.recommend_crops("测试", "壤土", {})
                print(f"   🌾 生成 {len(recs)} 个作物推荐")

            elif name == "GrowthSimulator":
                gs = getattr(module, 'GrowthSimulator')()
                growth = gs.simulate_growth("番茄", 3, {})
                print(f"   🌱 模拟 {len(growth)} 天生长")

        except Exception as e:
            print(f"❌ {name} - 加载失败: {e}")
            all_working = False

    return all_working


def test_cli_commands():
    """测试CLI命令"""
    print("\n🖥️ CLI命令测试")
    print("=" * 50)

    try:
        from agriculture_system.cli.main import cli, main

        # 获取所有命令
        commands = []
        for cmd in cli.commands.values():
            commands.append({
                'name': cmd.name,
                'help': cmd.help
            })

        print("✅ CLI接口正常")
        print("可用命令:")
        for cmd in commands:
            print(f"   {cmd['name']}: {cmd['help']}")

        return True

    except Exception as e:
        print(f"❌ CLI测试失败: {e}")
        return False


def show_integration_demo():
    """展示集成功能演示"""
    print("\n🎯 集成功能演示")
    print("=" * 50)

    try:
        from agriculture_system.core.weather_system import WeatherSystem
        from agriculture_system.core.data_analyzer import DataAnalyzer
        from agriculture_system.core.growth_simulator import GrowthSimulator

        print("模拟完整的农业分析流程:")
        print()

        # 1. 天气分析
        weather = WeatherSystem()
        forecast = weather.get_weather_forecast("演示农场", 2)
        print("1. 🌤️ 天气分析完成")
        for i, w in enumerate(forecast):
            print(f"   第{i + 1}天: {w.temperature:.1f}°C, {w.humidity:.1f}%湿度")

        # 2. 作物推荐
        analyzer = DataAnalyzer()
        recommendations = analyzer.recommend_crops("演示农场", "壤土", {})
        print("\n2. 🌿 作物推荐完成")
        for rec in recommendations[:2]:
            print(f"   {rec['crop']}: 适宜度 {rec['suitability_score']}")

        # 3. 生长模拟
        simulator = GrowthSimulator()
        growth_data = simulator.simulate_growth("番茄", 3, {})
        print("\n3. 🌱 生长模拟完成")
        for day in growth_data:
            print(f"   第{day['day']}天: {day['growth_stage']}")

        print("\n🎉 所有功能集成正常！")
        return True

    except Exception as e:
        print(f"❌ 演示失败: {e}")
        return False


if __name__ == "__main__":
    print("农业智能系统 - 集成验证")
    print("=" * 60)

    module_test = test_system_integration()
    cli_test = test_cli_commands()
    demo_test = show_integration_demo()

    print("\n" + "=" * 60)
    if all([module_test, cli_test, demo_test]):
        print("🎊 系统集成验证通过！")
        print("\n📋 您现在可以:")
        print("   1. 使用启动器访问所有功能")
        print("   2. 进行完整的农业分析")
        print("   3. 启动实时监控")
        print("   4. 查看功能演示")
    else:
        print("⚠️ 系统集成存在问题，请检查")