
# FinancialCrawler

## 目录

- [FinancialCrawler](#financialcrawler)
  - [目录](#目录)
  - [简介](#简介)
  - [安装](#安装)
    - [环境准备](#环境准备)
    - [安装步骤](#安装步骤)
  - [使用方法](#使用方法)
    - [爬虫模块](#爬虫模块)
    - [数据分析模块](#数据分析模块)
  - [项目结构](#项目结构)
  - [依赖项](#依赖项)
  - [贡献代码](#贡献代码)


## 简介

**FinancialCrawler** 是一个关于金融主题的网络爬虫系统，旨在从东方财富网抓取股票数据，并进行数据分析和可视化展示。项目分为两个主要部分：
1. **爬虫模块**：使用Scrapy框架从东方财富网抓取股票数据并存储到MongoDB数据库中。
2. **数据分析模块**：使用Pandas和PyEcharts对股票数据进行清洗、分析和可视化。

## 安装

### 环境准备

确保已安装以下工具和库：

- Python 3.8+
- MongoDB
- Scrapy
- Pandas
- PyEcharts

### 安装步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/yourusername/FinancialCrawler.git
   cd FinancialCrawler
   ```

2. 安装依赖项：

   ```bash
   pip install -r requirements.txt
   ```

3. 配置MongoDB连接（在`my_crawler/my_crawler/settings.py`中）：

   ```python
   MONGODB_HOST = "127.0.0.1"
   MONGODB_PORT = 27017
   MONGODB_DBNAME = "FinancialCrawler"
   ```

4. 启动爬虫：

   ```bash
   scrapy crawl stockBoardEm
   ```

5. 运行数据分析脚本：

   ```bash
   python data_analysis/data_ana/fiancial_ana_graph.py
   ```

## 使用方法

### 爬虫模块

1. 修改爬虫配置文件`my_crawler/my_crawler/settings.py`中的参数，如User-Agent等。
2. 启动爬虫，抓取股票数据并存储到MongoDB中。

### 数据分析模块

1. 数据清洗：运行`data_analysis/data_clean/stock_data.py`中的`clean_data()`函数，将MongoDB中的数据导出为CSV文件并进行清洗。
2. 数据分析与可视化：使用`data_analysis/data_ana`目录下的Python脚本进行数据分析和可视化。例如：

   ```python
   from data_analysis.data_ana.fiancial_ana_graph import stock_open_close_line, stock_close_worldcloud
   
   # 绘制今开昨收折线图
   stock_open_close_line("上海临港")
   
   # 绘制股价词云图
   stock_close_worldcloud("2022-05-13")
   ```

## 项目结构

```
FinancialCrawler/
├── README.md                           # 项目说明文档
├── requirements.txt                    # 依赖项列表
├── main.py                             # 示例主程序入口
├── my_crawler/
│   ├── scrapy.cfg                      # Scrapy配置文件
│   └── my_crawler/
│       ├── items.py                    # 爬虫Item定义
│       ├── middlewares.py              # 中间件定义
│       ├── pipelines.py                # 数据管道定义
│       ├── settings.py                 # 爬虫设置
│       └── spiders/
│           └── stockBoard.py           # 股票爬虫
├── data_analysis/
│   ├── data_clean/
│   │   └── stock_data.py               # 数据清洗脚本
│   ├── resources/
│   │   └── html/
│   │       ├── a.html                  # 示例HTML文件
│   │       └── kline_*.html            # K线图HTML文件
│   └── data_ana/
│       ├── fiancial_ana_graph.py       # 数据可视化脚本
│       ├── financial_ana_data.py       # 数据处理脚本
│       ├── financial_ana_kline.py      # K线图绘制脚本
│       └── test.py                     # 测试脚本
└── tests/                              # 测试代码目录
```

## 依赖项

- Python 3.8+
- Scrapy
- Pandas
- PyEcharts
- MongoDB



## 贡献代码

欢迎贡献代码！你可以通过以下方式参与：

1. Fork 仓库。
2. 创建新分支 (`git checkout -b feature-branch`)。
3. 提交更改 (`git commit -am 'Add some feature'`)。
4. 推送到新分支 (`git push origin feature-branch`)。
5. 提交Pull Request。
