import os
import re
import netifaces
import subprocess


class NetWorkConfig:
    def __init__(self):
        pass

    @staticmethod
    def check_network_isvalid(ip, netmask, gateway, dns):
        """
        判断用户输入的网络配置是否可用
        :param ip: str，IP地址
        :param netmask: str，子网掩码
        :param gateway: str，网关
        :param dns: str，DNS
        :return: bool，True表示配置可用，False表示配置不可用
        """
        # 判断IP地址是否合法
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            return False

        # 判断子网掩码是否合法
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", netmask):
            return False

        # 判断网关是否合法
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", gateway):
            return False

        # 判断DNS是否合法
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", dns):
            return False

        # 判断网络是否可用
        cmd_ping = f"ping {gateway}"
        try:
            subprocess.check_call(
                cmd_ping, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        except subprocess.CalledProcessError:
            return False

        return True

    @staticmethod
    def get_network_config(physical=False):
        """
        获取网卡配置信息
        :param physical: 是否仅获取物理网卡
        :return: 返回服务器网卡配置
        """
        i_faces = netifaces.interfaces()
        configs = []
        for i in i_faces:
            if physical and not i.startswith("e"):
                continue
            addr_s = netifaces.ifaddresses(i)
            inet = addr_s.get(netifaces.AF_INET)
            if not inet:
                continue
            ip = inet[0].get("addr")
            netmask = inet[0].get("netmask")
            broadcast = inet[0].get("broadcast")
            gateway = (
                netifaces.gateways().get("default", {}).get(netifaces.AF_INET, [])[0]
            )
            dns = netifaces.gateways().get("default", {}).get(netifaces.AF_INET, [])[1]
            configs.append(
                {
                    "iface": i,
                    "ip": ip,
                    "netmask": netmask,
                    "broadcast": broadcast,
                    "gateway": gateway,
                    "dns": dns,
                }
            )
        return configs

    @staticmethod
    def _check_network_config(iface, ip_address, netmask, gateway, dns):
        """
        检查IP地址和子网掩码修改是否生效
        :param iface: 网卡
        :param ip_address: ip地址
        :param netmask: 子网掩码
        :param gateway: 网关
        :param dns: DNS
        :return: 返回配置是否生效
        """
        # 检查ip地址是否生效
        cmd = f"ifconfig {iface} | grep {ip_address}"
        output = subprocess.check_output(cmd, shell=True)
        if ip_address not in output.decode("utf-8"):
            return False

        # 检查子网掩码是否生效
        cmd = f"ifconfig {iface} | grep {netmask}"
        output = subprocess.check_output(cmd, shell=True)
        if netmask not in output.decode("utf-8"):
            return False

        # 检查默认网关是否生效
        cmd = "route"
        output = subprocess.check_output(cmd, shell=True)
        pattern = rf"{gateway}\s.*\s{iface}"
        matches = re.findall(pattern, output.decode("utf-8"), re.MULTILINE)
        if not matches:
            return False

        # 检查DNS是否生效
        with open("/etc/resolv.conf", "r") as f:
            content = f.read()
        if dns not in content:
            return False

        return True

    @staticmethod
    def _write_network_config_to_file(config, mode="w"):
        """
        配置信息写入网卡
        """
        with open("/etc/network/interfaces", mode) as f:
            f.write(config)

    @staticmethod
    def _restart_network():
        """重启网络"""
        os.system("service networking restart")

    @staticmethod
    def _cp_config(cmd=None):
        """
        拷贝配置文件
        :param cmd: backup表示备份 rollback表示回滚
        """
        if cmd == "backup":
            os.system("cp /etc/network/interfaces /etc/network/interfaces.bak")
        if cmd == "rollback":
            os.system("cp /etc/network/interfaces.bak /etc/network/interfaces")

    def set_network_config(self, iface, ip_address, netmask, gateway, dns):
        """
        修改网络配置
        :param iface: 网卡名称
        :param ip_address: IP地址
        :param netmask: 子网掩码
        :param gateway: 默认网关
        :param dns: DNS服务器
        :return: 是否修改成功
        """
        self._cp_config(cmd="backup")

        config = f"""
            auto {iface}
            iface {iface} inet static
            address {ip_address}
            netmask {netmask}
            gateway {gateway}
            dns-nameservers {dns}
        """

        self._write_network_config_to_file(config, "w")
        self._restart_network()
        if self._check_network_config(iface, ip_address, netmask, gateway, dns):
            return True
        else:
            self._cp_config(cmd="rollback")
            self._restart_network()
            return False


network = NetWorkConfig()
