import dns.resolver
def resolve_domain(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        print(f"Result-> {domain}:")
        for ip in result:
            print(ip)
    except Exception as e:
        print(f"U wrote wrong domain, check it on website or ask GPT to write some domain example for u: {e}")

if __name__ == "__main__":
    domain = input("Write google.com to chech if it works (for example): ")
    resolve_domain(domain)