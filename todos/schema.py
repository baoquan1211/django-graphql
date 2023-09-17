from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from todos.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        filter_fields = "__all__"


class Query(graphene.ObjectType):
    todos = graphene.Field(TodoType, name=graphene.String())
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info, **kwargs):
        # Querying a list
        return Todo.objects.all()

    def resolve_todos(root, info, name):
        # Querying a single todo
        return Todo.objects.get(name=name)


schema = graphene.Schema(query=Query)
