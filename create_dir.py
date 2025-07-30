import os

base_path = "D:/projects-d/penta-robustvideomatting"
dir_to_create = os.path.join(base_path, "src_model")
os.makedirs(dir_to_create, exist_ok=True)

print(f"Directory {dir_to_create} created successfully.")