import asyncio
import cloudinary
import cloudinary.uploader
import logging  # Add this import statement

cloudinary.config(
    cloud_name="dmofunrex",
    api_key="983299355199791",
    api_secret="sTcYUDpBRuc8LXXekb0IUaKr2N0"
)

async def upload_on_cloudinary(local_file_path):
    try:
        if not local_file_path:
            return None
        
        logging.info("cloudinary_util.py upload_on_cloudinary local_file_path -> %s", local_file_path)
        
        # Upload the file on Cloudinary
        response = cloudinary.uploader.upload(local_file_path, resource_type="auto")
        
        # File has been uploaded successfully
        logging.info("cloudinary_util.py file is uploaded on Cloudinary response -> %s", response)
        
        # Optionally, delete the local file
        # os.remove(local_file_path)
        
        return response
    except cloudinary.exceptions.Error as e:  # Update the exception handling
        logging.error("An error occurred during Cloudinary upload: %s", str(e))
        return None
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
        return None

# Example usage
async def main():
    await upload_on_cloudinary("uploads/phone.jpg")

# Run the main function
asyncio.run(main())
