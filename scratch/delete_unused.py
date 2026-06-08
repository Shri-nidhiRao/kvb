import os
import re

def get_all_files(directory, extensions=None):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                all_files.append(os.path.join(root, file))
    return all_files

def main():
    root_dir = r"d:\kvb-green-energies-website"
    public_dir = os.path.join(root_dir, "public")
    
    asset_exts = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.mp4', '.avif', '.css', '.js']
    assets = get_all_files(public_dir, asset_exts)
    
    code_exts = ['.html', '.css', '.js']
    code_files = get_all_files(public_dir, code_exts)
    code_files.append(os.path.join(root_dir, "server.js"))

    code_contents = ""
    for cf in code_files:
        try:
            with open(cf, 'r', encoding='utf-8') as f:
                code_contents += f.read() + "\n"
        except Exception:
            pass

    to_delete = []

    # Check assets
    for asset in assets:
        basename = os.path.basename(asset)
        if basename not in code_contents:
            to_delete.append(asset)
            
    # Check HTML files
    html_files = get_all_files(public_dir, ['.html'])
    for hf in html_files:
        basename = os.path.basename(hf)
        if basename in ['index.html', '404.html', 'header.html', 'footer.html']:
            continue
        if basename not in code_contents:
            to_delete.append(hf)

    deleted_count = 0
    for f in to_delete:
        # Exclusions:
        if 'blog' in f.lower():
            continue # skip blogs
        if os.path.dirname(f) == root_dir:
            continue # skip root scripts
            
        print(f"Deleting: {f}")
        try:
            os.remove(f)
            deleted_count += 1
        except Exception as e:
            print(f"Failed to delete {f}: {e}")

    print(f"Total files deleted: {deleted_count}")

    # Remove empty directories
    print("Cleaning up empty directories...")
    for root_p, dirs, files in os.walk(public_dir, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root_p, name)
            if not os.listdir(dir_path):
                print(f"Removing empty directory: {dir_path}")
                try:
                    os.rmdir(dir_path)
                except Exception as e:
                    print(f"Failed to remove dir {dir_path}: {e}")

if __name__ == '__main__':
    main()
