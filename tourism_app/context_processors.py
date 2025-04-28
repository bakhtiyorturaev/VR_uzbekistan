from .head_footer_models import HeaderSettings, FooterSettings


def header_settings(request):
    try:
        header = HeaderSettings.objects.get(is_active=True)
    except HeaderSettings.DoesNotExist:
        header = None
    return {'header_settings': header}

def footer_settings(request):
    try:
        footer = FooterSettings.objects.get(is_active=True)
    except FooterSettings.DoesNotExist:
        footer = None
    return {'footer_settings': footer}