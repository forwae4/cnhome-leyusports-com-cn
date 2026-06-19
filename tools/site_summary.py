import json
import os
from datetime import datetime

# 内置站点资料数据
SITE_DATA = {
    "title": "乐鱼体育",
    "url": "https://cnhome-leyusports.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "互动平台"],
    "description": "乐鱼体育提供丰富的体育赛事资讯与在线互动服务，涵盖足球、篮球、网球等多个热门项目。",
    "tags": ["体育", "赛事", "娱乐", "资讯"]
}


def load_summary_template() -> dict:
    """返回摘要模板结构，包含各字段的默认值。"""
    return {
        "site_name": "",
        "site_url": "",
        "keywords": [],
        "tags": [],
        "short_desc": "",
        "generated_at": ""
    }


def build_summary(data: dict) -> dict:
    """根据内置数据构建结构化摘要。"""
    summary = load_summary_template()
    summary["site_name"] = data.get("title", "未知站点")
    summary["site_url"] = data.get("url", "")
    summary["keywords"] = data.get("keywords", [])
    summary["tags"] = data.get("tags", [])
    summary["short_desc"] = data.get("description", "")
    summary["generated_at"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return summary


def format_summary_text(summary: dict) -> str:
    """将摘要字典格式化为可读文本。"""
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点名称: {summary['site_name']}")
    lines.append(f"站点URL: {summary['site_url']}")
    lines.append(f"关键词: {', '.join(summary['keywords'])}")
    lines.append(f"标签: {', '.join(summary['tags'])}")
    lines.append(f"简介: {summary['short_desc']}")
    lines.append(f"生成时间: {summary['generated_at']}")
    lines.append("=" * 50)
    return "\n".join(lines)


def export_summary_to_json(summary: dict, output_path: str = None) -> str:
    """将摘要导出为 JSON 文件，返回文件路径。"""
    if output_path is None:
        output_path = "site_summary_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    return output_path


def read_json_summary(filepath: str) -> dict:
    """从 JSON 文件读取摘要数据。"""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # 使用内置站点资料构建摘要
    summary = build_summary(SITE_DATA)

    # 打印文本摘要
    text_summary = format_summary_text(summary)
    print(text_summary)

    # 导出 JSON 文件
    json_path = export_summary_to_json(summary)
    print(f"\n摘要已保存至: {json_path}")

    # 验证读取
    loaded = read_json_summary(json_path)
    if loaded:
        print("读取验证成功，摘要内容完整。")
    else:
        print("警告: 无法读取已保存摘要。")


if __name__ == "__main__":
    main()