
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

    def render(self):
        print("<%s>" % self._content)

    def close(self):
        print("Close %s" % self._name)
        self._content = ""


class Command(object):
    """
    Command interface
    """

    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class Open(Command):
    """
    Concrete command
    """

    def execute(self):
        self._obj.open()


class Paste(Command):
    """
    Concrete command
    """

    def __init__(self, obj, content):
        super(Paste, self).__init__(obj)
        self._content = content

    def execute(self):
        self._obj.append_content(self._content)

    def undo(self):
        self._obj.replace_content(self._content, "")


class Close(Command):
    """
    Concrete command
    """

    def execute(self):
        self._obj.close()


class Tracker(object):
    """
    Invoker
    """

    def __init__(self):
        self._commands = []
        self._last_command = None

    def record(self, command):
        self._commands.append(command)

    def run(self):
        for command in self._commands:
            command.execute()
            self._last_command = command

        self._commands = []

    def undo_last(self):
        if self._last_command:
            self._last_command.undo()
            self._last_command = None


if __name__ == "__main__":
    """
    Client
    """
    editor = Editor("not fun")
    tracker = Tracker()

    tracker.record(Open(editor))
    tracker.record(Paste(editor, " more not fun content"))
    tracker.run()
    editor.render()
    tracker.undo_last()
    editor.render()
    tracker.record(Close(editor))
    tracker.run()
