import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphene import ObjectType

from .models import Text, TagText


class TextType(DjangoObjectType):
    class Meta:
        model = Text
        fields = '__all__'


class AddText(graphene.Mutation):
    addText = graphene.Field(TextType)

    class Arguments:
        text = graphene.String(required = True)

    def mutate(self, info, text, **kwargs):
        text = Text(
            text = text,
        )

        text.save()

        return AddText(addText = text)


class Query(graphene.ObjectType):
    text = graphene.List(TextType)
    def resolve_text(self,info,**kwargs):
        return Text.objects.all()
    

class Mutation(graphene.ObjectType):
    add_text = AddText.Field()
