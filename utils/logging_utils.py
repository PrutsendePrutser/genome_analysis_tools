from settings import Settings


def log_update(msg):
    update_logfile_path = Settings.get_update_logfile_path()
    log_msg(update_logfile_path, msg)


def log_error(msg):
    error_logfile_path = Settings.get_error_logfile_path()
    log_msg(error_logfile_path, msg)


def log_msg(logfile_path, msg):
    with open(logfile_path, 'w') as logfile:
        logfile.write(msg)
