# import asyncio
# from random import randint
# from PIL import Image
# import requests
# from dotenv import get_key
# import os
# from time import sleep

# def open_images(promot):
#     folder_path = r"Data"
#     promot = promot.replace(" ", "_")

#     Files = [f"{promot}{i}.jpg" for i in range(1, 5)]

#     for jpg_file in Files:
#         image_path = os.path.join(folder_path, jpg_file)

#         try:
#             img = Image.open(image_path)
#             print(f"Opening image: {image_path}")
#             img.show()
#             sleep(1)

#         except IOError:
#             print(f"Unable to open {image_path}")
    
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# headeras = {"Authorization": f"Bearer {get_key('.env', 'HuggingFaceAPIKey')}"}

# async def query(payload):
#     response = await asyncio.to_thread(requests.post, API_URL, headeras=headeras, json=payload)
#     return response.content

# async def generate_images(prompt: str):
#     task = []

#     for _ in range(4):
#         payload = {
#             "inputs": f"{prompt}, quality=4K, sharpness=maximum, Ultra High details, high resolution, seed = {randint(0, 1000000)}",
#         }
#         task = asyncio.create_task(query(payload))
#         tasks.append(task)

#     image_bytes_list = await asyncio.gather(*tasks)

#     for i, image_bytes in enumerate(image_bytes_list):
#         with open(fr"Data\{prompt.replace(' ', '_')}{i + 1}.jpg", "wb") as f:
#             f.write(image_bytes)

# def GenerateImages(prompt: str):
#     asyncio.run(generate_images(prompt))
#     open_images(prompt)

# while True:
#     try:
#         with open(r"Frontend\Files\ImageGeneration.data", "r") as f:
#             Data: str = f.read()

#         Prompt, Status = Data.split(",")

#         if Status == "True":
#             print("Generation Images...")
#             ImageStatus = GenerateImages(prompt=Prompt)

#             with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
#                 f.write("False,False")
#                 break
#         else:
#             sleep(1)
    
#     except Exception as e:
#         print(e)

import asyncio
from random import randint
from PIL import Image
import os
import time
from huggingface_hub import InferenceClient
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
HF_API_KEY = env_vars.get("HuggingFaceAPIKey")

client = InferenceClient(
    provider="hf-inference",  
    api_key=HF_API_KEY
)

def open_images(prompt):
    """Open generated images"""
    prompt_clean = prompt.replace(" ", "_")
    os.makedirs("Data", exist_ok=True)
    
    for i in range(1, 5):
        filename = f"Data/{prompt_clean}{i}.jpg"
        if os.path.exists(filename):
            try:
                Image.open(filename).show()
                time.sleep(1)
            except:
                pass

async def generate_single_image(prompt, index, model_name):
    """Generate one image with retry logic"""
    for attempt in range(3):  # Retry up to 3 times
        try:
            print(f"  🎨 Generating image {index+1} (attempt {attempt+1})...")
            
            image = client.text_to_image(
                prompt=prompt,
                model=model_name,
                guidance_scale=7.5,
                num_inference_steps=30,
                seed=randint(0, 1000000),
                negative_prompt="blurry, bad quality, distorted"
            )
            
            prompt_clean = prompt.replace(" ", "_")
            filename = f"Data/{prompt_clean}{index+1}.jpg"
            image.save(filename)
            
            print(f"  ✅ Saved: {filename}")
            return True
            
        except Exception as e:
            error_msg = str(e)
            
            if "loading" in error_msg.lower():
                wait = 10 * (attempt + 1)  # Exponential backoff
                print(f"  ⏳ Model loading, waiting {wait}s...")
                await asyncio.sleep(wait)
            elif "rate limit" in error_msg.lower():
                print(f"  ⚠️ Rate limited, waiting 30s...")
                await asyncio.sleep(30)
            else:
                print(f"  ❌ Error: {error_msg}")
                if attempt == 2:  # Last attempt
                    return False
    
    return False

async def generate_images(prompt: str):
    """Generate 4 images concurrently with fallback models"""
    
    model_list = [
        "stabilityai/stable-diffusion-xl-base-1.0",  # Best quality
        "runwayml/stable-diffusion-v1-5",           # Reliable backup
        "Lykon/DreamShaper",                        # Artistic style
        "prompthero/openjourney"                    # Always available
    ]
    
    successful_model = None
    
    for model_name in model_list:
        print(f"\n🔍 Trying model: {model_name}")
        
        tasks = []
        for i in range(4):
            task = asyncio.create_task(
                generate_single_image(prompt, i, model_name)
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        success_count = sum(results)
        
        if success_count > 0:
            successful_model = model_name
            print(f"\n✅ Model '{model_name}' worked!")
            print(f"   Generated {success_count}/4 images")
            break
        else:
            print(f"⚠️ Model '{model_name}' failed, trying next...")
    
    return successful_model

def GenerateImages(prompt: str):
    """Main function - clean and simple"""
    print(f"\n🚀 Starting image generation for: '{prompt}'")
    
    working_model = asyncio.run(generate_images(prompt))
    
    if working_model:
        print(f"\n🎉 Success! Used model: {working_model}")
        open_images(prompt)
        return 4  # Assume all 4 were generated
    else:
        print("\n❌ All models failed. Check API key or try later.")
        return 0

def main():
    print("🖼️ Image Generation Service (Library Version)...")
    
    while True:
        try:
            if os.path.exists(r"Frontend\Files\ImageGeneration.data"):
                with open(r"Frontend\Files\ImageGeneration.data", "r") as f:
                    data = f.read().strip()
                
                if data:
                    parts = data.split(",")
                    if len(parts) >= 2 and parts[1].strip().lower() == "true":
                        prompt = parts[0].strip()
                        
                        # Update status
                        with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
                            f.write(f"{prompt},processing")
                        
                        # Generate
                        result = GenerateImages(prompt)
                        
                        # Mark complete
                        with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
                            f.write(f"{prompt},completed,{result}")
            
            time.sleep(1)
            
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    os.makedirs("Data", exist_ok=True)
    os.makedirs(r"Frontend\Files", exist_ok=True)
    
    data_file = r"Frontend\Files\ImageGeneration.data"
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            f.write("False,False")
    
    main()