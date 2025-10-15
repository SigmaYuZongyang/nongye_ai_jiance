# web_interface.py
from flask import Flask, render_template, request, jsonify, session
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.secret_key = 'agriculture_system_secret_key'


class AgricultureWebInterface:
    """农业系统Web界面"""

    def __init__(self, agriculture_system):
        self.agri_system = agriculture_system
        self.setup_routes()

    def setup_routes(self):
        """设置Web路由"""

        @app.route('/')
        def index():
            """主仪表板"""
            return render_template('index.html')

        @app.route('/api/current_status')
        def get_current_status():
            """获取当前系统状态"""
            status = {
                'temperature': self.agri_system.temp_monitor.read_temperature(),
                'air_humidity': self.agri_system.humidity_monitor.read_air_humidity(),
                'soil_humidity': self.agri_system.humidity_monitor.read_soil_humidity(),
                'timestamp': datetime.now().isoformat()
            }
            return jsonify(status)

        @app.route('/api/weather_forecast')
        def get_weather_forecast():
            """获取天气预报"""
            location = request.args.get('location', '北京')
            forecast = self.agri_system.weather_system.get_weather_forecast(location, 3)
            return jsonify(forecast)

        @app.route('/api/crop_recommendation')
        def get_crop_recommendation():
            """获取作物推荐"""
            location = request.args.get('location', '北京')
            soil_type = request.args.get('soil_type', '壤土')

            climate_data = {
                'avg_temperature': 25  # 从数据库获取实际数据
            }

            recommendations = self.agri_system.data_analyzer.recommend_crops(
                location, soil_type, climate_data
            )
            return jsonify(recommendations[:5])

        @app.route('/api/start_monitoring', methods=['POST'])
        def start_monitoring():
            """开始监控"""
            data = request.json
            location = data.get('location', '默认农场')
            interval = data.get('interval', 60)

            self.agri_system.start_monitoring(location, interval)
            return jsonify({'status': '监控已启动'})

        @app.route('/api/stop_monitoring', methods=['POST'])
        def stop_monitoring():
            """停止监控"""
            self.agri_system.stop_monitoring()
            return jsonify({'status': '监控已停止'})

        @app.route('/api/growth_simulation')
        def growth_simulation():
            """生长模拟"""
            crop_type = request.args.get('crop_type', '番茄')
            days = int(request.args.get('days', 7))

            conditions = {
                'temperature': 25,
                'humidity': 65
            }

            simulation = self.agri_system.growth_simulator.simulate_growth(
                crop_type, days, conditions
            )
            return jsonify(simulation)

        @app.route('/api/alerts')
        def get_alerts():
            """获取报警信息"""
            alerts = self.agri_system.alert_system.alerts[-10:]  # 最近10条报警
            return jsonify(alerts)


# HTML模板文件 (templates/index.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title>农业智能栽培系统</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>农业智能栽培系统控制面板</h1>

    <div class="dashboard">
        <div class="status-card">
            <h3>当前环境状态</h3>
            <div id="current-status">加载中...</div>
        </div>

        <div class="control-panel">
            <h3>系统控制</h3>
            <button onclick="startMonitoring()">开始监控</button>
            <button onclick="stopMonitoring()">停止监控</button>
        </div>

        <div class="chart-container">
            <canvas id="environmentChart"></canvas>
        </div>
    </div>

    <script>
        // 这里添加前端JavaScript代码来更新界面和图表
    </script>
</body>
</html>
"""