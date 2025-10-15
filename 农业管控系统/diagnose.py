# diagnose.py
import os
import sys


def check_file_contents():
    """检查关键文件内容"""
    print("🔍 检查文件内容...")

    files_to_check = {
        'weather_system.py': 'D:\\农业管控系统\\agriculture_system\\core\\weather_system.py',
        'core_init.py': 'D:\\农业管控系统\\agriculture_system\\core\\__init__.py',
        'main_init.py': 'D:\\农业管控系统\\agriculture_system\\__init__.py'
    }

    for file_name, file_path in files_to_check.items():
        print(f"\n📁 检查 {file_name}:")
        if os.path.exists(file_path):
            print(f"   ✅ 文件存在: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 检查关键内容
                if file_name == 'weather_system.py':
                    if 'class WeatherSystem' in content:
                        print("   ✅ 包含 WeatherSystem 类")
                    else:
                        print("   ❌ 缺少 WeatherSystem 类")

                if file_name.endswith('__init__.py'):
                    if 'WeatherSystem' in content:
                        print("   ✅ 导入了 WeatherSystem")
                    else:
                        print("   ❌ 未导入 WeatherSystem")

            except Exception as e:
                print(f"   ❌ 读取文件失败: {e}")
        else:
            print(f"   ❌ 文件不存在: {file_path}")


def test_direct_import():
    """直接测试导入"""
    print("\n🧪 直接测试导入...")

    try:
        # 直接导入 weather_system 模块
        from agriculture_system.core import weather_system
        print("   ✅ 成功导入 weather_system 模块")

        # 检查模块内容
        if hasattr(weather_system, 'WeatherSystem'):
            print("   ✅ weather_system 模块包含 WeatherSystem 类")

            # 测试实例化
            ws = weather_system.WeatherSystem()
            print("   ✅ 成功创建 WeatherSystem 实例")

        else:
            print("   ❌ weather_system 模块不包含 WeatherSystem 类")
            print(f"     模块内容: {dir(weather_system)}")

    except Exception as e:
        print(f"   ❌ 导入失败: {e}")


def check_package_structure():
    """检查包结构"""
    print("\n📦 检查包结构...")

    base_path = "D:\\农业管控系统\\agriculture_system"

    if os.path.exists(base_path):
        print(f"✅ 包目录存在: {base_path}")

        for root, dirs, files in os.walk(base_path):
            level = root.replace(base_path, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f'{indent}📁 {os.path.basename(root)}/')
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                if file.endswith('.py'):
                    print(f'{subindent}📄 {file}')
    else:
        print(f"❌ 包目录不存在: {base_path}")


if __name__ == "__main__":
    print("=" * 60)
    print("农业系统 - 问题诊断工具")
    print("=" * 60)

    check_package_structure()
    check_file_contents()
    test_direct_import()

    print("\n💡 建议:")
    print("1. 如果文件内容不正确，请用上面提供的代码替换")
    print("2. 确保所有文件使用UTF-8编码")
    print("3. 重新运行: pip install -e .")