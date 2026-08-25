import re
from django.core.validators import RegexValidator, _lazy_re_compile
from django.utils.translation import gettext_lazy as _


alphabet_re = _lazy_re_compile(r'^[ \w\-\']+\Z', re.UNICODE)
validate_alphabet = RegexValidator(
    alphabet_re,
    _("Field can only contain letters of the alphabet."),
    'invalid'
)

