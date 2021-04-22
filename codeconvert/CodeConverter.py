import argparse
import os
import sys

import imgkit
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_for_filename


class Convert():

    def __init__(self, source_file_path, charset):
        self.source_file_path = source_file_path
        self.charset = charset

        new_fname = os.path.basename(self.source_file_path)
        new_fpath = f'{new_fname}.html'

        self.new_html_file_path = os.fspath(new_fpath)

    
    def source_to_html(self):
        """
        Convert to html file and save.

        Parameters:
            charset: string

        Returns:
            tupple:
                boolean:
                string: html text or None
        """

        lexer = get_lexer_for_filename(self.source_file_path)
        formater = HtmlFormatter()

        try:
            with open(self.source_file_path, 'r', encoding=self.charset) as f:
                return True, highlight(f.read(), lexer, formater)
        except Exception:
            return False, None

    
    def get_highlight_css(self):
        """
        Get css.
        pygments style 'monokai'

        Returns:
            css text
        """

        return HtmlFormatter(style='monokai').get_style_defs('.highlight')


    def html_parser(self, html, css):
        """
        Soucecode convert to html file and save it.
        """

        index = open('index.html', mode='r', encoding=self.charset)
        soup = BeautifulSoup(index.read(), 'html.parser')
        index.close()
        
        with open(self.new_html_file_path, mode='w', encoding=self.charset) as f:
            soup.section.append(
                BeautifulSoup(html, 'html.parser')
            )
            soup.style.append(css)

            f.write(soup.prettify())


    def html_to_img(self):
        """
        html file convert to image file
        """

        img_name = f'{os.path.basename(self.new_html_file_path)}.jpg'

        options = {
            'format': 'jpg',
            'quality': 100,
            'crop-w': 1080,
            'encoding': self.charset
        }
        
        imgkit.from_file(self.new_html_file_path, img_name, options=options)
        os.remove(self.new_html_file_path)


def main():
    
    # argparseの設定
    parser = argparse.ArgumentParser(
        description='sourcecode convert to html file.')

    ## 必須の引数
    parser.add_argument(
        'path',
        help='sourcecode file path'
    )

    parser.add_argument(
        '-c', '--charset',
        default='utf-8'
    )

    args = parser.parse_args()

    convert = Convert(args.path, args.charset)

    # source code to html
    result, html = convert.source_to_html()

    if not result:
        print("Can't read source code file.")
        sys.exit()

    css = convert.get_highlight_css()
    convert.html_parser(html, css)
    convert.html_to_img()

    print('Save image file.')