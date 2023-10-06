from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class LictPagination(PageNumberPagination):
  page_size = 1