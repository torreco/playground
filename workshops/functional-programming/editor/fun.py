from functools import partial


class Editor(object):
    """
    Receiver
    """

    def __init__(self, name):
        self._name = name

    def open(self):
        print("Open %s" % self._name)
        self._content = "Initial content"

    def append_content(self, content):
        print("Append content %s" % self._name)
        self._content += content

    def close(self):
        print("Close %s" % self._name)
        self._content = ""

    def render(self):
        print("<%s>" % self._content)


def tracker(commands):
    return list(map(lambda c: c(), commands))


if __name__ == "__main__":
    editor = Editor("fun")

    tracker([editor.open, partial(editor.append_content, " more fun content")])

    editor.render()

    tracker([editor.close])

    editor.render()
