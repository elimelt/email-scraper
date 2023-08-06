import json

# Load JSON data containing parsed emails
with open('parsed.json', 'r') as json_file:
    emails_data = json.load(json_file)

# List of internship-related keywords to check in subject and parsed text
internship_keywords = ['internship', 'intern', 'application', 'recruiting']

# Prepare data for classification
internship_emails = []
non_internship_emails = []

for email in emails_data:
    if 'from' in email:
        sender =  email['from'][0]['address']
        if any([bad in sender for bad in ['github', '.edu', 'CampusPoint', 'simplify', 'handshake', 'edX', 'twitter', 'resumeworded', 'medium', 'indeed', 'edstem']]):
            continue
        
    
    if 'subject' in email and 'parsed' in email and email['parsed'].strip():
        text_content = email['parsed']
        subject = email['subject'].lower()

        # Check for internship keywords in subject or parsed text
        is_internship = any(keyword in subject or keyword in text_content for keyword in internship_keywords)

        if is_internship:
            internship_emails.append(email)
        else:
            non_internship_emails.append(email)

# Write internship emails to internship.json
with open('internship.json', 'w') as internship_file:
    json.dump(internship_emails, internship_file, indent=2)

# Write non-internship emails to non_internship.json
with open('non_internship.json', 'w') as non_internship_file:
    json.dump(non_internship_emails, non_internship_file, indent=2)

# Print the results
print(f"Number of internship-related emails: {len(internship_emails)}")
print(f"Number of non-internship emails: {len(non_internship_emails)}")

