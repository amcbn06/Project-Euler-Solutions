import os
import shutil

def flatten_files(root_dir):
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)

        if os.path.isdir(folder_path):  # process only folders
            # handle main.py
            main_file = os.path.join(folder_path, "main.py")
            if os.path.exists(main_file):
                new_py = os.path.join(root_dir, f"{folder}.py")
                if not os.path.exists(new_py):
                    shutil.move(main_file, new_py)
                    print(f"✅ {main_file} -> {new_py}")
                else:
                    print(f"⚠️ Skipped {main_file} (file {new_py} already exists)")

            # handle .txt files (assume max one per folder)
            for file in os.listdir(folder_path):
                if file.endswith(".txt"):
                    old_txt = os.path.join(folder_path, file)
                    new_txt = os.path.join(root_dir, f"{folder}.txt")
                    if not os.path.exists(new_txt):
                        shutil.move(old_txt, new_txt)
                        print(f"✅ {old_txt} -> {new_txt}")
                    else:
                        print(f"⚠️ Skipped {old_txt} (file {new_txt} already exists)")

            # delete folder
            shutil.rmtree(folder_path)
            print(f"🗑️ Deleted folder {folder_path}")

if __name__ == "__main__":
    root_directory = r"C:\Users\Andrei\Desktop\Projects\project-euler-solutions\001 - 100"  # change this
    flatten_files(root_directory)
