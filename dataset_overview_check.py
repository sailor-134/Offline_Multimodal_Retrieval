import os

def main():
    base_dir = "datasets"

    # 1. Google NQ 文本统计
    nq_process = os.path.join(base_dir, "01_google_nq_subset", "processed")
    nq_file_num = len(os.listdir(nq_process))
    print(f"1. Google NQ 预处理文件总数：{nq_file_num} 个")

    # 2. COCO 图片统计
    coco_process = os.path.join(base_dir, "02_coco_image_subset", "processed")
    coco_imgs = [
        f for f in os.listdir(coco_process)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    print(f"2. COCO 测试图片总数：{len(coco_imgs)} 张")

    # 3. RVL-CDIP 扫描文档统计
    rvl_process = os.path.join(base_dir, "03_rvl_cdip_scan_subset", "processed")
    rvl_imgs = [
        f for f in os.listdir(rvl_process)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff"))
    ]
    print(f"3. RVL-CDIP 扫描文档图片总数：{len(rvl_imgs)} 张")

    # 4. Wikipedia 维基百科文本统计
    wiki_process = os.path.join(base_dir, "04_wikipedia_corpus_subset", "processed")
    wiki_txt_list = [f for f in os.listdir(wiki_process) if f.endswith(".txt")]
    print(f"4. Wikipedia 百科文本总数：{len(wiki_txt_list)} 篇")

    print("\n======== 四大核准数据集校验全部完成 ========")

if __name__ == "__main__":
    main()