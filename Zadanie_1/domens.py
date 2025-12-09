import dns.resolver
import re

def check_email_domains(email_list):
    for email in email_list:
        domain = email.split('@')[-1]
        # Проверка валидности домена
        if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', domain):
            print(f"{email}: домен отсутствует")
            continue
        
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            if not mx_records:
                print(f"{email}: MX-записи отсутствуют или некорректны")
            else:
                print(f"{email}: домен валиден")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"{email}: домен отсутствует")
        except dns.exception.DNSException:
            print(f"{email}: ошибка проверки домена")

if __name__ == "__main__":
    emails = ["makarovm2007@gmail.com", "tempi2f@gmail.com", "mmaks@mail.ru"]
    check_email_domains(emails)