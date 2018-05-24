# coding=utf-8

from typing import Union

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

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

    author = graphene.Field(
        TypeAuthor,
        author_id=graphene.Argument(type=graphene.Int, required=False),
        name_first=graphene.Argument(type=graphene.String, required=False),
        name_last=graphene.Argument(type=graphene.String, required=False),
    )

    books = graphene.List(
        of_type=TypeBook,
        title=graphene.Argument(type=graphene.String, required=False),
        year=graphene.Argument(type=graphene.Int, required=False),
    )

    @staticmethod
    def resolve_author(
        args,
        info,
        author_id: Union[int, None] = None,
        name_first: Union[str, None] = None,
        name_last: Union[str, None] = None,
    ):
        query = TypeAuthor.get_query(info=info)

        if author_id:
            query = query.filter(Author.author_id == author_id)

        if name_first:
            query = query.filter(Author.name_first == name_first)

        if name_last:
            query = query.filter(Author.name_last == name_last)

        author = query.first()

        return author

    @staticmethod
    def resolve_books(
        args,
        info,
        title: Union[str, None] = None,
        year: Union[int, None] = None,
    ):
        query = TypeBook.get_query(info=info)

        if title:
            query = query.filter(Book.title == title)

        if year:
            query = query.filter(Book.year == year)

        books = query.all()

        return books


schema = graphene.Schema(
    query=Query,
    types=[
        TypeAuthor,
        TypeBook,
        TypeAuthorBook,
    ]
)
