"""This Module contains functions to validate input data."""

from datetime import datetime

def validate_date(date):
    """Validates that the input is a datetime object or a string 
    that can be converted to a datetime object."""
    if not isinstance(date, datetime):
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError as exc:
            raise TypeError(
                "Date must be a datetime object or a string in 'YYYY-MM-DD' format"
            ) from exc
    return date

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
