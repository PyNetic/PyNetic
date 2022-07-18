class Page:
    def __init__(self, title, filename):
        self.title = title
        self.children = []
        self.filename = filename

    def output(self, static=True):
        body = ""
        i = 0
        for child in self.children:
            body += (
                ("\t\t" if i != 0 else "")
                + str(child)
                + ("\n" if i != len(self.children) - 1 else "")
            )
            i += 1

        with open(self.filename + ".html", "w+") as index:
            index.write(
                f"""<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
                    """
            )

    def add(self, child):
        self.children.append(child)
        return child


class Header:
    def __init__(self, text, size=1):
        self.text = text
        self.size = size

    def __repr__(self):
        text = ""
        for child in self.text:
            text += str(child)
        return f"<h{self.size}>{text}</h{self.size}>"


class Bold:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"<b>{self.text}</b>"


class Paragraph:
    def __init__(self, text, size=1):
        self.text = text

    def __repr__(self):
        text = ""
        for child in self.text:
            text += str(child)
        return f"<p>{text}</p>"


class Image:
    def __init__(self, source):
        self.src = source

    def __repr__(self):
        return f'<img src="{self.src}"/>'
