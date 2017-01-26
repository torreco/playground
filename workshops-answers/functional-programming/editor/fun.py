from functools import partial, reduce


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

    def replace_content(self, old, new):
        print("Replace content %s" % self._name)
        self._content = self._content.replace(old, new)

    def close(self):
        print("Close %s" % self._name)
        self._content = ""

    def render(self):
        print("<%s>" % self._content)


def tracker(commands):
    def reducer(state, command_tuple):
        _, results = state
        action, undo = command_tuple
        results.append(action())
        return (undo, results)

    return reduce(reducer, commands, (None, []))


if __name__ == "__main__":
    editor = Editor("fun")

    undo_last, _ = tracker([
        (editor.open, None),
        (partial(editor.append_content, " more fun content"),
         partial(editor.replace_content, " more fun content", ""))
    ])
    editor.render()

    if undo_last:
        undo_last()

    editor.render()

    tracker([
        (editor.close, None)
    ])
    editor.render()
