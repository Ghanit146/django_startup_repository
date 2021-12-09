
from django.forms import ModelForm
from .models import Idea




class IdeaForm(ModelForm):
    class Meta:
        model = Idea

        fields = ['title', 'problem', 'solution', 'business_model', 'market', 'phase', 'incubated','team', 'logs']



