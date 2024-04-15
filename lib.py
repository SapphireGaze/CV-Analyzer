import PyPDF2
from transformers import pipeline

CLASSIFIER = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
CONFIDENCE_THRESHOLD = 0.7

def extract_text_from_pdf(file_path: str) -> str:
    with open(file_path, "rb") as file:
        text = ""
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def analyze_cv(cv_path: str, position: str) -> dict:
    cv_text = extract_text_from_pdf(cv_path)
    labels = [position]

    result = CLASSIFIER(cv_text, labels)

    predicted_label = result["labels"][0]
    confidence = result["scores"][0]

    if confidence >= CONFIDENCE_THRESHOLD:
        return {"message": f"You are a great potential candidate for the position of {predicted_label} with confidence {confidence:.2f}."}
    else:
        return {"message": f"Your suitability for the position of {predicted_label} is low (confidence: {confidence:.2f})."}