from django.http import HttpResponse
import datetime
from django import forms
from django.views.generic.edit import FormView
from django.template import RequestContext

NO_ERROR = "0"
SYNTAX_ERROR = "1"
TYPE_ERROR = "2"
RUNTIME_ERROR = "3"

CODE_EXO1= (
    ("int main ()",                 RUNTIME_ERROR, "Main should have two arguments"),
    ("{",                           NO_ERROR,       ""),
    ("    int i ;",                 NO_ERROR,       ""),
    ("    int j = k + 1 ;",         TYPE_ERROR,     "k is undefined"),
    ("    int a[] = {1,2,3}",       SYNTAX_ERROR,   "Missing semi-column"),
    ("    j = a + 6 ;",             TYPE_ERROR,     "We can't add an array to an int"),
    ("    a[4] = 7 ;",              NO_ERROR,       ""),
    ("    printf(hello world\\n) ;", SYNTAX_ERROR,   "Missing quotes"),
    ("}",                           TYPE_ERROR,     "missing return statement"),
)

CHOICES = (
    (NO_ERROR,"no error"),
    (SYNTAX_ERROR, "syntax error"),
    (TYPE_ERROR, "type error"),
    (RUNTIME_ERROR, "runtime error"),)

class LineField(forms.ChoiceField):
    def __init__(self, code, answer, tips):
        super(LineField, self).__init__(
            label = code, widget=forms.RadioSelect(), choices=CHOICES, initial=0,)
        self.code = code
        self.answer = answer
        self.tips = tips

    def validate(self, value):
        print "%s =? %s" % (value,self.answer)
        if self.answer == value:
            return value
        else:
            raise forms.ValidationError("")
        
class ExerciseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        for i,(code,answer,tips) in enumerate(CODE_EXO1):
            code = code.replace(" ", "&nbsp;")
            self.fields['line%d' % i] = LineField(code,answer,tips)

class Exercise1(FormView):

    template_name = "week1/exercise1.html"
    form_class = ExerciseForm
    #success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        status = None
        print request.POST
        if '_check' in request.POST:
            print form.is_valid()
            status = "check"
        return self.render_to_response(self.get_context_data(form=form, status=status))


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Exercise1, self).get_context_data(**kwargs)
        context['code'] = "\n".join(map(lambda x: x[0], CODE_EXO1))
        return context

def exercise1(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
