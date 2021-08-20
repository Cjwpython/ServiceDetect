# coding: utf-8
from optparse import OptionParser, OptionGroup


def cmdline_parse(cmd_args=None):
    usage = "usage: %prog -s http://example.com [options]"
    parser = OptionParser(usage=usage)

    base = OptionGroup(parser, "基础")
    base.add_option("-s", "--site",
                    type="string",
                    dest='site',
                    help="需要扫描的目标")

    hostscan = OptionGroup(parser, "存活检测")
    hostscan.add_option("-l", "--hostalive",
                        action="store_true",
                        dest='hostalive',
                        default=False,
                        help="是否进行目标存活探测(默认False)")
    hostscan.add_option("-n", "--nodnssolve",
                        action="store_true",
                        dest='noddnssolve',
                        default=True,
                        help="是否进行目标的dns解析(默认True)")
    portscan = OptionGroup(parser, "端口扫描技术")
    portscan.add_option("", "--tcpsyn",
                        action="store_true",
                        dest='tcpsyn',
                        default=False,
                        help="tcp syn扫描(默认False)")
    portscan.add_option("", "--tcpack",
                        action="store_true",
                        dest='tcpack',
                        default=False,
                        help="tcp ack扫描(默认False)")
    portscan.add_option("", "--tcpwindow",
                        action="store_true",
                        dest='tcpwindow',
                        default=False,
                        help="tcp 窗口扫描(默认False)")
    portscan.add_option("", "--tcpmaimon",
                        action="store_true",
                        dest='tcpmaimon',
                        default=False,
                        help="tcp maimon扫描(默认False)")
    portscan.add_option("", "--tcp",
                        action="store_true",
                        dest='tcp',
                        default=True,
                        help="tcp连接扫描(默认True)")
    portscan.add_option("", "--upd",
                        action="store_true",
                        dest='udp',
                        default=True,
                        help="udp连接测试")
    portscan.add_option("", "--tcpport",
                        type="string",
                        dest='tcpport',
                        help="tcp扫描的端口")
    portscan.add_option("", "--updport",
                        type="string",
                        dest='udpport',
                        help="udp扫描的端口")
    portscan.add_option("", "--exclide-ports",
                        type="string",
                        dest='exclide_ports',
                        help="排除扫描的端口")
    servicescan = OptionGroup(parser, "服务发现技术")
    servicescan.add_option("-v", "--serviceversion",
                           action="store_true",
                           dest='exclide_ports',
                           default=False,
                           help="版本探测(默认False)")
    servicescan.add_option("", "--version-intensity",
                           type="int",
                           dest='version_intensity',
                           default=2,
                           help="版本扫描强度1-9(数字越大识别越高，时间也越长,默认为2)")
    servicescan.add_option("", "--version-all",
                           action="store_true",
                           dest='version_all',
                           default=False,
                           help="尝试每个版本的识别(默认不开启，version_intensity设置为9,变向的开启了这个选项)")
    osscan = OptionGroup(parser, "操作系统检测")
    osscan.add_option("-o", "--osdetect",
                      action="store_true",
                      dest='osdetect',
                      default=False,
                      help="操作系统识别(默认不开启)")
    osscan.add_option("", "--osscan-guess",
                           action="store_true",
                           dest='osscan_guess',
                           default=False,
                           help="猜操作系统检测结果:当 Nmap 无法检测到完美的 OS 匹配时，它有时会提供接近匹配的可能性。默认情况下，Nmap 必须非常接近匹配才能执行此操作。这些（等效）选项中的任何一个都使 Nmap 猜测更加积极。Nmap 仍然会告诉您何时打印不完美的匹配并显示每个猜测的置信度（百分比）。(默认不开启)")
    osscan.add_option("", "--max-os-tries",
                      type="int",
                      dest='max_os_tries',
                      default=5,
                      help="设置针对目标的操作系统检测尝试的最大次数(默认为：5)")
    osscan.add_option("", "--osscan-limit",
                      action="store_true",
                      dest='osscan_limit',
                      default=False,
                      help="将操作系统检测限制为有希望的目标:如果至少找到一个打开和一个关闭的 TCP 端口，操作系统检测会更有效。设置此选项，Nmap 甚至不会尝试针对不符合此标准的主机进行操作系统检测。这可以节省大量时间，尤其是在-Pn对许多主机进行扫描时。仅当使用-O或请求操作系统检测时才重要-A。(默认不开启)")
    parser.add_option_group(base)
    parser.add_option_group(hostscan)
    parser.add_option_group(portscan)
    parser.add_option_group(servicescan)
    parser.add_option_group(osscan)
    options, args = parser.parse_args(args=cmd_args)
