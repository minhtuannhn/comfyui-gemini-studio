import os
import shutil

comfy_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
gemini_path = os.path.abspath(os.path.dirname(__file__))

def setup_js():
    try:
        js_dest_path = os.path.join(comfy_path, "web", "extensions", "gemini")
        js_destCss_path = os.path.join(comfy_path, "web", "user.css")  # Đường dẫn đích file use.css
        js_src_path = os.path.join(gemini_path, "gemini-studio","extensions2")
        js_srcCss_file = os.path.join(gemini_path,"gemini-studio", "CSS", "user.css")  # Đường dẫn nguồn file use.css

        print(js_src_path)
        print(js_dest_path)

        # Copy thư mục extensions vào web/extensions/gemini
        if os.path.exists(js_dest_path):
            shutil.rmtree(js_dest_path)

        shutil.copytree(js_src_path, js_dest_path)

        # Copy file use.css và ghi đè nếu file đã tồn tại

        shutil.copy(js_srcCss_file, js_destCss_path)  # Ghi đè file use.css
        print(f"Copied {js_srcCss_file} to {js_destCss_path}")


    except Exception as e:
        print(f"An error occurred: {e}")

setup_js()

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
WEB_DIRECTORY = "./gemini-studio/extensions"  # so ComfyUI can use custom CSS/JS

__all__ = ["WEB_DIRECTORY"]
