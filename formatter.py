def display_information(result):
    """Print a readable report using the API result."""
    details = result.get("details") or {}


    def value(key):
        item = details.get(key)
        return item if item not in (None, "") else "Not available"


    print("\n" + "=" * 55)
    print("                      IP INSIGHT")
    print("               PUBLIC IP INFORMATION")
    print("=" * 55)


    print("\nIP ADDRESS")
    print("-" * 55)
    print(f"IPv4       : {result.get('ipv4') or 'Not available'}")
    print(f"IPv6       : {result.get('ipv6') or 'Not available'}")


    print("\nNETWORK INFORMATION")
    print("-" * 55)
    print(f"ISP / Org  : {value('org')}")
    print(f"ASN        : {value('asn')}")
    print(f"Network    : {value('network')}")


    print("\nLOCATION INFORMATION")
    print("-" * 55)
    print(f"Country    : {value('country_name')}")
    print(f"Code       : {value('country_code')}")
    print(f"Region     : {value('region')}")
    print(f"City       : {value('city')}")


    print("\nGEOLOCATION")
    print("-" * 55)
    print(f"Latitude   : {value('latitude')}")
    print(f"Longitude  : {value('longitude')}")


    print("\n" + "=" * 55)
    print("                    END OF REPORT")
    print("=" * 55)
