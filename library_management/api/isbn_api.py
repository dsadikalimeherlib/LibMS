import frappe
import requests

@frappe.whitelist()
def fetch_book_details(isbn):
    try:
        url = f"https://isbnsearch.org/isbn/{isbn}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Accept-Language':'en-US,en;q=0.9'
            }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            # Convert the HTML response content to a string
            html_content = response.text
            
            # Check if captcha is detected
            if "Please Verify to Continue" in html_content:
                
                # Handle captcha
                return frappe.throw(f"Captcha detected. Please try again later.")
            # {'error': 'Captcha detected. Please try again later.'}
            
            # Extracting book details using string manipulation
            title_start = html_content.find('<h1>') + len('<h1>')
            title_end = html_content.find('</h1>', title_start)
            title = html_content[title_start:title_end].strip()
            
            if title == "Please Verify to Continue":
                return frappe.throw(f"Captcha detected. Please try again later.")

            author_start = html_content.find('<strong>Author:</strong>') + len('<strong>Author:</strong>')
            author_end = html_content.find('</p>', author_start)
            author = html_content[author_start:author_end].strip()

            publisher_start = html_content.find('<strong>Publisher:</strong>') + len('<strong>Publisher:</strong>')
            publisher_end = html_content.find('</p>', publisher_start)
            publisher = html_content[publisher_start:publisher_end].strip()

            published_year_start = html_content.find('<strong>Published:</strong>') + len('<strong>Published:</strong>')
            published_year_end = html_content.find('</p>', published_year_start)
            published_year = html_content[published_year_start:published_year_end].strip()

            # Extract image URL
            image_start = html_content.find('<div class="image">') + len('<div class="image">')
            image_end = html_content.find('</div>', image_start)
            image_tag = html_content[image_start:image_end]
            image_url_start = image_tag.find('src="') + len('src="')
            image_url_end = image_tag.find('"', image_url_start)
            image_url = image_tag[image_url_start:image_url_end]

            # Return the extracted book details
            return {
                'title': title,
                'author': author,
                'publisher': publisher,
                'published_year': published_year,
                'image_url': image_url
            }
        else:
            frappe.throw(f"Unexpected error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        frappe.throw(f"Error: {e}")
