import sublime, sublime_plugin

class CountLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("select_all")

        selection = self.view.sel()[0]
        bufferText = self.view.substr(selection).split('\n')
        isInCommentBlock = False
        sloc = 0
        for line in bufferText:
            trimmed = line.strip()
            if trimmed == "":
                continue
            if isInCommentBlock and trimmed.endswith("*/"):
                isInCommentBlock = False
                continue
            if isInCommentBlock:
                continue

            if trimmed.startswith("//"):
                continue

            if  trimmed.startswith("/*"):
                isInCommentBlock = True
                continue

            sloc += 1

        print sloc