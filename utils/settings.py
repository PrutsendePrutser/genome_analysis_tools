class Settings(object):
    _update_logfile_path = '../logs/update.log'
    _error_logfile_path = '../logs/error.log'

    def get_update_logfile_path(self):
        return self._update_logfile_path

    def set_update_logfile_path(self, filepath):
        self._update_logfile_path = filepath

    def get_error_logfile_path(self):
        return self._error_logfile_path

    def set_error_logfile_path(self, filepath):
        self._error_logfile_path = filepath

