# JNU_Marathon

这是一个用于爬取江南大学2023年马拉松赛事成绩的Python脚本。  
该脚本使用Selenium和Requests库来抓取网页数据并保存到CSV文件中。

## 功能

- 爬取江南大学马拉松赛事的成绩信息。
- 将爬取的数据保存为CSV格式。
- 下载证书图片并保存到本地。
- 二次爬取第一次未能成功的数据。

## 环境

- Python 3
- Selenium
- Requests

## 安装依赖

1. 确保Python3和pip安装在你的计算机上。然后，克隆这个仓库。

    ```bash
    git clone https://github.com/tinsyding/JNU_Marathon.git
    cd JNU_Marathon
    ```


2. 在项目的根目录下，运行以下命令安装所需依赖：

    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. 在项目的根目录下，运行：

    ```bash
    python src\\main.py
    ```

2. 按照提示选择一个Web浏览器（Google Chrome、Microsoft Edge、Mozilla Firefox）。

3. 程序将开始爬取数据并保存到 data 目录下的 data.csv 文件中。

4. 未能爬取的胸牌号码将被保存在 logs 目录下。

5. 如果你想二次爬取第一次未能成功的数据，在项目的根目录下，运行：

    ```bash
    python src\\retry_data.py
    ```
