# How to Upload Documents to Glenorchy Capital Website

## Quick Start (Web Browser Method - Easiest!)

### Step 1: Accept GitHub Invitation
1. Check your email for GitHub invitation
2. Click "Accept invitation"
3. Create GitHub account if you don't have one

### Step 2: Navigate to Documents Folder
1. Go to: https://github.com/sherudogaro/gc-website
2. Click on the `documents` folder

### Step 3: Upload Your File
1. Click "Add file" button (top right) → Select "Upload files"
2. Drag and drop your PDF or click "choose your files"
3. Multiple files can be uploaded at once

### Step 4: Commit (Save) Your Changes
1. Scroll down to "Commit changes" section
2. Add a brief message like "Add Form ADV 2025"
3. Leave "Commit directly to the main branch" selected
4. Click green "Commit changes" button

### Step 5: Verify Upload
- File will be live within 1-2 minutes at:
  `https://glenorchycapital.com/documents/[your-filename]`

---

## File Naming Best Practices

✅ **Good names:**
- `form-adv-2025-q3.pdf`
- `quarterly-report-2025.pdf`
- `glenorchy-factsheet.pdf`

❌ **Avoid:**
- Spaces: `Form ADV 2025.pdf`
- Special characters: `Form_ADV(2025)!.pdf`
- Very long names

---

## Updating Existing Files

To replace an existing file with a new version:

1. Navigate to the file in GitHub
2. Click on the file name
3. Click the trash icon to delete
4. Commit the deletion
5. Upload the new version with the same name

OR

1. Upload a file with the exact same name
2. GitHub will prompt you to replace it
3. Commit the change

---

## Creating Subfolders

To organize documents in subfolders:

1. Click "Create new file" in documents folder
2. Type: `subfolder-name/filename.pdf`
3. The forward slash (/) creates a new folder
4. Example: `reports/2025/q3-report.pdf`

---

## Common Issues & Solutions

**Problem:** "Permission denied" error
**Solution:** Make sure you accepted the GitHub invitation

**Problem:** File doesn't appear on website
**Solution:** Wait 2-3 minutes; check filename has no spaces

**Problem:** Need to delete a file
**Solution:** Click on file → trash icon → commit deletion

---

## Linking to Documents from Website

Once uploaded, documents can be linked from any page:

**Direct link format:**
```
https://glenorchycapital.com/documents/filename.pdf
```

**Example in HTML:**
```html
<a href="/documents/form-adv-2025.pdf">Download Form ADV</a>
```

---

## Support

If you encounter any issues:
1. Ensure you're logged into GitHub
2. Check that you accepted the repository invitation
3. Try refreshing the page
4. Contact Lucas for assistance

---

## Security Notes

- All uploaded files are PUBLIC
- Anyone with the link can access them
- Don't upload confidential client information
- For private documents, use secure client portal instead