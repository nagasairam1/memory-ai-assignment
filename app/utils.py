import json
from typing import List, Union, IO


def load_messages(source: Union[str, IO, bytes]) -> List[str]:
    """
    Load a list of messages (strings) from:
    - a file path (str), or
    - a Streamlit UploadedFile / file-like object.

    Expects JSON array: ["msg1", "msg2", ...]
    """
    # Case 1: source is a file path string
    if isinstance(source, str):
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        # Case 2: Streamlit UploadedFile or file-like
        # UploadedFile behaves like a binary file → decode to text
        try:
            # try reading bytes and decoding
            content = source.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8")
            data = json.loads(content)
        finally:
            # Reset pointer so it can be re-read if needed
            try:
                source.seek(0)
            except Exception:
                pass

    if not isinstance(data, list):
        raise ValueError("JSON must be an array of messages (list).")

    messages = [str(x) for x in data]
    return messages
