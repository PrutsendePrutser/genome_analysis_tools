





def create_makeblastdb_input_string(filepath_list):
    """
    Create a makeblastdb string, that can be passed to the commandline utils,
    to create the BLAST databases
    :param filepath_list: List of files to include in the BLAST DB
    :return: string that contains the commandline argument
    """
    # Wrap each filename in double quotes, this is required by makeblastdb in case there are
    # any spaces in the filepath
    makeblastdb_input_list = ['"{}"'.format(filepath) for filepath in filepath_list]
    makeblastdb_input_string = ' '.join(makeblastdb_input_list)
    return_string = '{}'.format(makeblastdb_input_string)








    return return_string

