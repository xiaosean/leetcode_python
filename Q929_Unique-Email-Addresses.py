class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # preprocess
        filter_emails = []
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.replace(".", "")
            if "+" in local_name:
                local_name = local_name[:local_name.index("+")]
            filter_emails += [local_name + "@" + domain_name ]
        return(len(set(filter_emails)))