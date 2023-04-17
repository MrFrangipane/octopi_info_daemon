import os
import jinja2

_HTML_J2 = os.path.join(os.path.dirname(__file__), "resources", "index.html.jinja2")


def make_html_template(htmlpage_filepath, octopi_info):  # FIXME : make info a dataclass
    environment = jinja2.Environment()

    with open(_HTML_J2, 'r') as template_file:
        template = environment.from_string(template_file.read())

    lines = list()
    for line in octopi_info:
        if not line:
            lines.append("&nbsp;")
        else:
            lines.append(line)

    page = template.render(overlay_divs="\n".join([f"<div>{line}</div>" for line in lines]))

    with open(htmlpage_filepath, 'w') as page_file:
        page_file.write(page)
