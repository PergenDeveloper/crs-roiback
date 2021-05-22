from django.http import Http404


def raise_404_if_empty(func):
    """
    Decorator for raising Http404 if function evaluation is false (e.g. empty queryset).
    """
    def func_wrapper(self):
        queryset = func(self)
        if queryset:
            return queryset
        raise Http404
    return func_wrapper
