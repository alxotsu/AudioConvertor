def exception_catcher_decorator(method):
    def inner(*args, **kwargs):
        try:
            response = method(*args, **kwargs)
        except Exception as e:
            response = _handle_exception(e)
        return response
    return inner


def _handle_exception(e):
    return str(e), 500  #TODO доделац
