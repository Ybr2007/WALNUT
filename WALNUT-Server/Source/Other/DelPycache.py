import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pyc"):
            os.remove(os.path.join(root, file))
    
for root, dirs, files in os.walk("."):
    for dir in dirs:
        if dir == "__pycache__":
            os.rmdir(os.path.join(root, dir))