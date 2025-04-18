def generate_warp_config(dns="cloudflare"):
    dns_map = {
        "cloudflare": "1.1.1.1",
        "google": "8.8.8.8",
        "adguard": "94.140.14.14"
    }
    return f"[Interface]\nPrivateKey = xxx\nDNS = {dns_map.get(dns, '1.1.1.1')}"
