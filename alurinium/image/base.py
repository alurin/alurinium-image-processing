from alurinium.image.backends.base import Backend
import hashlib
import json
import os


class Engine(object):
    """
    This class is managed work
    """
    def __init__(self):
        self.backend = Backend()
        self.thumbnail_path = ''

    def get_output_filename(self, original_filename, **options):
        token = json.dumps(options, sort_keys=True)
        token = u"%s.%s" % (original_filename, token)
        token = token.encode("utf-8")

        m = hashlib.sha256()
        m.update(token)
        return m.hexdigest()

    def process_image(self, original_filename, output_filename=None, **options):
        if original_filename:
            if not output_filename:
                output_filename = self.get_output_filename(original_filename, **options)
            output_fullname = os.path.join(self.thumbnail_path, output_filename)
            return self.backend.process_image(original_filename, output_fullname, **options)
        return None