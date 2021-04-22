import os

class Convert():

    def __init__(self, source_file_path, charset):
        self.source_file_path = source_file_path
        self.charset = charset

        new_fname = os.path.basename(self.source_file_path)
        new_fpath = f'{new_fname}.html'

        self.new_html_file_path = os.fspath(new_fpath)