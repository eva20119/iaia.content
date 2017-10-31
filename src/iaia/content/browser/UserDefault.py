from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form
from zope import schema
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from .. import _


class IUserDefault(Form.Schema):
    footer = schema.Text(
        title=_(u"Footer Information"),
        required=False
    )
    phone = schema.TextLine(
        title=_(u'Phone Number'),
        required=False
    )
    email = schema.TextLine(
         title=_(u'Contact Email'),
         required=False
     )


class UserDefaultControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IUserDefault

UserDefaultControlPanelView = layout.wrap_form(UserDefaultControlPanelForm, ControlPanelFormWrapper)
UserDefaultControlPanelView.label = _(u"User Default")
