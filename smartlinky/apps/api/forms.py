from django import forms

class AddLinkForm(forms.Form):
    url = forms.URLField(required=True)
    page_title = forms.CharField(required=True)
    section_id = forms.CharField(required=True)
    section_title = forms.CharField(required=True)
    link_url = forms.URLField(required=True)

