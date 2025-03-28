from django import forms
from companywebsite.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    
    class Meta:
        model = Page  # Specify the model to use
        exclude = ('category',)  # Exclude the category field from the form, we'll set it in the view

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If the URL does not start with 'http://', add it automatically
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data
