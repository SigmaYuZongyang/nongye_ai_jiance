# setup.py
from setuptools import setup, find_packages

setup(
    name="agriculture-intelligent-system",
    version="1.0.0",
    author="农业智能系统开发团队",
    description="农业栽培智能分析管控系统",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",  # 注意：使用 scikit-learn 而不是 sklearn
        "requests>=2.25.0",
        "matplotlib>=3.5.0",
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "agri-system=agriculture_system.cli.main:main",
        ],
    },
    python_requires=">=3.7",
)

