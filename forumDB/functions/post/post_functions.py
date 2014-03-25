from forumDB.functions.database import execInsertUpdateQuery

__author__ = 'maxim'


def save_post(required_parameters, optional_parameters):
    query = 'insert into Posts (date , thread , message , user , forum '
    values = "( %s , %s , %s , %s , %s "
    query_parameters = [required_parameters['date'], required_parameters['thread'], required_parameters['message'],
                        required_parameters['user'], required_parameters['forum']]
    if optional_parameters['parent'] is not None:
        query += ', parent '
        values += ', %s '
        query_parameters.append(optional_parameters['parent'])

    if optional_parameters['isApproved'] is not None:
        query += ', isApproved '
        values += ', %s '
        query_parameters.append(optional_parameters['isApproved'])

    if optional_parameters['isHighlighted'] is not None:
        query += ', isHighlighted '
        values += ', %s '
        query_parameters.append(optional_parameters['isHighlighted'])

    if optional_parameters['isSpam'] is not None:
        query += ', isSpam '
        values += ', %s '
        query_parameters.append(optional_parameters['isSpam'])

    if optional_parameters['isEdited'] is not None:
        query += ', isEdited '
        values += ', %s '
        query_parameters.append(optional_parameters['isEdited'])

    if optional_parameters['isDeleted'] is not None:
        query += ', isDeleted '
        values += ', %s '
        query_parameters.append(optional_parameters['isDeleted'])

    query += ') values ' + values + ')'
    execInsertUpdateQuery(query, query_parameters)