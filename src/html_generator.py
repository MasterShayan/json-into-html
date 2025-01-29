from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

from json_definition import DisplayType

class HtmlGenerator:
    def __init__(self, data, json_definition, template_path="template.html"):
        self.data = data
        self.json_definition = json_definition
        self.soup = BeautifulSoup("", "html.parser")
        self.env = Environment(loader=FileSystemLoader('.'))
        self.template = self.env.get_template(template_path)

    def generate_html(self):
        return self.template.render(data=self.data, json_definition=self.json_definition, display_type=DisplayType)


    def save_html(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.generate_html())