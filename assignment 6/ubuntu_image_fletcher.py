try:
    import requests
except ImportError:
    print("Error: The 'requests' library is not installed.")
    print("Please install it by running: pip install requests")
    exit(1)

import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def calculate_file_hash(filepath):
    """Calculate MD5 hash of a file to check for duplicates."""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception:
        return None

def is_safe_file_type(filename, content_type):
    """Check if the file type is safe for download."""
    safe_image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'}
    safe_content_types = {'image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp', 'image/tiff'}
    
    file_ext = os.path.splitext(filename)[1].lower()
    
    if content_type and content_type not in safe_content_types:
        return False
        
    if file_ext not in safe_image_extensions:
        return False
        
    return True

def download_image(url, download_folder="Fetched_Images"):
    """
    Download an image from a URL with proper error handling and safety checks.
    
    Args:
        url (str): The URL of the image to download
        download_folder (str): The folder to save downloaded images to
    
    Returns:
        dict: Result of the download attempt with status and message
    """
    result = {"success": False, "message": "", "filepath": ""}
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)
        
        # Send HEAD request first to check headers
        head_response = requests.head(url, timeout=10, allow_redirects=True)
        head_response.raise_for_status()
        
        # Check content type for safety
        content_type = head_response.headers.get('content-type', '').split(';')[0]
        content_length = head_response.headers.get('content-length')
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            # Generate a filename based on URL hash and content type
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            extension = ".jpg"  # default extension
            if content_type:
                extension = f".{content_type.split('/')[-1]}"
            filename = f"image_{url_hash}{extension}"
        
        # Check if file type is safe
        if not is_safe_file_type(filename, content_type):
            result["message"] = f"Unsafe file type: {content_type or filename}"
            return result
        
        # Check file size if available (limit to 10MB)
        if content_length and int(content_length) > 10 * 1024 * 1024:
            result["message"] = f"File too large: {int(content_length) / 1024 / 1024:.1f}MB"
            return result
        
        filepath = os.path.join(download_folder, filename)
        
        # Check for existing file with same content
        if os.path.exists(filepath):
            # If file exists, check if it's the same content
            existing_hash = calculate_file_hash(filepath)
            
            # Get the actual image to compare
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            # Calculate hash of the response content without saving yet
            new_hash = hashlib.md5(response.content).hexdigest()
            
            if existing_hash == new_hash:
                result["success"] = True
                result["message"] = f"Image already exists: {filename}"
                result["filepath"] = filepath
                return result
        
        # Download the image if it doesn't exist or is different
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Verify content type matches what we expected
        actual_content_type = response.headers.get('content-type', '').split(';')[0]
        if content_type and actual_content_type != content_type:
            result["message"] = f"Content type mismatch: expected {content_type}, got {actual_content_type}"
            return result
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        result["success"] = True
        result["message"] = f"Successfully fetched: {filename}"
        result["filepath"] = filepath
        
    except requests.exceptions.RequestException as e:
        result["message"] = f"Connection error: {e}"
    except Exception as e:
        result["message"] = f"An error occurred: {e}"
    
    return result

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URLs from user
    urls_input = input("Please enter image URLs (separated by commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    if not urls:
        print("No URLs provided. Exiting.")
        return
    
    successful_downloads = 0
    
    for i, url in enumerate(urls, 1):
        print(f"\nProcessing URL {i} of {len(urls)}: {url}")
        
        result = download_image(url)
        
        if result["success"]:
            print(f"✓ {result['message']}")
            if result['filepath']:
                print(f"✓ Image saved to {result['filepath']}")
            successful_downloads += 1
        else:
            print(f"✗ {result['message']}")
    
    print(f"\nDownloaded {successful_downloads} of {len(urls)} images.")
    
    if successful_downloads > 0:
        print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()