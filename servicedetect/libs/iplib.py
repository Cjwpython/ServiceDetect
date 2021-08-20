# coding: utf-8
import ipaddress
import socket


def is_ip(target, return_version=False):
    # 判断是否为ip
    try:
        ipaddr = ipaddress.ip_address(target)
        if return_version:
            return True, ipaddr.version
        return True
    except ValueError as e:
        if return_version:
            return False, 0
        return False


def is_domain(target, return_real_ip=False):
    # 判断是否为域名
    if is_ip(target):
        return False
    elif is_ip_segment(target):
        return False
    real_ip = socket.gethostbyname(target)
    if return_real_ip:
        return True, real_ip
    return True


def is_ip_segment(target, return_subnet_num=False):
    # 判断是否为ip段
    try:
        ipaddr = ipaddress.ip_network(target, strict=False)
        if ipaddr.prefixlen == 32 or ipaddr.prefixlen == 128:
            if return_subnet_num:
                return False, ipaddr.prefixlen
            return False
        if return_subnet_num:
            return True, ipaddr.prefixlen
        return True
    except ValueError:
        if return_subnet_num:
            return False, 0
        return False



