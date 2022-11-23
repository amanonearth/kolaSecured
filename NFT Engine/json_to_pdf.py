from datetime import datetime
from fpdf import FPDF, fpdf
import requests
import json
import sys
import os

fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'font'))

def getData(pdf):
    url = "http://127.0.0.1:5000/test"
    resp = requests.get(url)
    json_data = json.loads(resp.text)
    for key in json_data:
        # print(key + ": " + str(json_data[key]))
        pdf.multi_cell(0, 7, txt = f"{key}: {str(json_data[key])}" , align = 'L')
        # pdf.cell(0,4, ln=1, align='C')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] Site Name Not Given")
        exit(1)
    siteName = sys.argv[1]
    testTime = datetime.now()
    fileName = testTime.strftime("%m-%d-%Y_%H%M%S")

    pdf_files = os.path.join(os.path.dirname(__file__), "Tested_Site")
    pdf_out = os.path.join(pdf_files, f"({siteName})_{fileName}.pdf")
    if not os.path.isdir(pdf_files):
        os.mkdir(pdf_files)

    pdf=FPDF()
    pdf.add_font("NotoSans", style="", fname="NotoSans-Regular.ttf", uni=True)
    pdf.add_font("NotoSans-Bold", style="", fname="NotoSans-Bold.ttf", uni=True)
    pdf.add_font("NotoSans-ExtraBold", style="", fname="NotoSans-ExtraBold.ttf", uni=True)
    pdf.add_page()

    pdf.set_font("NotoSans-ExtraBold", size = 25)
    pdf.multi_cell(0, 8, txt = str(siteName), align = 'L')
    pdf.set_font("NotoSans", size = 9)
    pdf.multi_cell(0, 8, txt = str(testTime), align = 'L')

    pdf.cell(0,4, ln=1, align='C')

    pdf.set_font("NotoSans-Bold", size = 13)
    pdf.multi_cell(0, 8, txt = "Bugs found:", align = 'L')

    pdf.set_font("NotoSans", size = 10)
    getData(pdf)

    pdf.output(pdf_out)