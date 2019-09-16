import re

class UniqueEmail:
    def numUniqueEmails(self, emails: 'List[str]') -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            name = local.split('+')[0]
            name = name.replace('.', '')
            seen.add('@'.join([name, domain]))
        return len(seen)

    def numUniqueEmails2(self, emails: 'List[str]') -> int:
        seen = set()
        for email in emails:
            local, domain = email.split("@")
            local = re.sub(r'\+.+$', '', local).replace('.', '')
            seen.add(local+"@"+domain)
        return len(seen)
            