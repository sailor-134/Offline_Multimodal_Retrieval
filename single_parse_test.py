from batch_parse_test import parse_single_file

def main():
    file_path = r"./datasets/02_coco_image_subset"
    print("===== 开始单文件解析 =====")
    print("===== 本次解析的文件为02_coco_image_subset =====")
    result = parse_single_file(file_path)
    if result["ok"]:
        print("解析成功！")
        print("文件元数据：")
        print(f"文件路径：{result['meta']['path']}")
        print(f"文件类型：{result['meta']['type']}\n")

    else:
        print("解析失败，错误信息：", result["err"])
    print("===== 单文件解析完成 =====")

if __name__ == "__main__":
    main()
