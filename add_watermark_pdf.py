import PyPDF2
import os

def add_watermark(water_file,page_pdf):         #添加水印函数
    """
    将水印pdf与pdf的一页进行合并
    :param water_file:
    :param page_pdf:
    :return:
    """
    pdfReader = PyPDF2.PdfFileReader(water_file) 
    pdfReader.getPage(0).mergePage(page_pdf)     #将水印添加到提取页，水印置于下层背景，同word水印效果
    return pdfReader.getPage(0)

# 遍历pdf的每一页,添加水印

# 将把你要添加水印的pdf放在一个文件夹并填写文件夹路径
Document_file_path = r"D:\xx\xx\xx\xx"
DocumentName = os.listdir(Document_file_path)


# 用word生成你要添加水印的一页pdf，放在一个文件夹并填写文件夹路径
WatermarkName_file_path = r"D:\xx\xx\xx\xx"
WatermarkName= os.listdir(WatermarkName_file_path)


for SelectDN in range(len(DocumentName)):                      # 遍历所有文件
    pdfReader = PyPDF2.PdfFileReader(f"D:\\xx\\xx\\xx\\xx{DocumentName[SelectDN]}")   # 读取pdf内容
    for SelectWm in range(len(WatermarkName)):                 # 遍历所有watermark
        pdfWriter = PyPDF2.PdfFileWriter()                     # 用于写pdf
        for page in range(pdfReader.numPages):                 # 遍历pdf的每一页,添加水印
            page_pdf = add_watermark(f"D:\\xx\\xx\\xx\\xx{WatermarkName[SelectWm]}", pdfReader.getPage(page))
            pdfWriter.addPage(page_pdf)

        with open(WatermarkName[SelectWm][9:-4]+'_'+DocumentName[SelectDN], 'wb') as target_file:  #命名并保存最终pdf
            pdfWriter.write(target_file)
