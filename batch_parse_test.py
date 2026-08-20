import os
from tika import parser
from PIL import Image

def parse_single_file(file_path):
    #单文件解析：支持txt...
    suffix = os.path.splitext(file_path)[1].lower()
    meta = {"path": file_path, "type": suffix, "content": ""}
    try:
        if suffix in [".txt"]:
            with open(file_path, "r", encoding="utf-8") as f:
                meta["content"] = f.read()
        elif suffix in [".pdf", ".docx"]:
            raw = parser.from_file(file_path)
            meta["content"] = raw.get("content", "")
        elif suffix in [".jpg", ".png"]:
            img = Image.open(file_path)
            meta["content"] = f"图片尺寸：{img.size}"
        return {"ok": True, "meta": meta}
    except Exception as e:
        return {"ok": False, "err": str(e)}


def batch_file_parser(root_dir):
    #批量遍历目录执行解析
    success_count = 0
    fail_count = 0
    meta_list = []
    for parent, _, files in os.walk(root_dir):
        for fname in files:
            fp = os.path.join(parent, fname)
            res = parse_single_file(fp)
            if res["ok"]:
                success_count +=1
                meta_list.append(res["meta"])
            else:
                fail_count +=1
    return {
        "success_count": success_count,
        "fail_count": fail_count,
        "meta_list": meta_list
    }


def main():
    dataset_root = "./datasets"
    print("===== 开始批量解析 datasets 目录文件 =====")
    if not os.path.exists(dataset_root):
        print(f"目录不存在：{dataset_root}")
        return
    result = batch_file_parser(dataset_root)
    print("===== 批量解析完成 =====\n")
    print(f"成功解析文件数：{result.get('success_count',0)}")
    print(f"解析失败文件数：{result.get('fail_count',0)}")
    print("解析得到文件元数据(只打印前5条)：")
    for idx,meta in enumerate(result.get('meta_list', [])[:5],start=1):
        print(f"{idx}. 文件路径：{meta['path']}")
        print(f"   文件类型：{meta['type']}\n")

if __name__ == "__main__":
    main()