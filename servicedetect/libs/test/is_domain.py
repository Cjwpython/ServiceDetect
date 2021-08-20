# coding: utf-8
from servicedetect.libs.iplib import is_domain

# target = "10.0.81.9"
# target = "www.baidu.com"
target = "baidu.com"

print(is_domain(target, return_real_ip=True))
