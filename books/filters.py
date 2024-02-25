from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters
from .models import Book
from django.db.models import Q

class CustomSearchFilter(rest_filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if search_fields and search_terms:
            queries = [Q(**{f'{search_field}__icontains': term.strip()}) for term in search_terms for search_field in search_fields]
            combined_query = Q()
            
            for query in queries:
                combined_query |= query

            queryset = queryset.filter(combined_query)

        return queryset


class BookFilter(filters.FilterSet):
    author_name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    genre_name = filters.CharFilter(field_name='genre__name', lookup_expr='icontains')
    condition_name = filters.CharFilter(field_name='condition__name', lookup_expr='icontains')
    owner_username = filters.CharFilter(field_name='owner__username', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author_name', 'genre_name', 'condition_name', 'owner_username']