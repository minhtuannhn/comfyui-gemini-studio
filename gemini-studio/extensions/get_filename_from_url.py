import requests
from urllib.parse import unquote
import cgi

class GetFileNameFromURL:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "url": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("filename", "url")
    FUNCTION = "get_filename"
    CATEGORY = "Tools"

    def get_filename(self, url):
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            raise Exception(f"Error downloading file: {response.status_code}")

        # 处理重定向
        if response.status_code == 303:
            redirect_url = response.headers.get('Location')
            response = requests.get(redirect_url, stream=True)
            if response.status_code != 200:
                raise Exception(f"Error downloading file: {response.status_code}")

        # 尝试从 Content-Disposition 头中获取文件名
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            _, params = cgi.parse_header(content_disposition)
            filename = params.get("filename*")
            if filename:
                filename = unquote(filename.replace("UTF-8''", ""))
            else:
                filename = params.get("filename")
        else:
            # 尝试从 X-Goog-Filename 头中获取文件名
            filename = response.headers.get('X-Goog-Filename')

        if not filename:
            raise Exception("Unable to determine filename")

        return (filename, url)

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "GetFileNameFromURL": GetFileNameFromURL
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GetFileNameFromURL": "Get FileName From URL"
}
