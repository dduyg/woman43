# <samp>LiminalLoop ⛃⛂</samp>

> internet__moods

```html
<i class="fas fa-circle"></i>
<i class="fas fa-square"></i>
<i class="fas fa-database"></i>
<a href="../14/">➾</a>
```

<br>

<details>
<summary>&nbsp;<code>🪄 responsive font-size</code></summary>
<br>

> *To make the font size of your website responsive and look good on different screen sizes, you can adopt several strategies. The goal is to ensure text readability while adapting the size dynamically for different devices like mobile phones, tablets, and desktop monitors. Here are the key approaches to achieve this:*

## 1. Use Relative Units

Using relative units for font sizing, such as `em`, `rem`, or `vw`, allows the text to scale with the screen size, ensuring better responsiveness.

- **`rem` (Root Em)**: This is relative to the root element (`<html>`) font size. It's a stable choice for responsive typography.
- **`vw` (Viewport Width)**: This is relative to the viewport width. For example, `1vw` is 1% of the width of the viewport.

### Example CSS:

```css
html {
    font-size: 16px; /* Set the base font size for larger screens */
}

body {
    font-size: 1rem; /* The body text size will be 16px as 1rem = 16px */
    line-height: 1.6; /* Use a consistent line-height for readability */
}

@media (max-width: 1200px) {
    html {
        font-size: 15px; /* Slightly reduce font size on large tablets */
    }
}

@media (max-width: 768px) {
    html {
        font-size: 14px; /* Smaller font size for tablets */
    }
}

@media (max-width: 480px) {
    html {
        font-size: 13px; /* Adjust for smaller screens (mobile devices) */
    }
}
```

## 2. Fluid Typography (Using `vw`)

Another modern approach is using viewport-based units like `vw` to create **fluid typography**, meaning the text will scale according to the screen width.

### Example CSS:

```css
body {
    font-size: calc(1rem + 1vw); /* Combines a base size with a size relative to the viewport */
}
```

In this example, `calc(1rem + 1vw)` means that the font size will increase as the viewport width grows. The `1rem` ensures a base font size, and the `1vw` scales the text according to the viewport width.

## 3. Use Media Queries for Fine Control

For better control over typography across devices, use **media queries** to define specific font sizes for different screen widths.

### Example CSS with Media Queries:

```css
body {
    font-size: 1rem; /* Default for larger screens */
}

@media (max-width: 1200px) {
    body {
        font-size: 0.9rem; /* Slightly smaller for large tablets */
    }
}

@media (max-width: 768px) {
    body {
        font-size: 0.8rem; /* Smaller font for tablets */
    }
}

@media (max-width: 480px) {
    body {
        font-size: 0.75rem; /* Small font for mobile phones */
    }
}
```

## 4. Line Height and Letter Spacing

Maintaining good **line-height** and **letter-spacing** is important for readability. As you scale font sizes, ensure that line-height is appropriately set:

```css
body {
    line-height: 1.6; /* Ensures readability with proper spacing between lines */
    letter-spacing: 0.02em; /* Slightly adjusts the space between letters */
}
```

## 5. Consider Using CSS Clamp

The `clamp()` function allows you to set a dynamic font size with minimum and maximum limits:

```css
body {
    font-size: clamp(1rem, 2vw + 1rem, 2rem); /* Minimum 1rem, scales with viewport width, maximum 2rem */
}
```

This is a powerful approach because it combines fluid scaling with fixed boundaries, ensuring text doesn't become too small or too large.

<br><br>

<details>
<summary>&nbsp; <code>Common System Fonts</code> </summary>
<br>
  
```css
/* Sans-serif fonts */
font-family: "Arial", "Helvetica", sans-serif;
font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
font-family: "Verdana", Geneva, sans-serif;
font-family: "Tahoma", Geneva, sans-serif;
font-family: "Trebuchet MS", Helvetica, sans-serif;
font-family: "Arial Black", Gadget, sans-serif;
font-family: "Impact", Charcoal, sans-serif;
font-family: "Comic Sans MS", cursive, sans-serif;
font-family: "Arial Narrow", sans-serif;
font-family: "Century Gothic", sans-serif;
font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
font-family: "Optima", sans-serif;
```

```css
/* Serif fonts */
font-family: "Times New Roman", Times, serif;
font-family: "Times", Times New Roman, serif;
font-family: "Georgia", serif;
font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif;
font-family: "Book Antiqua", Palatino, serif;
font-family: "Garamond", serif;
font-family: "Baskerville", "Baskerville Old Face", "Hoefler Text", Garamond, "Times New Roman", serif;
font-family: "Cambria", Georgia, serif;
font-family: "Didot", serif;
font-family: "Rockwell", serif;
```

```css
/* Monospace fonts */
font-family: "Courier New", Courier, monospace;
font-family: "Courier", monospace;
font-family: "Lucida Console", Monaco, monospace;
font-family: "Monaco", monospace;
font-family: "Consolas", monospace;
font-family: "Menlo", monospace;
font-family: "Liberation Mono", monospace;
font-family: "Andale Mono", monospace;
font-family: "PT Mono", monospace;
/* ★★ */ font-family: "Roboto Mono", monospace;
font-family: "Source Code Pro", monospace;
font-family: "Inconsolata", monospace;
font-family: "IBM Plex Mono", monospace;
font-family: "Fira Mono", monospace;
```

</details>

<hr>
</details>

<details>
<summary>&nbsp;<code>🌆 .md <i>buttons</i></code></summary>

## Key Binding Buttons
*You can use the* `<kbd>` *tag.*

#### Link Outside
*The whole button is clickable, but doesn't have any color.*

[<kbd> <br> Title <br> </kbd>][Link]

[Link]: # 'Link with example title.'

#### Link Inside
*The button text is link colored, but only the text is clickable.*

<kbd> <br> [Title][Link] <br> </kbd>

[Link]: # 'Link with example title.'

## Shield Buttons
*You can use **badges** as buttons:*

[![Button](https://img.shields.io/badge/Title-EF2D5E?style=for-the-badge)](https://obsergallery.github.io)

*You can also use **icons** to indicate intent:*

[![Button](https://img.shields.io/badge/View%20Me-5F1F6D?style=for-the-badge&logo=materialdesignicons&logoColor=white)](https://obsergallery.github.io)

[![Button](https://img.shields.io/badge/Click%20Me-CB6100?style=for-the-badge&logo=zendesk&logoColor=white)](https://obsergallery.github.io)

[![Button](https://img.shields.io/badge/Button%20Click-DBA8ED?style=for-the-badge&logo=osf&logoColor=white)](https://obsergallery.github.io)

</details>

<details>
<summary>&nbsp;<code>🎴🏀 .js <i>comments</i></code></summary>

# JavaScript comments

```jsx
// =========================
//      Topic Introduction
// =========================
```


```jsx
/*******************************
          Topic Introduction
*******************************/
```

```javascript
// ---------------------------------------- \\
 //      Anchor Hover Effects for Body Copy    \\
// -------------------------------------------- \\
```

```jsx
/**********************************************
 *                                            *
 *              Topic Introduction            *
 *                                            *
 **********************************************/
```

```jsx
/* 
   _________ infoDropdown _________ 
  |                                | 
  |   here text text text text ''  | 
  |   here text text text text ''  | 
  |   here text text text text ''  | 
  |                                | 
  |                                | 
  |   here text text text text ''  |
  |   here text text text text ''  | 
  |                                | 
  |________________________________|
*/
```


```jsx
// Topic Introduction
// ------------------
```


```jsx
///////////////////////////////////////////////////////
////// Title-related Code
///////////////////////////////////////////////////////
```

```jsx
// ••••• Title-related Code •••••
```

```jsx
// >>> Title-related Code <<<
```

```jsx
// ====================================
// Title-related Code
// ====================================
```

```jsx
/*
 * ~~~ Title-related Code ~~~
 */
```

```jsx
// ------------ Title-related Code ------------
```

```jsx
/****************************************
 *           Title-related Code
 ****************************************/
```

```jsx
// ************** Input Handling **************
```

```jsx
// ============== Configuration ==============
```

```jsx
// ~~~~~~~~~~~~~~ Utility Functions ~~~~~~~~~~~~~~
```

```jsx
// ///////////////// Constants /////////////////
```

```jsx
// ^^^^^^^^^^^^^^ Data Structures ^^^^^^^^^^^^^^
```

```jsx
// ```````````````` Testing ````````````````
```

```jsx
// :::::::::::::::: Database Operations ::::::::::::::::
```

```jsx
// ------------------------
// Section: Animation Logic
// ------------------------
```

```jsx
// ******************************
// Section: User Interaction Logic
// ******************************
```

```jsx
/*
  +--------------------------+
  | Section: Rendering Logic |
  +--------------------------+
*/
```

```jsx
// ------------------------------
// Section: Event Handling Logic
// ------------------------------
```

```jsx
/******************************************************************
 ** Parameters for controlling various aspects of the simulation ~~
 ** ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~
 */
// Fill color for points; currently set to black
let pointFillColor = 0;
/******************************************************************/
```

</details>

<details>
<summary>&nbsp;<code>🧱 terminal colorPalettes</code></summary>
<br>
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/vscode-example.png" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/vim-example.png" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/specimen_2.png" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/emacs-example.png" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/helix-example.png" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/color01combi.jpeg" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/color02combi.jpg" width="250">
<img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/colorcombi03-comicmono.jpg" width="250">
 <img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/calling_code-2.jpg" width="250">
 <img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/goorm_code.jpg" width="250">
 <img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/maker_mono.jpg" width="250">
 <img src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop@main/01/new_heterodox_mono.jpg" width="250">
</details>

<details>
<summary>&nbsp;<code>🌐 jsDelivr CDN with GitHub</code></summary>
<br>

jsDelivr allows you to serve *any static file* from a *public GitHub repository*—fast, free, and reliable. This is useful for:
- Web projects
- Hosting assets (scripts, styles, media)
- Sharing static content without backend setup

## 🔧 jsDelivr GitHub URL Format
```
https://cdn.jsdelivr.net/gh/<username>/<repo>@<branch-or-commit>/<path/to/file>
```

- `@<branch>` (like `@main`) is optional; it defaults to the default branch.
- `@<commit>` is recommended for production use to avoid surprises when files change.

## ✅ Usage Examples

### 🟨 JavaScript File
GitHub Path:
```
https://github.com/user/my-repo/blob/main/js/main.js
```

jsDelivr URL:
```
https://cdn.jsdelivr.net/gh/user/my-repo/js/main.js
```

**Use in HTML:**
```html
<script src="https://cdn.jsdelivr.net/gh/user/my-repo/js/main.js"></script>
```

### 🟦 CSS File
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/user/my-repo/css/style.css">
```

### 🟪 Font File (`woff2`, `ttf`)
```css
@font-face {
  font-family: 'MyFont';
  src: url('https://cdn.jsdelivr.net/gh/user/my-repo/fonts/my-font.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
```

### 🟥 Image (`.png`, `.jpg`, `.svg`)

```html
<img src="https://cdn.jsdelivr.net/gh/user/my-repo/images/logo.png" alt="Logo">
```

### 🟩 Video File (`.mp4`)
```html
<video controls>
  <source src="https://cdn.jsdelivr.net/gh/user/my-repo/videos/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

### 🟫 JSON File
```
fetch("https://cdn.jsdelivr.net/gh/user/my-repo/data/config.json")
  .then(res => res.json())
  .then(data => console.log(data));
```

## 📌 Pinning to a Commit (Best Practice)
To prevent breaking changes when files are updated, pin the file to a **specific commit**.

1. Go to the GitHub file.
2. Click the file → click the "Copy permalink" (with commit hash).
3. Replace `main` with the commit hash:

**Example:**
```
https://cdn.jsdelivr.net/gh/user/my-repo@a1b2c3d4/js/main.js
```

## 💡 Tips
- Files must be in **public** repositories.
- Use the `gh/` prefix for GitHub; there's also support for `npm` and `WordPress`.
- jsDelivr automatically uses the best CDN node worldwide for fast delivery.
- 🧠 Works for all public files including SVG, MP3, ZIP, JSON, etc.

## 🔗 Real Example from Your Case

**GitHub File:**
```
https://raw.githubusercontent.com/dduyg/LiminalLoop/main/06/kemalizm.mp4
```

**jsDelivr URL:**
```
https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop/06/kemalizm.mp4
```

**Usage:**
```html
<video controls>
  <source src="https://cdn.jsdelivr.net/gh/dduyg/LiminalLoop/06/kemalizm.mp4" type="video/mp4">
</video>
```

## 🧪 Test Your Links
To verify a jsDelivr link:

- Open it in the browser.
- Check DevTools → Network to confirm it's loading via CDN.

</details>

<details>
<summary>&nbsp;<code>🌀 SVG optimizer</code></summary>
<br>

You can use tools like:

- 🔗 [**SVGOMG** (SVGO GUI)](https://jakearchibald.github.io/svgomg/)
- CLI tool: `svgo`

These **automatically remove metadata, compress path data**, and shorten the code **without changing the appearance**.

### Example using SVGOMG:

Upload your current SVG → Enable:

- **Remove editor data**
- **Cleanup IDs**
- **Minify path data**
- **Convert shapes to paths**

And copy the optimized version it gives you.
</details>

<details>
<summary>&nbsp;<code>🩻 &lt;img&gt; style properties</code></summary><br>

You can style an `<img>` tag in CSS using various properties to control its appearance, dimensions, position, and other effects. Below are some common ways to style an image in CSS:

## 1. Basic Styling
```css
img {
  width: 100px; /* Sets the width */
  height: auto; /* Maintains aspect ratio */
  border: 2px solid black; /* Adds a border */
  border-radius: 10px; /* Rounds the corners */
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Adds a shadow */
}
```

## 2. Responsive Images
Ensure the image scales properly on different devices:

```css
img {
  max-width: 100%; /* Ensures it doesn't exceed its container width */
  height: auto; /* Maintains aspect ratio */
}
```

## 3. Centering an Image
You can center an image using flexbox:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
img {
  max-width: 100%;
  height: auto;
}
```

## 4. Hover Effects
Add styles that apply when hovering over the image:

```css
img {
  transition: transform 0.3s ease;
}
img:hover {
  transform: scale(1.1); /* Slightly zooms in on hover */
  filter: brightness(120%); /* Brightens the image */
}
```

## 5. Add Filters
CSS filters let you adjust an image's appearance:

```css
img {
  filter: grayscale(50%); /* Makes the image partially black and white */
  opacity: 0.8; /* Reduces visibility slightly */
}
```

## 6. Clip or Mask an Image
Clip an image into a shape using clip-path or mask:

```css
img {
  clip-path: circle(50%); /* Makes the image circular */
  width: 150px;
  height: 150px;
}
```

## 7. Image Alignment
Align an image within text or a container:

```css
img {
  vertical-align: middle; /* Aligns with text */
  display: block; /* Removes inline spacing */
  margin: 0 auto; /* Centers within block containers */
}
```

## 8. Background Image
If the image is used as a background:

```css
.container {
  background-image: url('image.jpg');
  background-size: cover; /* Scales to cover the container */
  background-position: center; /* Centers the image */
  background-repeat: no-repeat; /* Prevents repeating */
  height: 300px;
  width: 100%;
}
```
</details>

<details>
<summary>&nbsp;<code>🗝 OpenAI API key Streamlit</code></summary><br>

### How to get an OpenAI API key for your Streamlit app

✅ 1. Create (or log into) your OpenAI account

Go to: https://platform.openai.com and log in.

✅ 2. Go to "API Keys"

Visit: https://platform.openai.com/settings/organization/api-keys

You will see a page like:

> “Create new secret key”

✅ 3. Click Create new secret key

Choose a name (example: streamlit_app).

Click Create.

You will get something like:

`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Copy it.
You will not see it again, so store it somewhere safe.


✅ 4. Add the key to your Streamlit app

If you deploy on Streamlit Cloud:

Create a file in your repo:

.streamlit/secrets.toml

`OPENAI_API_KEY = "sk-xxxxxxx"`

Then in your app code:

```
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
```

That's it.

⚠️ IMPORTANT

Do NOT commit the secret key into GitHub code.
Always store it in: Streamlit Cloud → Secrets

.streamlit/secrets.toml (not tracked by Git)

</details>

<details>
<summary>&nbsp;<code>🔗 Drive URL for code</code></summary>

## Getting a Direct Google Drive URL for Code
Getting a direct URL for a Google Drive file that works in code (often for downloading or direct embedding) requires converting the standard sharing link. This is because the standard link opens a web preview, not the raw file.

Here is the two-step process: **Share** and **Transform**.

### 1. Share the File Publicly

The file must be accessible to anyone with the link for the direct download URL to work outside of an authenticated session.

1.  **Open Google Drive** and locate your file.
2.  **Right-click** the file and select **Share**.
3.  In the sharing settings window, change the access from "Restricted" to **"Anyone with the link"**.
    * Set the permission to **Viewer**.
4.  Click **"Copy link"** to save the standard sharing URL.

The standard sharing link will look something like this:
`https://drive.google.com/file/d/**FILE_ID**/view?usp=sharing`

---

### 2. Transform the URL

You need to extract the unique **FILE\_ID** from the sharing link and embed it into a different Google service URL structure.

#### Identify the File ID

The **FILE\_ID** is the long string of characters located between `/d/` and `/view` in your standard sharing link:
`https://drive.google.com/file/d/**<-- THIS IS THE FILE_ID -->**/view?usp=sharing`

#### Construct the Direct URL

Replace `FILE_ID` in the template below with the actual ID you copied. This format tells Google Drive to serve the file directly as a download.

* **Direct Download URL Format:**
    `https://drive.google.com/uc?export=download&id=**FILE_ID**`

#### Example Conversion

| Type | Example URL |
| :--- | :--- |
| **Standard Sharing Link** | `https://drive.google.com/file/d/**1NAcyYvzOOUINBYuFLtCiRMN5Kk61n-or**/view?usp=sharing` |
| **Direct Download URL** | `https://drive.google.com/uc?export=download&id=**1NAcyYvzOOUINBYuFLtCiRMN5Kk61n-or**` |

### 🐍 Python Example (Using `requests`)

```python
import requests

# 1. Replace with your actual Direct Download URL
GOOGLE_DRIVE_URL = "[https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE](https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE)"
# 2. Define the local file name for the downloaded content
LOCAL_FILENAME = "downloaded_file.zip" 

try:
    # Use 'stream=True' to efficiently download large files
    response = requests.get(GOOGLE_DRIVE_URL, stream=True)
    response.raise_for_status() # Check for request errors (4xx or 5xx)

    # Write the content to the local file
    with open(LOCAL_FILENAME, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            # Filter out keep-alive chunks
            if chunk: 
                f.write(chunk)
    
    print(f"✅ File successfully downloaded and saved as: {LOCAL_FILENAME}")

except requests.exceptions.RequestException as e:
    print(f"❌ An error occurred during download: {e}")
```

### 🌐 JavaScript Example (Using fetch)
```javascript
// Replace with your actual Direct Download URL
const googleDriveUrl = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE";

async function fetchGoogleDriveFile() {
    try {
        const response = await fetch(googleDriveUrl);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Use .text() to read content as text (good for JSON, CSV, etc.)
        const fileContent = await response.text();
        
        console.log("✅ File content retrieved successfully!");
        console.log("--- START OF CONTENT ---");
        console.log(fileContent.substring(0, 200) + '...'); // Log the first 200 characters
        
    } catch (error) {
        console.error("❌ Failed to fetch the file:", error);
    }
}

fetchGoogleDriveFile();
```

### 💻 HTML Example (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Google Drive Direct Link Example</title>
</head>
<body>
    <h1>Download File from Google Drive</h1>

    <p>
        Click the link below to download the file directly from Google Drive.
        The `download` attribute suggests a filename to the user's browser.
    </p>

    <a 
        href="https://drive.google.com/uc?export=download&id=YOUR_FILE_ID_HERE" 
        download="My-Important-Document.zip"
    >
        ⬇️ Download My Document
    </a>

    <hr>
    
    <h2>Embedding an Image (Alternative)</h2>
    <p>
        To display an image without downloading, use the **`preview`** service:
    </p>
    
    <img 
        src="https://drive.google.com/uc?id=YOUR_IMAGE_FILE_ID&export=view" 
        alt="A Directly Embedded Image from Google Drive"
        style="max-width: 300px; border: 1px solid #ccc;"
    />
</body>
</html>
```

</details>
