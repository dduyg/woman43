"""
═══════════════════════════════════════════════════════════════════
　　　　　　　　　Ｆ Ｏ Ｎ Ｔ 　Ｃ Ａ Ｔ Ａ Ｌ Ｏ Ｇ 　　　　　　　　　
═══════════════════════════════════════════════════════════════════

　░▒▓█  ＴＡＧ　ＰＡＬＥＴＴＥ  █▓▒░

　geometric • formal • handwritten • fatface • monospaced • techno
　pixel • medieval • art nouveau • blobby • distressed • wood
　wacky • shaded • marker • futuristic • vintage • calm • playful
　sophisticated • business • stiff • childlike • horror • distorted
　clean • warm • aesthetic • brutalist • modular • neutral
　contemporary • rounded • approachable • humanist • coding
　retro • android

═══════════════════════════════════════════════════════════════════
"""

import json
import requests
from getpass import getpass
from base64 import b64encode, b64decode
import io

try:
    import google.generativeai as genai
    from PIL import Image, ImageDraw, ImageFont
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  google-generativeai or PIL not installed. AI features disabled.")
    print("   Install with: pip install google-generativeai pillow")


class FontCatalogManager:
    def __init__(self, token, repo_owner, repo_name, file_path="catalog.fonts.json", 
                 branch="main", gemini_api_key=None):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.file_path = file_path
        self.branch = branch
        self.gemini_api_key = gemini_api_key
        self.api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Initialize Gemini if available and key provided
        if self.gemini_api_key and GEMINI_AVAILABLE:
            genai.configure(api_key=self.gemini_api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
    
    def get_current_catalog(self):
        """Fetch the current catalog from GitHub"""
        response = requests.get(self.api_url, headers=self.headers, params={"ref": self.branch})
        
        if response.status_code == 200:
            content = response.json()
            file_content = b64decode(content["content"]).decode("utf-8")
            return json.loads(file_content), content["sha"]
        elif response.status_code == 404:
            print("⚠️  File not found. Will create new file.")
            return [], None
        else:
            raise Exception(f"Failed to fetch file: {response.status_code} - {response.text}")
    
    def update_catalog(self, catalog_data, sha, commit_message):
        """Update the catalog on GitHub"""
        content_bytes = json.dumps(catalog_data, indent=2, ensure_ascii=False).encode("utf-8")
        content_b64 = b64encode(content_bytes).decode("utf-8")
        
        payload = {
            "message": commit_message,
            "content": content_b64,
            "branch": self.branch
        }
        
        if sha:
            payload["sha"] = sha
        
        response = requests.put(self.api_url, headers=self.headers, json=payload)
        
        if response.status_code in [200, 201]:
            print("✅ Catalog updated successfully!")
            return True
        else:
            raise Exception(f"Failed to update file: {response.status_code} - {response.text}")
    
    def get_google_font_specimen(self, font_name):
        """Generate a visual specimen for Google Fonts"""
        try:
            # Try to get the font specimen from Google Fonts
            safe_name = font_name.replace(' ', '+')
            specimen_url = f"https://fonts.gstatic.com/s/a/{safe_name}.png"
            
            response = requests.get(specimen_url, timeout=5)
            if response.status_code == 200:
                return Image.open(io.BytesIO(response.content))
            
            # Alternative: Google Fonts specimen sheet
            alt_url = f"https://fonts.google.com/specimen/{safe_name}"
            # This won't give us direct image, so we'll use text rendering instead
            
            return None
        except Exception as e:
            print(f"　　　⚠️  Could not fetch Google Font specimen: {e}")
            return None
    
    def generate_font_specimen(self, font_name, source, url):
        """Generate a text specimen image showing how the font looks"""
        try:
            # Create a specimen image with sample text
            img = Image.new('RGB', (800, 400), color='white')
            draw = ImageDraw.Draw(img)
            
            # Sample text to show font characteristics
            sample_text = [
                f"{font_name}",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "abcdefghijklmnopqrstuvwxyz",
                "0123456789 !@#$%&*()_+-=",
                "The quick brown fox jumps over the lazy dog"
            ]
            
            # For now, use default font (we'll let Gemini analyze from URL or name)
            # In production, you'd download and render the actual font
            y_position = 20
            for text in sample_text:
                draw.text((20, y_position), text, fill='black')
                y_position += 70
            
            return img
        except Exception as e:
            print(f"　　　⚠️  Could not generate specimen: {e}")
            return None
    
    def analyze_font_visually(self, name, source, url, category):
        """Use Gemini to visually analyze the font's appearance"""
        if not self.model:
            return []
        
        try:
            # Try to get visual specimen
            font_image = None
            
            if source == "google":
                # For Google Fonts, try to get official specimen
                font_image = self.get_google_font_specimen(name)
            
            # If we have an image, analyze it visually
            if font_image:
                prompt = """Analyze this font specimen image carefully and describe ONLY what you see visually.

Look at the actual letterforms and identify:
- **Structure**: Is it geometric (constructed from circles/squares), organic (flowing/natural), modular (repeating shapes), grotesque (industrial), or humanist (calligraphic influence)?
- **Terminals**: Are the letter endings rounded, sharp, square, or angled?
- **Weight & Width**: Is it light, regular, bold, condensed, or extended?
- **Character Spacing**: Is it monospaced (fixed-width like coding fonts) or proportional?
- **X-height**: Is it tall or short compared to ascenders/descenders?
- **Stroke Contrast**: Is there high contrast (thick/thin variation) or low contrast (uniform)?
- **Style Period**: Does it look retro (70s/80s/90s), vintage (pre-1950s), contemporary (modern clean), or futuristic?
- **Mood**: Does it feel playful, serious, warm, cold, technical, elegant, casual, distressed?
- **Special Features**: Any unique characteristics like pixelation, distressing, decorative elements, hand-drawn quality?

Based ONLY on the visual appearance, generate 3-5 precise aesthetic tags.

Return ONLY comma-separated tags with no explanation.
Example: geometric, brutalist, contemporary, monospaced, coding"""

                response = self.model.generate_content([prompt, font_image])
                
            else:
                # Fallback: Use URL analysis for custom fonts or if image unavailable
                prompt = f"""Analyze how this font likely looks based on its URL and context:

Font Name: {name}
Source: {source}
Category: {category}
URL: {url}

From the URL path, font name, and category, infer the visual aesthetic:
- For ".woff2" custom fonts, analyze the filename for clues
- For Google Fonts, consider typical characteristics of that family
- For monospace category, it's likely coding-oriented
- Look for keywords in the name/URL like: rounded, condensed, display, text, mono, etc.

Generate 3-5 tags describing the VISUAL APPEARANCE:
- Structure: geometric, organic, humanist, grotesque, modular
- Style: retro, vintage, contemporary, futuristic, medieval
- Mood: playful, serious, calm, energetic, warm, cold
- Features: rounded, sharp, distressed, clean, monospaced, pixel
- Use: coding, display, formal, casual, technical, artistic

Return ONLY comma-separated tags.
Example: geometric, contemporary, clean, neutral, business"""

                response = self.model.generate_content(prompt)
            
            tags_text = response.text.strip()
            
            # Clean up response
            tags_text = tags_text.replace('*', '').replace('`', '').replace('#', '').strip()
            
            # Parse the response
            suggested_tags = [tag.strip().lower() for tag in tags_text.split(',') if tag.strip()]
            
            return suggested_tags[:5]  # Limit to 5 tags
            
        except Exception as e:
            print(f"　　　⚠️  AI analysis error: {e}")
            return []
    
    def add_font_interactive(self):
        """Interactive prompt to add a new font"""
        print("\n" + "═" * 67)
        print("　　　　　　　　░▒▓█  ＡＤＤＩＮＧ　ＦＯＮＴ  █▓▒░")
        print("═" * 67)
        
        # Get font details
        name = input("\n　Ｆ Ｏ Ｎ Ｔ 　Ｎ Ａ Ｍ Ｅ ： ").strip()
        
        print("\n　━━━ ＳＯＵＲＣＥ ━━━")
        print("　　　（google • custom • other）")
        source = input("　　　＞ ").strip().lower()
        
        print("\n　━━━ ＵＲＬ ━━━")
        url = input("　　　＞ ").strip()
        
        print("\n　━━━ ＣＡＴＥＧＯＲＹ ━━━")
        print("　　　（sans-serif • serif • monospace • display • handwriting）")
        category = input("　　　＞ ").strip().lower()
        
        # AI-powered visual tag analysis
        print("\n　━━━ ＴＡＧＳ ━━━")
        suggested_tags = []
        
        if self.model:
            print("　　　🤖 Analyzing font visual appearance...")
            suggested_tags = self.analyze_font_visually(name, source, url, category)
            
            if suggested_tags:
                print(f"　　　💡 AI Detected Visual Style: {', '.join(suggested_tags)}")
                print("　　　（Press Enter to accept, or type your own comma-separated tags）")
            else:
                print("　　　（Enter comma-separated tags）")
        else:
            print("　　　（Enter comma-separated tags, e.g., geometric,neutral,modern）")
        
        tags_input = input("　　　＞ ").strip()
        
        # Use suggested if empty, otherwise parse input
        if not tags_input and suggested_tags:
            tags = suggested_tags
            print(f"　　　✨ Using AI visual analysis: {', '.join(tags)}")
        else:
            tags = [tag.strip().lower() for tag in tags_input.split(",") if tag.strip()]
        
        # Create new font entry
        new_font = {
            "name": name,
            "source": source,
            "url": url,
            "category": category,
            "tags": tags
        }
        
        # Preview
        print("\n" + "═" * 67)
        print("　　　　　　　　░▒▓█  ＰＲＥＶＩＥＷ  █▓▒░")
        print("═" * 67)
        print(json.dumps(new_font, indent=2))
        print("═" * 67)
        
        confirm = input("\n　ＣＯＮＦＩＲＭ？ (yes/no)： ").strip().lower()
        
        if confirm in ['yes', 'y']:
            return new_font
        else:
            print("❌ Cancelled.")
            return None
    
    def run(self):
        """Main execution flow"""
        try:
            # Fetch current catalog
            print("\n🔍 Fetching current catalog from GitHub...")
            catalog, sha = self.get_current_catalog()
            print(f"✅ Found {len(catalog)} existing fonts")
            
            # Add new font interactively
            new_font = self.add_font_interactive()
            
            if new_font:
                # Check for duplicates
                if any(font["name"] == new_font["name"] for font in catalog):
                    print(f"\n⚠️  Font '{new_font['name']}' already exists!")
                    overwrite = input("　ＯＶＥＲＷＲＩＴＥ？ (yes/no)： ").strip().lower()
                    if overwrite in ['yes', 'y']:
                        catalog = [f for f in catalog if f["name"] != new_font["name"]]
                    else:
                        print("❌ Cancelled.")
                        return
                
                # Add to catalog
                catalog.append(new_font)
                
                # Update on GitHub
                commit_msg = f"Add {new_font['name']} to font catalog"
                print(f"\n📤 Uploading to GitHub...")
                self.update_catalog(catalog, sha, commit_msg)
                print(f"🎉 Successfully added '{new_font['name']}' to catalog!")
                
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    print("\n" + "═" * 67)
    print("　　　　　　░▒▓█  ＦＯＮＴ　ＣＡＴＡＬＯＧ　ＭＡＮＡＧＥＲ  █▓▒░")
    print("═" * 67)
    
    # Get credentials
    token = getpass("\n　ＧＩＴＨＵＢ　ＰＡＴ (hidden)： ")
    
    # Get repository in format username/repo-name
    while True:
        repo_full = input("\n　ＤＥＳＴＩＮＡＴＩＯＮ (username/repo-name)： ").strip()
        if "/" in repo_full:
            repo_owner, repo_name = repo_full.split("/", 1)
            repo_owner = repo_owner.strip()
            repo_name = repo_name.strip()
            if repo_owner and repo_name:
                break
        print("　❌ Invalid format. Use: username/repo-name")
    
    # Optional: custom file path and branch
    file_path = input("\n　ＦＩＬＥ　ＰＡＴＨ (default: catalog.fonts.json)： ").strip() or "catalog.fonts.json"
    branch = input("　ＢＲＡＮＣＨ (default: main)： ").strip() or "main"
    
    # Optional: Gemini API for AI tag suggestions
    gemini_key = None
    if GEMINI_AVAILABLE:
        use_ai = input("\n　Ｕ Ｓ Ｅ 　Ａ Ｉ 　Ｖ Ｉ Ｓ Ｕ Ａ Ｌ 　Ａ Ｎ Ａ Ｌ Ｙ Ｓ Ｉ Ｓ？ (yes/no)： ").strip().lower()
        if use_ai in ['yes', 'y']:
            gemini_key = getpass("　ＧＥＭＩＮＩ　ＡＰＩ　ＫＥＹ (hidden)： ")
    
    # Create manager and run
    manager = FontCatalogManager(token, repo_owner, repo_name, file_path, branch, gemini_key)
    manager.run()


if __name__ == "__main__":
    main()
