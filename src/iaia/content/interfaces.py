# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from iaia.content import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.textfield import RichText
from z3c.relationfield import RelationList
from plone.namedfile.field import NamedBlobImage


class IIaiaContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICover(Interface):
    title = schema.TextLine(
        title=_(u'標題'),
        required=False,
    )
    description = schema.Text(
        title=_(u'描述'),
        required=False,
    )
    cover_image1 = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )
    cover_image2 = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )
    cover_image3 = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )
    cover_image4 = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )
    cover_image5 = NamedBlobImage(
        title=_(u"Cover Image"),
        required=False,
    )
   

class IFaq(Interface):
    title = schema.TextLine(
        title=_(u'問題'),
        required=False,
    )
    answer = RichText(
        title=_(u'回答'),
        required=False,
    )


class IMedia(Interface):
    title = schema.TextLine(
        title=_(u'標題'),
        required=False,
    )
    description = schema.Text(
        title=_(u'描述'),
        required=False,
    )
    youtube = schema.Text(
        title=_(u'嵌入影片'),
        required=False,
    )
