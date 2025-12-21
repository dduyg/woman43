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

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  google-generativeai not installed. AI features disabled.")
    print("   Install with: pip install google-generativeai")


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
    
    def analyze_font_with_gemini(self, name, source, url, category):
        """Use Gemini to analyze font and generate aesthetic tags"""
        if not self.model:
            return []
        
        try:
            prompt = f"""Analyze this font and describe its aesthetic characteristics:

Font Name: {name}
Source: {source}
Category: {category}
URL: {url}

Based on the font name, source, and technical category, generate 3-5 precise aesthetic tags that describe this font's visual style and personality.

Consider aspects like:
- Visual structure (geometric, organic, modular, grotesque, humanist, etc.)
- Mood/feeling (playful, serious, warm, cold, calm, energetic, etc.)
- Historical period (retro, futuristic, contemporary, vintage, medieval, etc.)
- Use case (coding, display, body text, branding, business, etc.)
- Stylistic traits (rounded, sharp, distressed, clean, brutalist, etc.)
- Special characteristics (monospaced, condensed, extended, handwritten, etc.)

Return ONLY the tags as a comma-separated list with no additional text, explanation, or formatting.
Example output: geometric, brutalist, contemporary, clean, modular"""

            response = self.model.generate_content(prompt)
            tags_text = response.text.strip()
            
            # Clean up response - remove any markdown or extra text
            tags_text = tags_text.replace('*', '').replace('`', '').strip()
            
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
        
        # AI-powered tag suggestion
        print("\n　━━━ ＴＡＧＳ ━━━")
        suggested_tags = []
        
        if self.model:
            print("　　　🤖 Analyzing font aesthetics with AI...")
            suggested_tags = self.analyze_font_with_gemini(name, source, url, category)
            
            if suggested_tags:
                print(f"　　　💡 AI Suggested: {', '.join(suggested_tags)}")
                print("　　　（Press Enter to accept, or type your own comma-separated tags）")
            else:
                print("　　　（Enter comma-separated tags）")
        else:
            print("　　　（Enter comma-separated tags, e.g., geometric,neutral,modern）")
        
        tags_input = input("　　　＞ ").strip()
        
        # Use suggested if empty, otherwise parse input
        if not tags_input and suggested_tags:
            tags = suggested_tags
            print(f"　　　✨ Using AI suggestions: {', '.join(tags)}")
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
        use_ai = input("\n　Ｕ Ｓ Ｅ 　Ａ Ｉ 　Ｔ Ａ Ｇ 　Ａ Ｎ Ａ Ｌ Ｙ Ｓ Ｉ Ｓ？ (yes/no)： ").strip().lower()
        if use_ai in ['yes', 'y']:
            gemini_key = getpass("　ＧＥＭＩＮＩ　ＡＰＩ　ＫＥＹ (hidden)： ")
    
    # Create manager and run
    manager = FontCatalogManager(token, repo_owner, repo_name, file_path, branch, gemini_key)
    manager.run()


if __name__ == "__main__":
    main()
