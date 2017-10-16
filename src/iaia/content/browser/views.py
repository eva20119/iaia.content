from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from bs4 import BeautifulSoup
import random

class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/Cover.pt')
 
    def get_media(self):
        portal=api.portal.get()
        result_media = []
        i=1
        brains = api.content.find(context=portal['media_platform'], portal_type='Media',
        sort_on='created', sort_order='reverse', sort_limit=3)

        return brains
        
    def get_news_item(self):
        portal=api.portal.get()
        result_news_item = []
        i=1
        brains = api.content.find(context=portal['news'], portal_type='News Item',
        sort_on='created', sort_order='reverse', sort_limit=10)

        return brains

    def get_document(self):
        portal=api.portal.get()
        result_document = []
        i=1
        brains = api.content.find(context=portal['economy']['market'], portal_type='Document',
        sort_on='created', sort_order='reverse', sort_limit=10)

        brains=list(brains)
        random.shuffle(brains)

        return brains
    
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

    def __call__(self):
        return self.template()