from django.views.generic.edit import FormView

from .forms import SetUserRoleForm


class SetRoleView(FormView):
    template_name = 'user/set_role_form.html'
    form_class = SetUserRoleForm
