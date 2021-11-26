"""
This module can send data to group C/D server.
"""
import os
import json
from knox_source_data_io.io_handler import IOHandler
from config_data import config

"""
Send data to Knowledge Layer
"""


def send_data(url: str = "http://127.0.0.1:8000/uploadjsonapi/uploadJsonDoc"):
    output_folder = config["OUTPUT_FOLDER"]
    for foldername in os.listdir(output_folder):
        id = foldername[len("Grundfosliterature-") :]
        json_file_name = "Grundfosliterature-" + id + "_output.json"
        json_path = os.path.join(output_folder, foldername, json_file_name)
        try:
            with open(json_path, "r", encoding="utf-16") as json_file:
                IOHandler.post_json(json_file.read().encode("utf-8"), url)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    send_data()
