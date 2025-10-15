# ml_training.py
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np
import joblib


class PestDetectionModel:
    """病虫害检测机器学习模型"""

    def __init__(self):
        self.model = None
        self.label_encoder = LabelEncoder()
        self.scaler = StandardScaler()

    def create_cnn_model(self, input_shape: tuple, num_classes: int):
        """创建CNN图像识别模型"""
        model = keras.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D((2, 2)),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.Flatten(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(num_classes, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        return model

    def train_pest_classifier(self, images: np.ndarray, labels: list, epochs: int = 50):
        """训练病虫害分类器"""
        # 编码标签
        encoded_labels = self.label_encoder.fit_transform(labels)
        categorical_labels = keras.utils.to_categorical(encoded_labels)

        # 分割数据集
        X_train, X_test, y_train, y_test = train_test_split(
            images, categorical_labels, test_size=0.2, random_state=42
        )

        # 创建和训练模型
        input_shape = images.shape[1:]
        num_classes = len(self.label_encoder.classes_)

        self.model = self.create_cnn_model(input_shape, num_classes)

        history = self.model.fit(
            X_train, y_train,
            epochs=epochs,
            validation_data=(X_test, y_test),
            batch_size=32
        )

        return history

    from typing import Dict
    def predict_pest(self, image: np.ndarray) -> Dict:
        """预测病虫害"""
        if self.model is None:
            raise ValueError("模型未训练")

        prediction = self.model.predict(np.expand_dims(image, axis=0))
        class_idx = np.argmax(prediction[0])
        confidence = prediction[0][class_idx]
        pest_type = self.label_encoder.inverse_transform([class_idx])[0]

        return {
            'pest_type': pest_type,
            'confidence': float(confidence),
            'all_predictions': dict(zip(
                self.label_encoder.classes_,
                prediction[0]
            ))
        }


class YieldPredictionModel:
    """产量预测机器学习模型"""

    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()

    def prepare_yield_data(self, historical_data: pd.DataFrame) -> tuple:
        """准备产量预测数据"""
        features = [
            'avg_temperature', 'total_rainfall', 'sunlight_hours',
            'soil_ph', 'fertilizer_amount', 'pest_incidence'
        ]

        X = historical_data[features]
        y = historical_data['yield']

        # 标准化特征
        X_scaled = self.scaler.fit_transform(X)

        return X_scaled, y

    def train_yield_predictor(self, historical_data: pd.DataFrame):
        """训练产量预测模型"""
        X, y = self.prepare_yield_data(historical_data)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # 使用随机森林回归
        from sklearn.ensemble import RandomForestRegressor

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # 评估模型
        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)

        return {
            'train_score': train_score,
            'test_score': test_score,
            'feature_importance': dict(zip(
                historical_data.columns[:-1],  # 排除目标变量
                self.model.feature_importances_
            ))
        }

    from typing import Dict
    def predict_yield(self, conditions: Dict) -> float:
        """预测产量"""
        if self.model is None:
            raise ValueError("模型未训练")

        # 准备输入数据
        input_features = np.array([[
            conditions['avg_temperature'],
            conditions['total_rainfall'],
            conditions['sunlight_hours'],
            conditions['soil_ph'],
            conditions['fertilizer_amount'],
            conditions['pest_incidence']
        ]])

        input_scaled = self.scaler.transform(input_features)
        prediction = self.model.predict(input_scaled)

        return float(prediction[0])

from typing import Dict
class PestVirusMonitor(object):
    pass


class WeatherData(object):
    pass


class EnhancedPestMonitor(PestVirusMonitor):
    """增强的病虫害监测器，集成机器学习"""

    def __init__(self):
        super().__init__()
        self.pest_detection_model = PestDetectionModel()
        self.yield_prediction_model = YieldPredictionModel()
        self.is_trained = False

    def train_models(self, training_data: Dict):
        """训练机器学习模型"""
        print("开始训练病虫害检测模型...")

        # 训练病虫害检测模型
        pest_history = self.pest_detection_model.train_pest_classifier(
            training_data['pest_images'],
            training_data['pest_labels']
        )

        print("开始训练产量预测模型...")

        # 训练产量预测模型
        yield_results = self.yield_prediction_model.train_yield_predictor(
            training_data['yield_data']
        )

        self.is_trained = True

        return {
            'pest_training_history': pest_history.history,
            'yield_training_results': yield_results
        }

    def enhanced_pest_analysis(self, image: np.ndarray, weather_data: WeatherData) -> Dict:
        """增强的病虫害分析"""
        if self.is_trained:
            # 使用机器学习模型进行预测
            ml_prediction = self.pest_detection_model.predict_pest(image)

            # 结合传统方法
            traditional_analysis = super().analyze_pest_risk(image, weather_data)

            return {
                **traditional_analysis,
                'ml_prediction': ml_prediction,
                'combined_confidence': max(
                    traditional_analysis['risk_score'],
                    ml_prediction['confidence']
                )
            }
        else:
            # 回退到传统方法
            return super().analyze_pest_risk(image, weather_data)