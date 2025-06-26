import os

def read_code_file(file):
    ext = os.path.splitext(file.name)[1]
    if ext in [".py", ".java", ".cob", ".txt"]:
        return file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file format")

def detect_language(code):
    if "def " in code or "import" in code:
        return "python"
    elif "IDENTIFICATION DIVISION" in code.upper():
        return "cobol"
    elif "public class" in code or "System.out.println" in code:
        return "java"
    return "unknown"
