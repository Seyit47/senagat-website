from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import *

@registry.register_document
class NewsDocument(Document):
    class Index:
        name = 'news'

    class Django:
        model = News

        fields = [
            'id',
            'title',
            'thumbnail',
            'published_date',
        ]

@registry.register_document
class TenderDocument(Document):
    class Index:
        name = 'tender'

    class Django:
        model = Tender

        fields = [
            'id',
            'title',
            'thumbnail',
            'published_date',
        ]