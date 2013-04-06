import sublime, sublime_plugin

class CountLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("select_all")

        selection = self.view.sel()[0]
        bufferText = self.view.substr(selection)
        isInCommentBlock = False
        sloc = count_lines(bufferText, "//", "/*", "*/")

        print sloc

    def count_lines(text, singleLineComment, multilineCommentStart, multilineCommentEnd):
        byLine = text.split('\n')
        isInCommentBlock = False
        sloc = 0
        for line in bufferText:
            trimmed = line.strip()
            if trimmed == "":
                continue
            if isInCommentBlock and trimmed.endswith(multilineCommentEnd):
                isInCommentBlock = False
                continue
            if isInCommentBlock:
                continue

            if trimmed.startswith(singleLineComment):
                continue

            if  trimmed.startswith(multilineCommentStart):
                isInCommentBlock = True
                continue

            sloc += 1

        return sloc;