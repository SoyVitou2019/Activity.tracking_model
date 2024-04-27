import easyocr

def extract_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = " "
    for (bbox, text_s, prob) in result:
        text += text_s
    return text

print(extract_text("./images/image2.png"))