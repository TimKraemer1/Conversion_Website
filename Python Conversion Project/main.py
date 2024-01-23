# import sys
# import os
# import conversions

# def printpwd(a, b, o):
#     if a == 'jpg':
#         if b == 'png':
#             conversions.jpgTopng(o)
    
#     if a == 'png':
#         if b == 'jpg':
#             conversions.pngTojpg(o)
    
#     if a == 'pdf':
#         dest = os.path.splitext(o)[0] + '.docx'
#         print(o)
#         conversions.pdfTodocx(o, dest)
    
#     if a == 'docx':
#         dest = os.path.splitext(o)[0] + '.pdf'
#         conversions.docxTopdf(o, dest)

#     return 1

# if __name__ == "__main__":
#     conv_a = sys.argv[1]
#     conv_b = sys.argv[2]
#     orig_pw = sys.argv[3]
#     printpwd(conv_a, conv_b, orig_pw)