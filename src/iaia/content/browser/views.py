from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from bs4 import BeautifulSoup
from zope.component import getMultiAdapter
import random


class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/Cover.pt')

    def get_media(self):
        portal = api.portal.get()
        media_result = []
        count = 1
        brains = api.content.find(context=portal['media_platform'], portal_type='Media',
        sort_on='created', sort_order='reverse', sort_limit=4)
        for brain in brains:
            item = brain.getObject()
            media_result.append({
                'title': item.title,
                'description': item.description,
                'youtube': item.youtube,
                'count': count
            })
            count += 1
        return media_result

    def get_news_item(self):
        portal = api.portal.get()
        result_news_item = []

        brains = api.content.find(context=portal['news'], portal_type='News Item',
        sort_on='created', sort_order='reverse', sort_limit=10, review_state='published')[0:10]

        return brains

    def get_news_item_title(self,brain):

        result = brain.getObject()
        title = result.title[:22]

        return title

    def get_document(self):
        portal = api.portal.get()

        brains = api.content.find(context=portal['economy']['market'], portal_type='Document',
        sort_on='created', sort_order='reverse', sort_limit=10)

        brains = list(brains)
        random.shuffle(brains)

        return brains

    def toLocalizedTime(self, time):
        plone = getMultiAdapter((self.context, self.request), name="plone")

        return plone.toLocalizedTime(time, long_format=0)

    def __call__(self):
        return self.template()


class FaqView(BrowserView):
    # template = ViewPageTemplateFile('template/CoverView.pt')

    def __call__(self):
        return


class FaqListView(BrowserView):
    template = ViewPageTemplateFile('template/FaqList.pt')

    def get_faqlist(self):

        documents = api.content.find(
            context=api.portal.get(), portal_type='Faq')
        return documents

    def __call__(self):

        return self.template()


class Media(BrowserView):
    template = ViewPageTemplateFile('template/Media.pt')

    def get_youtube(self):

        process = ''
        result = ''
        brains = api.content.find(
            context=self.context, portal_type='Media')
        for brain in brains:
            item = brain.getObject()
            process = item.youtube.split('560')[0]+'100%'+item.youtube.split('560')[1]
            result = process.split('315')[0]+'450'+process.split('315')[1]

        return result

    def __call__(self):
        return self.template()


class LoginView(BrowserView):
    template = ViewPageTemplateFile('template/user_login.pt')

    def __call__(self):
        return template
