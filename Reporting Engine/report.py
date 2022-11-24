from urllib.parse import urlparse
from datetime import datetime
from fpdf import FPDF, fpdf
import json
import os

fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'font'))

def id_generator(json_data):
    for k, v in json_data.items():
        if k == "inputs":
            yield v
        elif isinstance(v, dict):
            for id_val in id_generator(v):
                yield id_val

def report_gen(pdf, ll):
    print("------------------------")
    json_data = json.loads(ll)

    for key in json_data:
        if key == 'inputs':
            break
        print(key + ": " + str(json_data[key]))
        pdf.multi_cell(0, 7, txt = f"{key}: {str(json_data[key])}" , align = 'L')

    print('inputs:')
    pdf.multi_cell(0, 7, txt = "inputs:", align = 'L')
    for _ in id_generator(json_data):
        l1 = json.dumps(_[0])
        print(l1)
        pdf.multi_cell(0, 7, txt = f"{l1}" , align = 'L')

        l2 = json.dumps(_[1])
        print(l2)
        pdf.multi_cell(0, 7, txt = f"{l2}" , align = 'L')

    return
        # pdf.multi_cell(0, 7, txt = f"{key}: {str(json_data[key])}" , align = 'L')
        # # pdf.cell(0,4, ln=1, align='C')


def pdf_generation(ll, siteName):
    t = urlparse(siteName).netloc
    siteName = '.'.join(t.split('.')[-2:])

    testTime = datetime.now()
    fileName = testTime.strftime("%m-%d-%Y_%H%M%S")

    pdf_files = os.path.join(os.path.dirname(__file__), "Tested_Site")
    pdf_out = os.path.join(pdf_files, f"({siteName})_{fileName}.pdf")
    if not os.path.isdir(pdf_files):
        os.mkdir(pdf_files)

    try:
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
        report_gen(pdf, ll)
        pdf.output(pdf_out)
    except Exception as e:
        print(e)


ll = {'action': 'https://www.bpitindia.com/', 'method': 'get', 'inputs': [{'type': 'search', 'name': 's'}, {'type': 'hidden', 'name': 'id'}]}
pdf_generation(json.dumps(ll), "https://www.bpitindia.com/")
