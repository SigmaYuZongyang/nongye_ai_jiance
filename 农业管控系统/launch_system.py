# launch_system.py
import os
import sys
import subprocess


def clear_screen():
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    """显示菜单"""
    clear_screen()
    print("=" * 50)
    print("农业栽培智能分析管控系统")
    print("=" * 50)
    print()
    print("请选择功能:")
    print("1. 农业分析")
    print("2. 实时监控")
    print("3. 功能演示")
    print("4. 帮助信息")
    print("5. 快速开始")
    print("6. 退出系统")
    print()


def run_analysis():
    """运行分析功能"""
    print("\n农业分析功能")
    print("-" * 20)

    location = input("请输入地点 (默认: 北京): ").strip()
    crop = input("请输入作物类型 (默认: 番茄): ").strip()

    if not location:
        location = "云南"
    if not crop:
        crop = "土豆"

    print(f"\n开始分析 {crop} 在 {location} 的栽培情况...")
    cmd = [sys.executable, "-m", "agriculture_system.cli.main", "analyze",
           "--location", location, "--crop", crop]
    subprocess.run(cmd)


def run_monitoring():
    """运行监控功能"""
    print("\n实时监控功能")
    print("-" * 20)

    location = input("请输入监控地点 (默认: 我的农场): ").strip()
    interval = input("请输入监控间隔秒数 (默认: 10): ").strip()

    if not location:
        location = "我的农场"
    if not interval:
        interval = "10"

    print(f"\n启动监控，按 Ctrl+C 停止...")
    cmd = [sys.executable, "-m", "agriculture_system.cli.main", "monitor",
           "--location", location, "--interval", interval]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n监控已停止")


def run_demo():
    """运行演示功能"""
    print("\n开始系统功能演示...")
    cmd = [sys.executable, "-m", "agriculture_system.cli.main", "demo"]
    subprocess.run(cmd)


def show_help():
    """显示帮助信息"""
    print("\n系统帮助信息")
    cmd = [sys.executable, "-m", "agriculture_system.cli.main", "--help"]
    subprocess.run(cmd)


def quick_start():
    """快速开始"""
    print("\n快速开始 - 分析云南玉米栽培...")
    cmd = [sys.executable, "-m", "agriculture_system.cli.main", "analyze",
           "--location", "云南", "--crop", "玉米"]
    subprocess.run(cmd)


def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请输入选择 (1-6): ").strip()

        if choice == '1':
            run_analysis()
        elif choice == '2':
            run_monitoring()
        elif choice == '3':
            run_demo()
        elif choice == '4':
            show_help()
        elif choice == '5':
            quick_start()
        elif choice == '6':
            print("\n感谢使用农业智能系统！")
            break
        else:
            print("无效选择，请重新输入")
            input("按任意键继续...")
            continue

        if choice != '6':
            input("\n按任意键返回主菜单...")


if __name__ == "__main__":
    main()