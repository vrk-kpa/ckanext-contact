import logging

log = logging.getLogger(__name__)


def check_captcha(request):
    captcha_response_field = request.params.get('captcha_response_field', '')
    captcha_challenge_field = request.params.get('captcha_challenge_field')
    try:
        expected_result = sum(int(n) for n in captcha_challenge_field.split())
        received_result = int(captcha_response_field)
    except:
        raise CaptchaError()

    if received_result != expected_result:
        raise CaptchaError()


class CaptchaError(ValueError):
    pass
