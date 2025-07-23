import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_pdfs(url, download_dir="mit_pdfs"):
    # 发送 HTTP 请求获取网页内容
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # 检查请求是否成功
    except requests.RequestException as e:
        print(f"Failed to fetch webpage: {e}")
        return

    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []

    # 查找所有 <a> 标签，提取 PDF 链接
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            # 将相对 URL 转换为绝对 URL
            absolute_url = urljoin(url, href)
            pdf_links.append(absolute_url)
            print(f"Found PDF: {absolute_url}")

    # 创建下载目录
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # 下载 PDF 文件
    for pdf_url in pdf_links:
        try:
            file_name = pdf_url.split('/')[-1].split('_')[-1]
            file_path = os.path.join(download_dir, file_name)
            print(f"Downloading: {file_name}")

            # 下载文件
            pdf_response = requests.get(pdf_url, timeout=30)
            pdf_response.raise_for_status()
            with open(file_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f"Saved: {file_path}")
        except requests.RequestException as e:
            print(f"Failed to download {pdf_url}: {e}")

    print(f"Total PDFs found: {len(pdf_links)}")

# 示例用法
if __name__ == "__main__":
    url = "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/resources/lecture-notes/"
    download_pdfs(url)
