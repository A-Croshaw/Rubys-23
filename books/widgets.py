from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class MyClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Image')
    input_text = _('')
    template_name = 'books/widgets/my_clearable_file_input.html'
