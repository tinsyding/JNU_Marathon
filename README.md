# JNU_Marathon

这是一个用于爬取江南大学2023年马拉松赛事成绩的Python项目。它使用Selenium和Requests库来抓取网页数据并保存到CSV文件中。

## 功能

- 爬取江南大学马拉松赛事的成绩信息。
- 将爬取的数据保存为CSV格式。
- 下载证书图片并保存到本地。
- 二次爬取第一次未能成功的数据。

## 环境

- Python 3
- Selenium
- Requests

## 安装

确保你有Python3和pip安装在你的计算机上。然后，克隆这个仓库。

```bash
git clone https://github.com/tinsyding/JNU_Marathon.git
cd JNU_Marathon
```

## 依赖

在项目的根目录下，运行以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```

## 使用

1. 在项目的根目录下，运行：

```bash
python -m src.main
```

2. 按照提示选择一个Web浏览器（Chrome、Edge或Firefox）。
3. 程序将开始爬取数据并保存到 data 目录下的 data.csv 文件中。
4. 相关的日志将被保存在 logs 目录下。

5. 如果你想二次爬取第一次未能成功的数据，在项目的根目录下，运行：
```bash
python -m src.retry_data.py
```

## 注意事项

- 2023年11月23日，该项目仍有效。
- 请确保在遵守目标网站服务条款的前提下使用本脚本。
- 网站结构的变更可能导致脚本失效，此时需要对脚本进行相应的更新。

## 贡献
如果你想为这个项目贡献代码，请遵循以下步骤：

1. Fork 这个仓库。
2. 创建一个新的分支 (`git checkout -b feature/your_feature`).
3. 提交你的更改 (`git commit -am 'Add some feature'`).
4. 推送到分支 (`git push origin feature/your_feature`).
5. 创建一个新的Pull Request。
