from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/Cover.pt')
 
    def get_media(self):
        results = []
        i=1
        brains = api.content.find(context=api.portal.get(), portal_type='Media')
        for brain in brains:
            item = brain.getObject()
            url=item.url.split('watch?v=')[0]+'embed/'+item.url.split('watch?v=')[1]

            results.append({
                'title':item.title,
                'description':item.description,
                'url':str(url),
                'count':i
            })
            i+=1
        return results
        

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

    def get_url(self):
        url=self.context.url
        url0=url.split('watch?v=')[0]
        url1=url.split('watch?v=')[1]
        newUrl=url0+'embed/'+url1
        return newUrl

    def __call__(self):
    
        return self.template()