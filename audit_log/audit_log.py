from datetime import datetime


# writing to audit file function
def write_audit_log(user, change_type, details):
    log_entry = "{date_time} - {user} - {change_type} - {details}".format(
        date_time=datetime.now(),
        user=user,
        change_type=change_type,
        details=details
    )

    with open("audit.log", "a") as log_file:
        log_file.write(log_entry + "\n")


# writing to audit file
def create_data(user, data):
    write_audit_log(user, "create", data)


# updating to audit file
def update_data(user, data):
    write_audit_log(user, "update", data)


# archive in audit file
def archive_data(user, data):
    write_audit_log(user, "archive", data)


# unarchive in audit file
def unarchive_data(user, data):
    write_audit_log(user, "unarchive", data)