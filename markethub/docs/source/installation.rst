Installation
============

Sphinx:
--------
- 1. Sphinx Setup aur Configuration

   command prompt mein apne project directory mein jaake yeh command run karein:

   ```
   sphinx-quickstart
   ```

- 2. Documentation Likhein: 
   Jaise, index.rst file mein introduction aur installation guide add kar sakte hain aur naye sections ke liye alag .rst files bana sakte hain.

- 3. Documentation Build Karna (Generate HTML)
   Apne project directory mein jaake yeh command run karein:
   Yeh command Sphinx documentation ko HTML format mein build karega aur output ko build/html/ folder mein save karega.
   ```
      make html
   ```

- 4. Documentation Dekhna
   Bas index.html par double-click karein, aur yeh aapke default web browser mein open ho jayega.

- 5. Documentation Update Karna
   Agar aap apne documentation mein koi update ya changes karte hain, to phir se make html command run karein taaki naye changes reflect hoon.
   Uske baad, index.html ko refresh karke updated documentation dekh sakte hain.