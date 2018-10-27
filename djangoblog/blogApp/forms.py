from django import forms

from.models import article,comment
from django.forms import ModelForm

class createForms(forms.ModelForm):
	class Meta:
		model=article
		fields=[

		'title',
		'body',
		'image',
		'category'
		]


class commentForms(forms.ModelForm):
	class Meta:
		model=comment
		fields=[

			'name',
			'email',
			'post_comment'

		]