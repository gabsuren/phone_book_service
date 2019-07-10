class ServiceException(Exception):
    """"
    Custom exception for services.
    """
    def __init__(self, error_msg, error_code):
        """
        Overrides default __init__ method and appends error message and
            error code to its instance
        :param error_msg:
        :param error_code:
        """

        self.error_msg = unicode(error_msg)
        self.error_code = error_code

        super(Exception, self).__init__()
