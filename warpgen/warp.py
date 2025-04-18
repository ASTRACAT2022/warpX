def generate_warp_config(dns="cloudflare"):
    config = f"[Interface]\nPrivateKey = xxx\nDNS = {1.1.1.1 if dns == 'cloudflare' else '8.8.8.8'}"
    return config
