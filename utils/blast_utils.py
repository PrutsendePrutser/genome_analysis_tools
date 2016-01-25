def create_makeblastdb_input_string(filepath_list):
    # Wrap each filename in double quotes, this is required by makeblastdb in case there are
    # any spaces in the filepath
    makeblastdb_input_list = ['"{}"'.format(filepath) for filepath in filepath_list]
    makeblastdb_input_string = ' '.join(makeblastdb_input_list)
    return_string = '{}'.format(makeblastdb_input_string)

    return return_string

