# agriculture_system/web/app.py
from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime


def create_app(agriculture_system):
    """创建Flask应用"""
    app = Flask(__name__)
    app.agriculture_system = agriculture_system

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/status')
    def get_status():
        """获取系统状态"""
        status = {
            'is_running': app.agriculture_system.is_running,
            'timestamp': datetime.now().isoformat(),
            'version': '1.0.0'
        }
        return jsonify(status)

    @app.route('/api/analyze', methods=['POST'])
    def analyze():
        """执行分析"""
        data = request.json
        location = data.get('location', '北京')
        crop_type = data.get('crop_type', '番茄')

        report = app.agriculture_system.generate_report(location, crop_type)
        return jsonify(report)

    @app.route('/api/start_monitoring', methods=['POST'])
    def start_monitoring():
        """开始监控"""
        data = request.json
        location = data.get('location', '默认农场')
        interval = data.get('interval', 60)

        app.agriculture_system.start(location, interval)
        return jsonify({'status': '监控已启动'})

    @app.route('/api/stop_monitoring', methods=['POST'])
    def stop_monitoring():
        """停止监控"""
        app.agriculture_system.stop()
        return jsonify({'status': '监控已停止'})

    return app


def main():
    """Web服务器主函数"""
    from ..core.main_system import EnhancedAgricultureIntelligentSystem

    # 创建系统实例
    system = EnhancedAgricultureIntelligentSystem()

    # 创建Flask应用
    app = create_app(system)

    # 启动服务器
    app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == '__main__':
    main()