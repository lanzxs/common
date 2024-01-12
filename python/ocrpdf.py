from paddleocr import PaddleOCR

# Paddleocr 目前支持的多语言语种可以通过修改 lang 参数进行切换
# 例如 `ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=3)  # need to run only once to download and load model into memory
img_path = './111.pdf'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)
