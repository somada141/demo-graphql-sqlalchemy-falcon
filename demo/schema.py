# coding=utf-8

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
import sqlalchemy.orm

from demo.orm import Author
from demo.orm import Book
from demo.orm import AuthorBook


class TypeAuthor(SQLAlchemyObjectType):
    class Meta:
        model = Author


class TypeBook(SQLAlchemyObjectType):
    class Meta:
        model = Book


class TypeAuthorBook(SQLAlchemyObjectType):
    class Meta:
        model = AuthorBook


class Query(graphene.ObjectType):

    robert = graphene.Field(TypeAuthor)

    def resolve_robert(self, info):
        query = TypeAuthor.get_query(info=info)
        query = query.filter(Author.name_first == "Robert")

        robert = query.first()

        return robert


schema = graphene.Schema(
    query=Query,
    types=[
        TypeAuthor,
        TypeBook,
        TypeAuthorBook,
    ]
)
