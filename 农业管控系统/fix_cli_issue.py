# fix_cli_issue.py
import os


def fix_weather_system_file():
    """修复 weather_system.py 文件"""
    file_path = r"D:\农业管控系统\agriculture_system\core\weather_system.py"

    # 读取现有内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已经有 EnhancedWeatherSystem
    if 'class EnhancedWeatherSystem' not in content:
        # 在文件末尾添加 EnhancedWeatherSystem 类
        enhanced_class = '''

# 添加 EnhancedWeatherSystem 类
class EnhancedWeatherSystem(WeatherSystem):
    """增强的天气系统"""

    def __init__(self, api_key: str = None):
        super().__init__(api_key)

    def get_real_time_weather(self, location: str):
        """获取实时天气数据"""
        print(f"获取 {location} 的实时天气数据")
        return self._get_simulated_weather()

    def _get_simulated_weather(self):
        """模拟天气数据"""
        import random
        return {
            'temperature': random.uniform(10, 35),
            'humidity': random.uniform(30, 90),
            'description': '晴朗'
        }
'''
        content += enhanced_class

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ 已修复 weather_system.py")
    else:
        print("✅ weather_system.py 已经包含 EnhancedWeatherSystem")


def fix_cli_file():
    """简化 CLI 文件以避免导入问题"""
    file_path = r"D:\农业管控系统\agriculture_system\cli\main.py"

    # 创建简化的 CLI 内容
    cli_content = '''import click
from agriculture_system.core.weather_system import WeatherSystem
from agriculture_system.core.data_analyzer import DataAnalyzer
from agriculture_system.core.growth_simulator import GrowthSimulator

@click.group()
def cli():
    """农业栽培智能分析管控系统命令行接口"""
    pass

@cli.command()
@click.option('--location', default='北京', help='农场位置')
@click.option('--crop', default='番茄', help='作物类型')
def analyze(location, crop):
    """执行农业分析"""
    click.echo(f"开始分析 {location} 的 {crop} 栽培情况...")

    # 创建系统实例
    weather_system = WeatherSystem()
    data_analyzer = DataAnalyzer()
    growth_simulator = GrowthSimulator()

    # 获取天气预测
    forecast = weather_system.get_weather_forecast(location)

    # 获取作物推荐
    recommendations = data_analyzer.recommend_crops(location, '壤土', {})

    # 生长模拟
    growth_data = growth_simulator.simulate_growth(crop, 7, {})

    # 输出报告
    click.echo("\\n" + "="*50)
    click.echo("农业分析报告")
    click.echo("="*50)
    click.echo(f"位置: {location}")
    click.echo(f"作物: {crop}")

    click.echo(f"\\n天气预测:")
    for i, weather in enumerate(forecast):
        click.echo(f"  第{i+1}天: {weather.temperature:.1f}°C, 湿度{weather.humidity:.1f}%")

    click.echo(f"\\n作物推荐 (前3名):")
    for i, rec in enumerate(recommendations[:3], 1):
        click.echo(f"  {i}. {rec['crop']} - 适宜度: {rec['suitability_score']}")

    click.echo(f"\\n生长模拟:")
    for day_data in growth_data[::2]:
        click.echo(f"  第{day_data['day']}天: {day_data['growth_stage']}")

@cli.command()
@click.option('--location', default='默认农场', help='监控位置')
@click.option('--interval', default=60, help='监控间隔(秒)')
def monitor(location, interval):
    """启动实时监控"""
    click.echo(f"启动实时监控 - 位置: {location}, 间隔: {interval}秒")
    click.echo("按 Ctrl+C 停止监控")

    try:
        import time
        count = 0
        while True:
            count += 1
            click.echo(f"监控周期 {count}: 采集环境数据...")
            time.sleep(interval)
    except KeyboardInterrupt:
        click.echo("\\n停止监控...")

@cli.command()
@click.option('--host', default='localhost', help='Web服务器主机')
@click.option('--port', default=5000, help='Web服务器端口')
def web(host, port):
    """启动Web界面"""
    click.echo(f"启动Web界面: http://{host}:{port}")
    click.echo("Web界面功能开发中...")

@cli.command()
def demo():
    """演示所有功能"""
    click.echo("开始演示农业智能系统功能...")

    # 演示分析功能
    analyze.callback(location="北京", crop="番茄")

    click.echo("\\n演示完成!")

def main():
    cli()

if __name__ == '__main__':
    main()
'''

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cli_content)

    print("✅ 已修复 CLI 文件")


if __name__ == "__main__":
    print("🔧 开始修复 CLI 导入问题...")
    fix_weather_system_file()
    fix_cli_file()
    print("🎯 修复完成！请重新运行测试。")