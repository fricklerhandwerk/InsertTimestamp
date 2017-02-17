import sublime_plugin
from datetime import datetime
from datetime import timezone


class InsertTimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit, fmt='%Y-%m-%dT%H:%M:%S%z'):
        time = datetime.now(timezone.utc) \
                       .astimezone() \
                       .strftime(fmt)
        for s in self.view.sel():
            # do not select after inserting into empty region
            if s.empty():
                self.view.insert(edit, s.a, time)
            else:
                self.view.replace(edit, s, time)
