
"""Retrieve public IPv4, IPv6 and network information."""

import ipaddress
import requests

IPV4_URL = "https://api4.ipify.org?format=json"
IPV6_URL = "https://api6.ipify.org?format=json"
DETAILS_URL = "https://ipapi.co/{ip}/json/"


def get_public_ip(version):
    """Retrieve the public address for a specific IP version."""
    url = IPV4_URL if version == 4 else IPV6_URL

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        ip = response.json()["ip"]

        if ipaddress.ip_address(ip).version != version:
            return None

        return ip
    except (requests.RequestException, ValueError, KeyError):
        return None


def get_ip_details(ip):
    """Retrieve geolocation and ISP information for an IP address."""
    if not ip:
        return {}

    try:
        response = requests.get(
            DETAILS_URL.format(ip=ip), timeout=5
        )
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict) or data.get("error"):
            return {}

        return data
    except (requests.RequestException, ValueError):
        return {}


def get_all_information():
    """Collect both IP versions and details for the available address."""
    ipv4 = get_public_ip(4)
    ipv6 = get_public_ip(6)

    details = get_ip_details(ipv4 or ipv6)

    return {
        "ipv4": ipv4,
        "ipv6": ipv6,
        "details": details,
    }
