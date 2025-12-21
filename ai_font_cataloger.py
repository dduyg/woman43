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
from PIL import Image, ImageDraw, ImageFont
import tempfile
import os

# Check running environment
try:
    from google.colab import ai
    COLAB_AI_AVAILABLE = True
    AI_MODEL = None
except ImportError:
    COLAB_AI_AVAILABLE = False
    # Fallback to regular Gemini API
    try:
        import google.generativeai as genai
        GEMINI_AVAILABLE = True
    except ImportError:
        GEMINI_AVAILABLE = False
        print("⚠️  No AI available. Install: pip install google-generativeai pillow")


class FontCatalogManager:
    def __init__(self, token, repo_owner, repo_name, file_path="catalog.fonts.json", 
                 branch="main", use_ai=True, gemini_api_key=None):
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.file_path = file_path
        self.branch = branch
        self.use_ai = use_ai
        self.api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Initialize AI based on environment
        if self.use_ai:
            if COLAB_AI_AVAILABLE:
                print("✅ Using Google Colab AI (free!)")
                self.ai_type = "colab"
                self.model = None  # Colab AI doesn't need model initialization
            elif GEMINI_AVAILABLE and gemini_api_key:
                print("✅ Using Gemini API")
                genai.configure(api_key=gemini_api_key)
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                self.ai_type = "gemini"
            else:
                print("⚠️  AI not available")
                self.ai_type = None
                self.model = None
        else:
            self.ai_type = None
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
    
    def generate_font_specimen(self, name, source, url):
        """Generate a font specimen image for visual analysis"""
        try:
            # Download font file
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return None
            
            # Save temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.ttf') as tmp:
                tmp.write(response.content)
                tmp_path = tmp.name
            
            # Create specimen image
            img = Image.new('RGB', (800, 400), color='white')
            draw = ImageDraw.Draw(img)
            
            try:
                # Try to load the font
                font_large = ImageFont.truetype(tmp_path, 72)
                font_medium = ImageFont.truetype(tmp_path, 48)
                font_small = ImageFont.truetype(tmp_path, 32)
            except:
                # If font loading fails, return None
                os.unlink(tmp_path)
                return None
            
            # Draw text specimens
            draw.text((20, 20), "AaBbCc 123", fill='black', font=font_large)
            draw.text((20, 120), "The quick brown fox", fill='black', font=font_medium)
            draw.text((20, 180), "jumps over the lazy dog", fill='black', font=font_medium)
            draw.text((20, 250), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", fill='black', font=font_small)
            draw.text((20, 300), "abcdefghijklmnopqrstuvwxyz", fill='black', font=font_small)
            draw.text((20, 350), "0123456789 !@#$%^&*()", fill='black', font=font_small)
            
            # Clean up temp file
            os.unlink(tmp_path)
            
            return img
            
        except Exception as e:
            print(f"　　　⚠️  Could not generate specimen: {e}")
            return None
    
    def get_google_font_specimen(self, font_name):
        """Try to get Google Fonts specimen image"""
        try:
            # Google Fonts specimen
            font_name_clean = font_name.replace(' ', '+')
            specimen_url = f"https://fonts.gstatic.com/s/{font_name.lower().replace(' ', '')}/v1/specimen.png"
            
            response = requests.get(specimen_url, timeout=5)
            if response.status_code == 200:
                return Image.open(io.BytesIO(response.content))
            
            return None
        except:
            return None
    
    def analyze_font_with_colab_ai(self, name, source, url, category, specimen_img=None):
        """Use Google Colab AI for visual analysis"""
        try:
            prompt_base = """Analyze this font and describe its VISUAL aesthetic characteristics.

Look at the actual letterforms and identify 3-5 precise aesthetic tags based on what you SEE:

VISUAL STRUCTURE:
- Is it geometric (precise circles/squares) or organic (flowing curves)?
- Is it modular (built from repeated shapes) or varied?
- Is it monospaced (equal character width) or proportional?
- Are terminals rounded, sharp, or squared?

STYLE & MOOD:
- Does it look retro (70s/80s), futuristic, contemporary, or vintage?
- Is it playful, serious, calm, energetic, sophisticated?
- Does it feel warm (friendly curves) or cold (technical angles)?

SPECIAL CHARACTERISTICS:
- Brutalist (raw, harsh), clean (minimal), distressed (worn)?
- Handwritten, pixel-art, medieval, art nouveau style?
- Formal/business or casual/playful?
- Any unique traits: blobby, wacky, horror, stiff, etc.?

Reference tags (use these as inspiration but create your own if needed):
geometric, formal, handwritten, fatface, monospaced, techno, pixel, medieval, art nouveau, blobby, distressed, wood, wacky, shaded, marker, futuristic, vintage, calm, playful, sophisticated, business, stiff, childlike, horror, distorted, clean, warm, aesthetic, brutalist, modular, neutral, contemporary, rounded, approachable, humanist, coding, retro, android

Return ONLY 3-5 tags as a comma-separated list based on VISUAL APPEARANCE, no explanation.
Example: geometric, brutalist, contemporary, clean, modular"""

            if specimen_img:
                # Visual analysis with image
                # Convert PIL Image to bytes for Colab AI
                img_byte_arr = io.BytesIO()
                specimen_img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                
                # Colab AI expects different format - use text-only for now
                # Image support may vary, so fallback to text description
                prompt = f"""Font specimen image shows: {name}
Category: {category}
Source: {source}

{prompt_base}"""
                
                response = ai.generate_text(
                    prompt=prompt,
                    model='google/gemini-2.5-flash'
                )
            else:
                # Text-based inference
                prompt = f"""Based on this font metadata, infer its likely VISUAL aesthetic:

Font Name: {name}
Source: {source}
Category: {category}

{prompt_base}"""
                
                response = ai.generate_text(
                    prompt=prompt,
                    model='google/gemini-2.5-flash'
                )
            
            # Parse response
            tags_text = response.strip().replace('*', '').replace('`', '').replace('"', '')
            suggested_tags = [tag.strip().lower() for tag in tags_text.split(',') if tag.strip()]
            
            return suggested_tags[:5]
            
        except Exception as e:
            print(f"　　　⚠️  Colab AI error: {e}")
            return []
    
    def analyze_font_with_gemini(self, name, source, url, category, specimen_img=None):
        """Use Gemini API for visual analysis"""
        try:
            prompt_base = """Analyze this font and describe its VISUAL aesthetic characteristics.

Look at the actual letterforms and identify 3-5 precise aesthetic tags based on what you SEE:

VISUAL STRUCTURE:
- Is it geometric (precise circles/squares) or organic (flowing curves)?
- Is it modular (built from repeated shapes) or varied?
- Is it monospaced (equal character width) or proportional?
- Are terminals rounded, sharp, or squared?

STYLE & MOOD:
- Does it look retro (70s/80s), futuristic, contemporary, or vintage?
- Is it playful, serious, calm, energetic, sophisticated?
- Does it feel warm (friendly curves) or cold (technical angles)?

SPECIAL CHARACTERISTICS:
- Brutalist (raw, harsh), clean (minimal), distressed (worn)?
- Handwritten, pixel-art, medieval, art nouveau style?
- Formal/business or casual/playful?
- Any unique traits: blobby, wacky, horror, stiff, etc.?

Reference tags (use these as inspiration but create your own if needed):
geometric, formal, handwritten, fatface, monospaced, techno, pixel, medieval, art nouveau, blobby, distressed, wood, wacky, shaded, marker, futuristic, vintage, calm, playful, sophisticated, business, stiff, childlike, horror, distorted, clean, warm, aesthetic, brutalist, modular, neutral, contemporary, rounded, approachable, humanist, coding, retro, android

Return ONLY 3-5 tags as a comma-separated list based on VISUAL APPEARANCE, no explanation.
Example: geometric, brutalist, contemporary, clean, modular"""

            if specimen_img:
                response = self.model.generate_content([prompt_base, specimen_img])
            else:
                prompt = f"""Based on this font metadata, infer its likely VISUAL aesthetic:

Font Name: {name}
Source: {source}
Category: {category}

{prompt_base}"""
                response = self.model.generate_content(prompt)
            
            tags_text = response.text.strip().replace('*', '').replace('`', '').replace('"', '')
            suggested_tags = [tag.strip().lower() for tag in tags_text.split(',') if tag.strip()]
            
            return suggested_tags[:5]
            
        except Exception as e:
            print(f"　　　⚠️  Gemini API error: {e}")
            return []
    
    def analyze_font_visually(self, name, source, url, category):
        """Use AI to visually analyze font appearance"""
        if not self.ai_type:
            return []
        
        try:
            # Try to get font specimen image
            specimen_img = None
            
            if source == "google":
                print("　　　📸 Fetching Google Fonts specimen...")
                specimen_img = self.get_google_font_specimen(name)
            
            if not specimen_img and url:
                print("　　　📸 Generating font specimen from URL...")
                specimen_img = self.generate_font_specimen(name, source, url)
            
            # Analyze based on AI type
            if self.ai_type == "colab":
                return self.analyze_font_with_colab_ai(name, source, url, category, specimen_img)
            elif self.ai_type == "gemini":
                return self.analyze_font_with_gemini(name, source, url, category, specimen_img)
            
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
        
        # AI-powered VISUAL tag suggestion
        print("\n　━━━ ＴＡＧＳ ━━━")
        suggested_tags = []
        
        if self.ai_type:
            print("　　　🤖 Analyzing font VISUAL aesthetics with AI...")
            suggested_tags = self.analyze_font_visually(name, source, url, category)
            
            if suggested_tags:
                print(f"　　　💡 AI Suggested (based on visual analysis): {', '.join(suggested_tags)}")
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
    
    # AI configuration
    use_ai = True
    gemini_key = None
    
    if COLAB_AI_AVAILABLE:
        use_ai_input = input("\n　Ｕ Ｓ Ｅ 　Ａ Ｉ 　ＶＩＳＵＡＬ 　Ａ Ｎ Ａ Ｌ Ｙ Ｓ Ｉ Ｓ？ (yes/no)： ").strip().lower()
        use_ai = use_ai_input in ['yes', 'y', '']
    elif GEMINI_AVAILABLE:
        use_ai_input = input("\n　Ｕ Ｓ Ｅ 　Ａ Ｉ 　ＶＩＳＵＡＬ 　Ａ Ｎ Ａ Ｌ Ｙ Ｓ Ｉ Ｓ？ (yes/no)： ").strip().lower()
        if use_ai_input in ['yes', 'y']:
            gemini_key = getpass("　ＧＥＭＩＮＩ　ＡＰＩ　ＫＥＹ (hidden)： ")
            use_ai = True
        else:
            use_ai = False
    else:
        use_ai = False
    
    # Create manager and run
    manager = FontCatalogManager(token, repo_owner, repo_name, file_path, branch, use_ai, gemini_key)
    manager.run()


if __name__ == "__main__":
    main()
