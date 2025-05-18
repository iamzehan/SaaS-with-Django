- **Preparation and Setup:**
    
    - Ensure you have the recommended prerequisites: some experience with Python 3 (understanding classes, functions, lists, dictionaries, math), CSS, and HTML. If needed, check out the creator's other courses like "30 days of Python" or "Try Django".
    - Have Visual Studio Code (VS Code) downloaded and ready, as this is the recommended editor. Git is also helpful for version control, and VS Code has it built-in.
    - **Watch the introduction** of the video to understand the course goals (building a SaaS to potentially generate recurring revenue), the modern technology stack used (Django, Stripe, Neon, TailwindCSS, Flowbite, GitHub Actions, Docker, Railway), and the philosophy behind the course (foundational code, iterating, deploying early).
    - **Pause the video** and **set up your local development environment**. Create the project folder (e.g., "SAS"), save the workspace in VS Code, create an "SRC" folder for Django code, create a `requirements.txt` file, create and activate a Python virtual environment, and install the specified dependencies using pip.
- **Core Django Development (Follow the Timeline):**
    
    - **Watch the section on creating the Django project.** Learn how to use `django-admin startproject` within the "SRC" folder using the period (`.`) to place the project files directly there.
    - **Code along and run the initial Django server** (`python manage.py runserver`) to see the default "Hello World" landing page.
    - **Watch and implement basic views and URLs**. Create a `views.py` file and a basic view function. Create or modify `urls.py` to route a URL path to the view function. Learn how Django functions can return HTML.
    - **Configure Templates**. Create a "templates" folder at the project root. Modify the `DIRS` setting in `settings.py` to include this folder. Create a basic HTML template (e.g., `home.html`) and update the view function to render it using Django's `render` function.
    - **Implement Template Inheritance and Includes**. Create a `base.html` template for structure. Learn how to make other templates extend `base.html` and include smaller snippets using Django template tags. Basic template logic like conditional statements (`{% if user.is_authenticated %}`) can also be explored.
- **Version Control and Deployment Preparation:**
    
    - **Watch the section on Git and GitHub**. Initialize a Git repository in the project root. Create and configure a `.gitignore` file to exclude files like the virtual environment and collected static files. Learn basic Git commands like `git add --all`, `git commit`, and `git push` or use the built-in VS Code Git interface.
    - **Create a remote repository on GitHub** and link your local repository to it (`git remote add origin ...`). Push your initial commit to GitHub. The code is available on the SAS foundations repo if you get stuck or want to reference it.
    - **Prepare for Deployment**. Watch the introduction to Docker and Railway. Create a `Dockerfile` and `Railway.toml` file, defining your application container and deployment settings. Define watch patterns in `Railway.toml`.
    - **Configure Environment Variables**. Learn the importance of environment variables for sensitive settings. Update `settings.py` to use `os.environ.get()` initially and then integrate the `python-decouple` library for more robust `.env` file handling.
- **Adding Functionality and Structure:**
    
    - **Set up a Production Database**. Watch the section on using Neon (serverless PostgreSQL). Learn how to create a database instance and obtain the connection string for Django.
    - **Structure Static Files**. Understand static files (CSS, JS, images) in Django. Create a dedicated "static-files" folder, organize vendor libraries, add it to `.gitignore`, and configure `STATICFILES_DIRS` and `STATIC_ROOT` in `settings.py`. Note that the included Tailwind/Flowbite theme is pre-built to avoid Node.js dependency issues in deployment, but a separate course exists for building your own theme.
    - **Implement Custom Management Commands**. Learn how to create a custom Django management command (e.g., `vendor_pole.py`) to automate tasks like downloading static files. Learn to use helper functions for reusable logic (e.g., downloading files). Integrate the command into the Dockerfile build process.
    - **Configure Email Sending**. Understand the need for transactional email. Configure Django's email settings using Gmail with an App Password (for local testing). Use the `sendtestemail` command to verify setup. Configure `ADMINS` and `MANAGERS` for error notifications.
- **User Management and Authentication:**
    
    - **Implement User Authentication and Allauth**. Integrate `django-allauth` for comprehensive authentication features beyond Django's built-in system. Configure `INSTALLED_APPS` and Allauth-specific settings. Include Allauth's URL patterns and run migrations. Learn about features like email verification and social authentication (e.g., GitHub).
    - **Explore Django Admin and User Management**. Learn to use the Django admin interface to manage users and permissions. Create a superuser and explore user data and permissions within the admin and the Django shell.
    - **Implement User Permissions and Groups**. Understand and use Django's built-in permission system. Manage permissions via the admin interface.
- **Implementing Stripe Integration:**
    
    - **Set up Subscription Pricing Models**. Define models for subscription plans and prices, linking them to Stripe IDs and managing features like 'featured' status and ordering for the Django pricing page.
    - **Create Pricing Views**. Develop views and templates to display subscription pricing information, often organized by interval (e.g., monthly, annual). Learn how to query and display the relevant subscription prices.
    - **Implement Stripe Checkout Integration**. Integrate with Stripe Checkout to handle user subscriptions. Learn how to create checkout sessions using Stripe's API via helper functions, providing details like line items (price ID), mode (subscription), success URL, and cancel URL. Understand how to redirect the user to the Stripe-hosted checkout page.
    - **Handle Checkout Success**. Create a view to handle the redirect back from Stripe after a successful checkout. Learn how to retrieve the checkout session details using the session ID provided by Stripe in the URL. Use the session details to get the subscription ID and retrieve the subscription details from Stripe.
    - **Process Subscription Data**. Learn to extract relevant data from the Stripe subscription object, such as the customer ID, plan/price ID, status, and current period start/end dates. Understand the need to convert Stripe timestamps to Python datetime objects. Store or update this information in your user subscription model in Django.
    - **Display User Subscription Status**. Create a view and template to show the user their current subscription details, including status, plan name, and period dates. Learn how to serialize subscription data for display or API use.
    - **Implement Subscription Cancellation**. Create a view to handle subscription cancellation requests. Learn how to use Stripe's API to cancel a subscription, specifically considering canceling "at period end" as a user-friendly option. Update the user subscription model/status based on the cancellation response.
- **Advanced/Automation Concepts:**
    
    - **Create Utility Functions**. Extract reusable logic (like refreshing subscription data from Stripe) into utility functions for use in different parts of the application (views, management commands).
    - **Develop Management Commands for Syncing**. Create a management command (e.g., `sync_user_subs`) to periodically sync subscription data from Stripe for multiple users. Learn to add arguments to management commands (e.g., `days_left`, `days_ago`, `clear_dangling`) to control their behavior.
    - **Implement Queryset Filtering**. Learn how to write custom Django queryset methods to filter subscriptions based on criteria like the end date being within a certain range of days (future or past). Use Django's timezone utilities for date/time comparisons.
    - **Schedule Commands with GitHub Actions**. Introduce GitHub Actions as a way to automate running Django management commands on a schedule using cron syntax. Learn about different workflow triggers (push, workflow_dispatch, schedule). Use resources like crontab.guru to understand cron syntax.
    - **Use GitHub Actions for Testing/Automation**. Set up basic GitHub Actions workflows for testing, including steps like checking out code using `actions/checkout`. Integrate the management commands into the GitHub Actions workflow to run automatically (e.g., daily sync) or manually.

Throughout this routine:

- **Pause and rewind** the video frequently, especially when the pace picks up.
- **Code along** exactly as shown, ensuring your virtual environment is activated and you are in the correct directory.
- **Run the commands** as demonstrated and check the output.
- **Troubleshoot errors** by reviewing the video, checking the error messages, and potentially comparing your code to the provided code on GitHub.
- **Use the Django admin** and other tools (like the Stripe dashboard if you're integrating Stripe) to verify changes and data.
- **Refer to documentation** (Django, Stripe, WhiteNoise, etc.) when mentioned or when seeking deeper understanding.

By following these steps and actively coding along with the video, you should be able to build the foundational SaaS application as demonstrated in the course.