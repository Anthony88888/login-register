import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

        subject, form_email, to = '来自currylinux.github.io的测试邮件', 'devops8@163.com', 'rosecar258@gmail.com'
        text_content = '欢迎访问currylinux.github.io, 这里是curry的博客和教程站点, 本站专注于Python、Django和机器学习技术的分享! '
        html_content = '<p>欢迎访问<a href="https://currylinux.github.io" target=blank>www.currylinux.io</a>, 这里是curry的博客和教程站点, 本站专注于Python、Django和机器学习技术的分享!</p>'
        msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

