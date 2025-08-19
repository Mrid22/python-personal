import os
import zipfile
import tarfile

for filename in os.listdir("/home/mridula/Downloads"):
    # Skip hidden files
    if filename.startswith("."):
        continue
    # Move Pictures
    if filename.endswith(".jpg") or filename.endswith(".png"):
        os.rename("/home/mridula/Downloads/" + filename, "/home/mridula/Pictures/" + filename)
    # Move Documents
    elif filename.endswith(".pdf") or filename.endswith(".docx"):
        os.rename("/home/mridula/Downloads/" + filename, "/home/mridula/Documents/" + filename)
    # Move ISO Files
    elif filename.endswith(".iso"):
        os.rename("/home/mridula/Downloads/" + filename, "/home/mridula/ISOs/" + filename)
    # Extract Archives
    elif filename.endswith(".zip"):
        with zipfile.ZipFile("/home/mridula/Downloads/" + filename) as zip_ref:
            zip_ref.extractall("/home/mridula/Downloads/ " + filename[:-4])
        os.remove("/home/mridula/Downloads/" + filename)
    elif filename.endswith(".tar.gz") or filename.endswith(".tgz"):
        file = tarfile.open("/home/mridula/Downloads/" + filename)
        file.extractall("/home/mridula/Downloads/" + filename[:-7])
        file.close()
        os.remove("/home/mridula/Downloads/" + filename)
