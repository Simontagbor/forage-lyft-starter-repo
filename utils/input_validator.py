"""This Module contains functions to validate input data."""

from datetime import datetime, date

def validate_date(date_input):
    """Validates that the input is a datetime object or a string 
    that can be converted to a datetime object."""
    if isinstance(date_input, datetime):
        return date_input.date()
    elif isinstance(date_input, date):
        return date_input
    elif isinstance(date_input, str):
        try:
            return datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError as exc:
            raise TypeError(
                "Date must be a datetime object, a date object, or a string in 'YYYY-MM-DD' format"
            ) from exc
    else:
        raise TypeError(
            "Date must be a datetime object, a date object, or a string in 'YYYY-MM-DD' format"
        )
    
def validate_int(number, variable_name):
    """Validates that the input is an integer or a string
      that can be converted to an integer."""
    if not isinstance(number, int):
        try:
            return int(number)
        except ValueError as exc:
            raise TypeError(
                f"{variable_name} must be an integer or a string \
                that can be converted to an integer"
            ) from exc
    return number

def validate_bool(value, variable_name):
    """Validates that the input is a boolean or a string 
    that can be converted to a boolean."""
    if not isinstance(value, bool):
        if isinstance(value, str):
            if value.lower() in ['true', 'false']:
                return value.lower() == 'true'
        raise TypeError(
            f"{variable_name} must be a boolean or a string that can \
            be converted to a boolean ('true' or 'false')"
        )
    return value

def validate_array(array, variable_name):
    """Validates that the input is a list or a string that can be 
    converted to a list."""
    if not isinstance(array, list):
        if isinstance(array, str):
            try:
                return list(map(float, array.split(',')))
            except ValueError as exc:
                raise TypeError(
                    f"{variable_name} must be a list or a string that can \
                    be converted to a list"
                ) from exc
        raise TypeError(
            f"{variable_name} must be a list or a string that can be \
            converted to a list"
        )
    return array
