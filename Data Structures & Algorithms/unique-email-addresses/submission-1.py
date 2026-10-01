class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            name,domain = email.split('@')
            name = name.split('+')[0].replace('.','')
            final_mail = f"{name}@{domain}"
            unique_emails.add(final_mail)
            print(f'{final_mail}')

        return len(unique_emails)
        
        