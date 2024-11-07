Installation Guide
====================

1. **Prerequisites**:
    - Python 3.8+
    - Django 3.2+ (or the version used in your project)
    - Database setup (SQLite for development)
    

2. **Steps**:

   1. Clone the repository:
   
      .. code-block:: bash

         git clone <repository-url>

   2. Install dependencies:

      .. code-block:: bash

         pip install -r requirements.txt

   3. Run database migrations:

      .. code-block:: bash

         python manage.py migrate

   4. Create a superuser for admin access:

      .. code-block:: bash

         python manage.py createsuperuser

   5. Start the development server:

      .. code-block:: bash

         python manage.py runserver

    
**Sphinx**:
--------

-  **Sphinx Setup aur Configuration**:

   command prompt mein apne project directory mein jaake yeh command run karein:

   ```
   sphinx-quickstart
   ```

-  **Documentation Likhein**: 
   Jaise, index.rst file mein introduction aur installation guide add kar sakte hain aur naye sections ke liye alag .rst files bana sakte hain.

-  **Documentation Build Karna (Generate HTML)**:
   Apne project directory (markethub/docs) mein jaake yeh command run karein:
   Yeh command Sphinx documentation ko HTML format mein build karega aur output ko build/html/ folder mein save karega.
   ```
   make html   
   ```
   make clean: ye command all html file ko clean karega jo build/html folder ke andar create hue hai
   ```
   make clean   
   ```

-  **Documentation Dekhna**:
   Bas index.html par double-click karein, aur yeh aapke default web browser mein open ho jayega.

-  **Documentation Update Karna**:
   Agar aap apne documentation mein koi update ya changes karte hain, to phir se make html command run karein taaki naye changes reflect hoon.
   Uske baad, index.html ko refresh karke updated documentation dekh sakte hain.**