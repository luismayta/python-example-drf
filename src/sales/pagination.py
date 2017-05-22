from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param


class CustomCoursePaginator(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({'count': self.page.paginator.count,
                         'next': self.get_next_link(),
                         'previous': self.get_previous_link(),
                         'result': data})

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return replace_query_param('', self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return replace_query_param('', self.page_query_param, page_number)