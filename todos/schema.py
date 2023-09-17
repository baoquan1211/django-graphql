from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from todos.models import Todo


class TodoNode(DjangoObjectType):
    class Meta:
        model = Todo
        filter_fields = ["name", "done"]
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    todo = graphene.relay.Node.Field(TodoNode)
    all_todos = DjangoFilterConnectionField(TodoNode)
