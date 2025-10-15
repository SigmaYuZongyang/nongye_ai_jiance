# database_manager.py
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any
from datetime import timedelta
#from mypy.typeshed.stdlib.datetime import timedelta


class AgricultureDatabase:
    """农业数据数据库管理"""

    def __init__(self, db_path: str = "agriculture_system.db"):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        """初始化数据库表结构"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # 创建天气数据表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                temperature REAL,
                humidity REAL,
                rainfall REAL,
                wind_speed REAL,
                location TEXT
            )
        ''')

        # 创建传感器数据表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                air_temperature REAL,
                soil_temperature REAL,
                air_humidity REAL,
                soil_humidity REAL,
                soil_ph REAL,
                light_intensity REAL
            )
        ''')

        # 创建作物生长数据表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crop_growth (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                crop_type TEXT,
                growth_stage TEXT,
                health_score REAL,
                height REAL,
                notes TEXT
            )
        ''')

        # 创建病虫害记录表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pest_disease_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                pest_type TEXT,
                disease_type TEXT,
                severity REAL,
                treatment_applied TEXT,
                effectiveness REAL
            )
        ''')

        # 创建报警记录表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alert_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                alert_type TEXT,
                alert_level TEXT,
                message TEXT,
                resolved BOOLEAN DEFAULT FALSE
            )
        ''')

        conn.commit()
        conn.close()

    def save_weather_data(self, weather_data: Dict, location: str):
        """保存天气数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO weather_data 
            (timestamp, temperature, humidity, rainfall, wind_speed, location)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            weather_data.get('timestamp', datetime.now()),
            weather_data.get('temperature'),
            weather_data.get('humidity'),
            weather_data.get('rainfall', 0),
            weather_data.get('wind_speed', 0),
            location
        ))

        conn.commit()
        conn.close()

    def save_sensor_data(self, sensor_data: Dict):
        """保存传感器数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO sensor_data 
            (timestamp, air_temperature, soil_temperature, air_humidity, 
             soil_humidity, soil_ph, light_intensity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            sensor_data.get('timestamp', datetime.now()),
            sensor_data.get('air_temperature'),
            sensor_data.get('soil_temperature'),
            sensor_data.get('air_humidity'),
            sensor_data.get('soil_humidity'),
            sensor_data.get('soil_ph', 6.5),
            sensor_data.get('light_intensity', 0)
        ))

        conn.commit()
        conn.close()

    def get_historical_weather(self, location: str, days: int = 30) -> List[Dict]:
        """获取历史天气数据"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        start_date = datetime.now() - timedelta(days=days)

        cursor.execute('''
            SELECT * FROM weather_data 
            WHERE location = ? AND timestamp > ?
            ORDER BY timestamp DESC
        ''', (location, start_date))

        rows = cursor.fetchall()
        conn.close()

        return [
            {
                'id': row[0],
                'timestamp': row[1],
                'temperature': row[2],
                'humidity': row[3],
                'rainfall': row[4],
                'wind_speed': row[5],
                'location': row[6]
            }
            for row in rows
        ]

    def get_sensor_statistics(self, hours: int = 24) -> Dict:
        """获取传感器数据统计"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        start_time = datetime.now() - timedelta(hours=hours)

        cursor.execute('''
            SELECT 
                AVG(air_temperature),
                MAX(air_temperature),
                MIN(air_temperature),
                AVG(soil_humidity),
                AVG(air_humidity)
            FROM sensor_data 
            WHERE timestamp > ?
        ''', (start_time,))

        result = cursor.fetchone()
        conn.close()

        return {
            'avg_temperature': result[0],
            'max_temperature': result[1],
            'min_temperature': result[2],
            'avg_soil_humidity': result[3],
            'avg_air_humidity': result[4]
        }